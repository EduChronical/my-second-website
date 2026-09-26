#!/usr/bin/env python3
from __future__ import annotations
import ast, hashlib, importlib.util, ipaddress, json, os, re, socket, sys, time
import urllib.parse, urllib.request, urllib.robotparser
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

EVOBOT=Path(__file__).resolve().parents[1]
STATE_PATH=EVOBOT/"state.json"; CORE_PATH=EVOBOT/"generated_core.py"; SEEDS_PATH=EVOBOT/"worker"/"seeds.json"
MODEL_ENDPOINT="https://models.github.ai/inference/chat/completions"
UA="EvoBotResearch/2.0 (+https://educhronical.github.io/my-second-website/evobot/)"
MAX_MEMORY=600; MAX_FRONTIER=2500; MAX_EVENTS=100; MAX_FAILURES=120

def utcnow(): return datetime.now(timezone.utc).isoformat(timespec="seconds")
def load_json(path,default):
    try:return json.loads(path.read_text(encoding="utf-8"))
    except Exception:return default
def save_json(path,value): path.write_text(json.dumps(value,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
def base_state():
    return {"schema":2,"generation":1,"core_version":1,"runs":0,"pages_learned":0,"last_run":None,"last_model_mutation":None,
    "frontier":[],"visited":{},"memory":[],"failures":[],"events":[],"metrics":{"successful_fetches":0,"failed_fetches":0,
    "duplicate_pages":0,"candidate_promotions":0,"candidate_rejections":0}}
def load_state():
    s=base_state(); old=load_json(STATE_PATH,{})
    if isinstance(old,dict):s.update(old)
    for k,v in base_state().items():
        if k not in s:s[k]=v
    return s
def event(s,kind,message,**extra):
    s.setdefault("events",[]).insert(0,{"at":utcnow(),"kind":kind,"message":message,**extra});s["events"]=s["events"][:MAX_EVENTS]
def failure(s,url,error):
    s.setdefault("failures",[]).append({"at":utcnow(),"url":url,"error":error[:500]});s["failures"]=s["failures"][-MAX_FAILURES:]
    s["metrics"]["failed_fetches"]=int(s["metrics"].get("failed_fetches",0))+1

def norm_url(url,base=None):
    try:
        u=urllib.parse.urljoin(base or "",url.strip());p=urllib.parse.urlsplit(u)
        if p.scheme not in {"http","https"} or not p.hostname or p.username or p.password:return None
        host=p.hostname.lower().rstrip(".")
        if host in {"localhost","localhost.localdomain"} or host.endswith(".local"):return None
        q=[(k,v) for k,v in urllib.parse.parse_qsl(p.query,keep_blank_values=False) if not k.lower().startswith("utm_") and k.lower() not in {"fbclid","gclid"}]
        return urllib.parse.urlunsplit((p.scheme,p.netloc,p.path or "/",urllib.parse.urlencode(q),""))[:2048]
    except Exception:return None
def public_host(url):
    try:
        host=urllib.parse.urlsplit(url).hostname
        if not host:return False
        for info in socket.getaddrinfo(host,None):
            ip=ipaddress.ip_address(info[4][0])
            if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_multicast or ip.is_reserved or ip.is_unspecified:return False
        return True
    except Exception:return False
def robots_allowed(url,cache):
    try:
        p=urllib.parse.urlsplit(url);root=f"{p.scheme}://{p.netloc}"
        if root in cache:return cache[root]
        rp=urllib.robotparser.RobotFileParser(root+"/robots.txt");rp.set_url(root+"/robots.txt")
        try:rp.read();ok=rp.can_fetch(UA,url)
        except Exception:ok=True
        cache[root]=ok;return ok
    except Exception:return False
def get(url,timeout=20,max_bytes=800000):
    req=urllib.request.Request(url,headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml,text/plain,application/json,application/xml;q=0.8,*/*;q=0.2"})
    with urllib.request.urlopen(req,timeout=timeout) as r:
        ctype=r.headers.get("content-type","").split(";",1)[0].strip().lower();data=r.read(max_bytes+1)[:max_bytes];return data,ctype
def fetch_text(url):
    try:
        data,_=get("https://r.jina.ai/"+url,25,700000);text=data.decode("utf-8","replace")
        if len(text.strip())>=120:
            links=re.findall(r"\[[^\]]{0,120}\]\((https?://[^)\s]+)\)",text)+re.findall(r"(?<!\()\bhttps?://[^\s<>'\"]+",text)
            return text,links
    except Exception:pass
    data,ctype=get(url,20,700000);raw=data.decode("utf-8","replace")
    if "html" in ctype or "<html" in raw[:500].lower():
        links=re.findall(r"href=[\"']([^\"'#]+)",raw,flags=re.I)
        text=re.sub(r"(?is)<(script|style|noscript|svg).*?>.*?</\1>"," ",raw);text=re.sub(r"(?s)<[^>]+>"," ",text)
        text=re.sub(r"&nbsp;"," ",text,flags=re.I);text=re.sub(r"&amp;","&",text,flags=re.I)
        return re.sub(r"\s+"," ",text).strip(),links
    return raw,[]
def title(text,url):
    for pat in [r"(?im)^Title:\s*(.+)$",r"(?im)^#\s+(.+)$"]:
        m=re.search(pat,text)
        if m:return m.group(1).strip()[:220]
    p=urllib.parse.urlsplit(url);return (p.hostname or "")+(p.path if p.path!="/" else "")
def compact(text,n=2600):return re.sub(r"\s+"," ",text).strip()[:n]
def digest(text):return hashlib.sha256(text.encode("utf-8","ignore")).hexdigest()
def load_core(path=CORE_PATH):
    spec=importlib.util.spec_from_file_location("evobot_generated_core",path)
    if not spec or not spec.loader:raise RuntimeError("cannot load generated core")
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def seed_queue(s):
    seeds=load_json(SEEDS_PATH,[]);frontier=s.setdefault("frontier",[]);seen=set(s.get("visited",{}))|set(frontier)
    for u in seeds if isinstance(seeds,list) else []:
        n=norm_url(u)
        if n and n not in seen:frontier.append(n);seen.add(n)
    s["frontier"]=frontier[:MAX_FRONTIER]
def remember(s,core,url,text):
    cleaned=compact(text);h=digest(cleaned)
    if any(x.get("hash")==h for x in s.get("memory",[])[-250:]):
        s["metrics"]["duplicate_pages"]=int(s["metrics"].get("duplicate_pages",0))+1;return False
    try:kws=list(core.extract_keywords(cleaned,14))[:14]
    except Exception:kws=[]
    s.setdefault("memory",[]).append({"url":url,"title":title(text,url),"summary":cleaned[:900],"keywords":[str(x)[:60] for x in kws],"hash":h,"learned_at":utcnow()})
    s["memory"]=s["memory"][-MAX_MEMORY:];s["pages_learned"]=int(s.get("pages_learned",0))+1;s["metrics"]["successful_fetches"]=int(s["metrics"].get("successful_fetches",0))+1
    return True
def crawl(s,core):
    seed_queue(s);frontier=s["frontier"];visited=s.setdefault("visited",{});robots={};per_domain=Counter()
    try:
        q=" ".join(k for m in s.get("memory",[])[-40:] for k in m.get("keywords",[])[:2]);ranked=[u for u in core.rank_urls(frontier[:300],q) if u in frontier]
        frontier[:]=ranked+[u for u in frontier if u not in set(ranked)]
    except Exception:pass
    successes=attempts=0
    while frontier and attempts<24 and successes<8:
        attempts+=1;url=frontier.pop(0)
        if url in visited:continue
        host=urllib.parse.urlsplit(url).hostname or ""
        if per_domain[host]>=2:frontier.append(url);continue
        if not public_host(url):visited[url]={"at":utcnow(),"status":"blocked_nonpublic"};continue
        if not robots_allowed(url,robots):visited[url]={"at":utcnow(),"status":"robots_disallow"};continue
        per_domain[host]+=1
        try:
            text,links=fetch_text(url)
            if len(text.strip())<80:raise ValueError("too little readable text")
            if remember(s,core,url,text):successes+=1
            visited[url]={"at":utcnow(),"status":"ok","hash":digest(compact(text))}
            new=[]
            for link in links[:80]:
                n=norm_url(link,url)
                if n and n not in visited and n not in frontier:new.append(n)
            frontier.extend([x for x in new if urllib.parse.urlsplit(x).hostname==host][:8]+[x for x in new if urllib.parse.urlsplit(x).hostname!=host][:6]);frontier[:]=frontier[:MAX_FRONTIER]
        except Exception as e:
            visited[url]={"at":utcnow(),"status":"error","error":str(e)[:250]};failure(s,url,f"{type(e).__name__}: {e}")
        time.sleep(.2)
    if len(visited)>4000:s["visited"]=dict(list(visited.items())[-4000:])
    event(s,"crawl",f"Crawl cycle learned {successes} new pages",attempted=attempts,frontier=len(frontier))

SAFE={"len":len,"str":str,"int":int,"float":float,"range":range,"min":min,"max":max,"sorted":sorted,"set":set,"list":list,"dict":dict,"sum":sum,"enumerate":enumerate,"zip":zip,"abs":abs,"any":any,"all":all,"round":round}
def validate(source):
    if not source or len(source)>14000:return False,"source empty or too large"
    try:tree=ast.parse(source)
    except SyntaxError as e:return False,f"syntax error: {e}"
    required={"rank_urls","extract_keywords","answer_hint"};found=set()
    for node in tree.body:
        if not isinstance(node,(ast.FunctionDef,ast.Assign,ast.Expr)):return False,f"forbidden top-level {type(node).__name__}"
        if isinstance(node,ast.Expr) and not (isinstance(node.value,ast.Constant) and isinstance(node.value.value,str)):return False,"only docstrings allowed at module level"
        if isinstance(node,ast.FunctionDef):found.add(node.name)
    if not required.issubset(found):return False,f"missing functions {sorted(required-found)}"
    bad_names={"open","exec","eval","compile","__import__","input","breakpoint"};bad_attrs={"system","popen","spawn","connect","urlopen","request","unlink","remove","rmdir","write_text","write_bytes"}
    for node in ast.walk(tree):
        if isinstance(node,(ast.Import,ast.ImportFrom,ast.Global,ast.Nonlocal,ast.With,ast.AsyncWith,ast.Await,ast.AsyncFunctionDef,ast.ClassDef,ast.Lambda)):return False,f"forbidden node {type(node).__name__}"
        if isinstance(node,ast.Name) and node.id in bad_names:return False,f"forbidden name {node.id}"
        if isinstance(node,ast.Attribute) and node.attr in bad_attrs:return False,f"forbidden attribute {node.attr}"
    return True,"ok"
def compile_candidate(source):
    ok,why=validate(source)
    if not ok:raise ValueError(why)
    env={"__builtins__":SAFE};exec(compile(source,"<candidate_core>","exec"),env,env);return env
def benchmark(env):
    if isinstance(env,dict):rank,kw,hint=env["rank_urls"],env["extract_keywords"],env["answer_hint"]
    else:rank,kw,hint=env.rank_urls,env.extract_keywords,env.answer_hint
    score=0;total=6
    for urls,q,expected in [(["https://x.test/cats","https://x.test/space/rocket","https://x.test/music"],"rocket space","rocket"),(["https://x.test/python","https://x.test/civil-engineering","https://x.test/news"],"civil engineering","civil-engineering")]:
        try:
            r=list(rank(urls,q));score+=1 if r and expected in r[0] else 0
        except Exception:pass
    for text,expected in [("quantum quantum entanglement photon physics quantum","quantum"),("foundation soil bearing capacity soil settlement","soil")]:
        try:score+=1 if expected in [str(x).lower() for x in kw(text,8)] else 0
        except Exception:pass
    try:
        mem=[{"title":"ISRO mission update","summary":"ISRO launched a satellite mission","keywords":["isro","mission"],"url":"https://isro.gov.in/"},{"title":"Cooking","summary":"recipe","keywords":["food"],"url":"https://example.com/food"}]
        score+=1 if "isro" in str(hint("latest ISRO mission",mem)).lower() else 0;score+=1 if isinstance(hint("unknown subject",mem),str) else 0
    except Exception:pass
    return round(score/total,4)
def model(messages):
    token=os.environ.get("GITHUB_TOKEN","").strip()
    if not token:raise RuntimeError("GITHUB_TOKEN unavailable")
    body=json.dumps({"model":os.environ.get("EVOBOT_MODEL","openai/gpt-4.1"),"temperature":.2,"messages":messages,"max_tokens":5000}).encode()
    req=urllib.request.Request(MODEL_ENDPOINT,data=body,method="POST",headers={"Authorization":f"Bearer {token}","Content-Type":"application/json","Accept":"application/json"})
    with urllib.request.urlopen(req,timeout=60) as r:return json.loads(r.read().decode())["choices"][0]["message"]["content"]
def parse_candidate(text):
    text=text.strip()
    sm=re.search(r"<SOURCE>\\s*(.*?)\\s*</SOURCE>",text,re.S|re.I)
    rm=re.search(r"<RATIONALE>\\s*(.*?)\\s*</RATIONALE>",text,re.S|re.I)
    if sm:return sm.group(1).strip(),(rm.group(1).strip() if rm else "AI mutation")
    fence=chr(96)*3
    if fence in text:
        parts=text.split(fence)
        for part in parts:
            p=part.strip()
            if p.startswith("python"):p=p[6:].lstrip()
            if "def rank_urls" in p and "def extract_keywords" in p and "def answer_hint" in p:return p,"AI mutation"
    raise ValueError("model response did not contain a source module")
def mutate(s):
    runs=int(s.get("runs",0));recent=s.get("failures",[])[-10:]
    force=os.environ.get("EVOBOT_FORCE_MUTATE","").lower()=="true"
    if not (force or runs%12==0 or (len(recent)>=6 and s.get("last_model_mutation")!=s.get("last_run"))):return
    current=CORE_PATH.read_text(encoding="utf-8");curmod=load_core();baseline=benchmark(curmod);topics=Counter(k for m in s.get("memory",[])[-80:] for k in m.get("keywords",[])).most_common(20)
    prompt=f"""Improve EvoBot's MUTABLE PURE CORE. A protected supervisor owns networking, files, secrets, execution and promotion.
Required functions:
rank_urls(urls, query) -> list of the input URLs, best first
extract_keywords(text, limit=12) -> list[str]
answer_hint(query, memories) -> str
Hard constraints: no imports; no file/network/process access; no eval/exec/open; no classes; deterministic; source under 12000 chars.
Current benchmark: {baseline}
Recent topics: {topics}
Recent crawler failures: {recent}
CURRENT CORE:
{current}
Return exactly this format and nothing else:\n<RATIONALE>short explanation</RATIONALE>\n<SOURCE>\ncomplete Python module\n</SOURCE>"""
    try:
        raw=model([{"role":"system","content":"Produce conservative, testable code improvements and obey the tagged output contract exactly."},{"role":"user","content":prompt}])
        source,rationale=parse_candidate(raw);rationale=rationale[:600];env=compile_candidate(source);cand=benchmark(env)
        if cand+1e-9<baseline:raise ValueError(f"benchmark regression {baseline}->{cand}")
        if digest(source)==digest(current):raise ValueError("candidate identical")
        CORE_PATH.write_text(source.rstrip()+"\n",encoding="utf-8");s["core_version"]=int(s.get("core_version",1))+1;s["last_model_mutation"]=utcnow()
        s["metrics"]["candidate_promotions"]=int(s["metrics"].get("candidate_promotions",0))+1;event(s,"core_promoted",f"Promoted mutable core v{s['core_version']}",baseline=baseline,candidate=cand,rationale=rationale)
    except Exception as e:
        s["last_model_mutation"]=utcnow();s["metrics"]["candidate_rejections"]=int(s["metrics"].get("candidate_rejections",0))+1;event(s,"core_rejected","Rejected proposed core mutation",reason=f"{type(e).__name__}: {e}"[:700])
def main():
    s=load_state();s["runs"]=int(s.get("runs",0))+1;s["generation"]=int(s.get("generation",1))+1;s["last_run"]=utcnow()
    try:core=load_core()
    except Exception as e:print("Core load failed",e,file=sys.stderr);return 2
    try:crawl(s,core)
    except Exception as e:event(s,"supervisor_error","Crawler failed",reason=f"{type(e).__name__}: {e}"[:700])
    try:mutate(s)
    except Exception as e:event(s,"supervisor_error","Mutation failed",reason=f"{type(e).__name__}: {e}"[:700])
    save_json(STATE_PATH,s);print(json.dumps({"run":s["runs"],"generation":s["generation"],"core_version":s["core_version"],"pages_learned":s["pages_learned"],"frontier":len(s["frontier"]),"last_run":s["last_run"]},indent=2));return 0
if __name__=="__main__":raise SystemExit(main())
