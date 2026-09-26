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
def learned_hosts(s):
    counts=Counter()
    for m in s.get("memory",[])[-300:]:
        try:
            h=urllib.parse.urlsplit(m.get("url","")).hostname
            if h:counts[h.lower()]+=1
        except Exception:pass
    preferred=["isro.gov.in","nasa.gov","noaa.gov","who.int","worldbank.org","imf.org","rbi.org.in","sebi.gov.in","pib.gov.in","data.gov.in","arxiv.org","nature.com","science.org"]
    out=[]
    for h in preferred+[h for h,_ in counts.most_common(20)]:
        if h and h not in out:out.append(h)
    return out[:24]

def default_genome():
    return {"query_weight":3.0,"trusted_bonus":1.0,"https_bonus":0.2,"title_bonus":2.0,"keyword_bonus":2.0,"summary_bonus":1.0,"keyword_min":3,"answer_top":4,"summary_chars":360}

def source_from_genome(g,hosts):
    stop=["the","and","for","with","that","this","from","into","your","you","are","was","were","have","has","had","but","not","can","will","would","about","what","when","where","which","their","there","than","then","them","they","its","our","out","all","also","more","most","how","why","who","an","of","to","in","on","at","is","it","as","be","or","by"]
    return '''"""EvoBot evolved pure core. Generated and benchmarked by the protected supervisor."""
STOPWORDS=%r
TRUSTED_HOSTS=%r
QUERY_WEIGHT=%r
TRUSTED_BONUS=%r
HTTPS_BONUS=%r
TITLE_BONUS=%r
KEYWORD_BONUS=%r
SUMMARY_BONUS=%r
KEYWORD_MIN=%r
ANSWER_TOP=%r
SUMMARY_CHARS=%r

def _tokens(text):
    out=[];word=""
    for ch in str(text).lower():
        if ch.isalnum() or ch in "_-":word+=ch
        elif word:
            if len(word)>=KEYWORD_MIN and word not in STOPWORDS:out.append(word)
            word=""
    if word and len(word)>=KEYWORD_MIN and word not in STOPWORDS:out.append(word)
    return out

def rank_urls(urls,query):
    q=set(_tokens(query));rows=[]
    for i,url in enumerate(urls):
        low=str(url).lower();score=sum(QUERY_WEIGHT for t in q if t in low)
        if any(h in low for h in TRUSTED_HOSTS):score+=TRUSTED_BONUS
        if low.startswith("https://"):score+=HTTPS_BONUS
        rows.append((score,-i,url))
    rows.sort(reverse=True)
    return [x[2] for x in rows]

def extract_keywords(text,limit=12):
    counts={}
    for t in _tokens(text):counts[t]=counts.get(t,0)+1
    rows=sorted([(-v,k) for k,v in counts.items()])
    return [k for _,k in rows[:max(1,int(limit))]]

def answer_hint(query,memories):
    q=set(_tokens(query));rows=[]
    for i,m in enumerate(memories):
        title=str(m.get("title","")).lower();summary=str(m.get("summary","")).lower();keys=[str(x).lower() for x in m.get("keywords",[])]
        score=0.0
        for t in q:
            if t in title:score+=TITLE_BONUS
            if t in keys:score+=KEYWORD_BONUS
            if t in summary:score+=SUMMARY_BONUS
        if score:rows.append((score,-i,m))
    rows.sort(reverse=True)
    out=[]
    for _,__,m in rows[:ANSWER_TOP]:
        out.append(str(m.get("title",""))+" — "+str(m.get("summary",""))[:SUMMARY_CHARS]+" ["+str(m.get("url",""))+"]")
    return "\\n\\n".join(out)
'''%(stop,hosts,float(g["query_weight"]),float(g["trusted_bonus"]),float(g["https_bonus"]),float(g["title_bonus"]),float(g["keyword_bonus"]),float(g["summary_bonus"]),int(g["keyword_min"]),int(g["answer_top"]),int(g["summary_chars"]))

def evaluate_core(env,s):
    base=benchmark(env)*6.0;points=base;total=6.0
    if isinstance(env,dict):rank,kw,hint=env["rank_urls"],env["extract_keywords"],env["answer_hint"]
    else:rank,kw,hint=env.rank_urls,env.extract_keywords,env.answer_hint
    cases=[
        (["https://example.com/bank-policy","https://www.rbi.org.in/"],"bank policy","rbi.org.in"),
        (["https://example.com/space-research","https://www.nasa.gov/"],"space research","nasa.gov"),
        (["https://example.com/science-paper","https://arxiv.org/abs/1234"],"science paper","arxiv.org"),
        (["https://random.example/python-docs","https://docs.python.org/3/"],"python docs","python.org")
    ]
    for urls,q,host in cases:
        total+=1
        try:
            r=list(rank(urls,q));points+=1 if r and host in r[0] else 0
        except Exception:pass
    mem=s.get("memory",[])
    for idx,m in enumerate(mem[-8:]):
        keys=m.get("keywords",[])
        if not keys:continue
        distract=[x for x in mem[max(0,len(mem)-30):] if x is not m][:3]
        sample=[m]+distract;total+=1
        try:
            h=str(hint(str(keys[0]),sample));points+=1 if str(m.get("url","")) in h else 0
        except Exception:pass
    return round(points/max(total,1),6)

def candidate_genomes(current):
    out=[];seen=set()
    def add(g):
        key=tuple(sorted(g.items()))
        if key not in seen:seen.add(key);out.append(g)
    add(dict(current))
    for v in [2.0,3.0,4.0]:g=dict(current);g["query_weight"]=v;add(g)
    for v in [2.0,4.0,6.0,8.0,10.0]:g=dict(current);g["trusted_bonus"]=v;add(g)
    for v in [1.0,2.0,3.0,4.0]:g=dict(current);g["title_bonus"]=v;add(g)
    for v in [1.0,2.0,3.0,4.0]:g=dict(current);g["keyword_bonus"]=v;add(g)
    for v in [0.5,1.0,1.5,2.0]:g=dict(current);g["summary_bonus"]=v;add(g)
    for v in [3,4,5]:g=dict(current);g["keyword_min"]=v;add(g)
    for v in [3,4,5,6]:g=dict(current);g["answer_top"]=v;add(g)
    for v in [280,360,480,600]:g=dict(current);g["summary_chars"]=v;add(g)
    # Coordinated variants let improvements emerge from interacting parameters.
    combos=[(3,8,3,3,1),(2,8,4,3,1.5),(3,10,4,4,1.5),(4,10,3,4,2)]
    for qw,tb,tib,kb,sb in combos:
        g=dict(current);g.update({"query_weight":float(qw),"trusted_bonus":float(tb),"title_bonus":float(tib),"keyword_bonus":float(kb),"summary_bonus":float(sb)});add(g)
    return out

def mutate(s):
    force=os.environ.get("EVOBOT_FORCE_MUTATE","").lower()=="true";runs=int(s.get("runs",0))
    hosts=learned_hosts(s);old_hosts=s.get("core_hosts",[])
    current_genome=dict(default_genome());current_genome.update(s.get("core_genome",{}))
    try:current_env=load_core();current_score=evaluate_core(current_env,s)
    except Exception:current_env=None;current_score=-1.0
    best_score=current_score;best_genome=current_genome;best_source=None;candidate_errors=[]
    for g in candidate_genomes(current_genome):
        try:
            src=source_from_genome(g,hosts);env=compile_candidate(src);score=evaluate_core(env,s)
            if score>best_score+1e-9:
                best_score=score;best_genome=g;best_source=src
        except Exception as e:
            if len(candidate_errors)<5:candidate_errors.append(f"{type(e).__name__}: {e}")
    # Even without a score increase, fold newly learned reliable hosts into code
    # periodically if it does not regress. This makes the mutable core reflect
    # accumulated web experience instead of merely storing it outside the code.
    if best_source is None and hosts!=old_hosts and (force or runs%3==0):
        try:
            src=source_from_genome(current_genome,hosts);env=compile_candidate(src);score=evaluate_core(env,s)
            if score+1e-9>=current_score:best_source=src;best_score=score;best_genome=current_genome
        except Exception:pass
    if best_source is not None:
        CORE_PATH.write_text(best_source.rstrip()+"\n",encoding="utf-8")
        s["core_genome"]=best_genome;s["core_hosts"]=hosts;s["core_version"]=int(s.get("core_version",1))+1
        s["metrics"]["candidate_promotions"]=int(s["metrics"].get("candidate_promotions",0))+1
        event(s,"core_promoted",f"Promoted evolved core v{s['core_version']}",baseline=current_score,candidate=best_score,hosts=len(hosts),genome=best_genome)
    else:
        s["metrics"]["candidate_rejections"]=int(s["metrics"].get("candidate_rejections",0))+1
        event(s,"core_unchanged","No candidate beat the current core",score=current_score,hosts=len(hosts),candidate_errors=candidate_errors)

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
