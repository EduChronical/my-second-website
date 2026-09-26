"""EvoBot mutable pure core v1.

The protected supervisor may replace this module after validation and tests.
It intentionally has no networking, file or process capabilities.
"""

STOPWORDS = {
    "the","and","for","with","that","this","from","into","your","you","are","was","were","have","has","had",
    "but","not","can","will","would","about","what","when","where","which","their","there","than","then","them",
    "they","its","our","out","all","also","more","most","how","why","who","an","of","to","in","on","at","is",
    "it","as","be","or","by"
}

def _tokens(text):
    out=[]; word=""
    for ch in str(text).lower():
        if ch.isalnum() or ch in "_-":
            word += ch
        elif word:
            if len(word)>2 and word not in STOPWORDS: out.append(word)
            word=""
    if word and len(word)>2 and word not in STOPWORDS: out.append(word)
    return out

def rank_urls(urls, query):
    q=set(_tokens(query)); scored=[]
    for i,url in enumerate(urls):
        low=str(url).lower()
        score=sum(3 for token in q if token in low)
        if ".gov" in low or ".edu" in low: score += 1
        if low.startswith("https://"): score += 0.2
        scored.append((score,-i,url))
    scored.sort(reverse=True)
    return [x[2] for x in scored]

def extract_keywords(text, limit=12):
    counts={}
    for token in _tokens(text): counts[token]=counts.get(token,0)+1
    ranked=sorted(counts.items(),key=lambda kv:(-kv[1],kv[0]))
    return [k for k,_ in ranked[:max(1,int(limit))]]

def answer_hint(query, memories):
    q=set(_tokens(query)); best=[]
    for m in memories:
        hay=" ".join([str(m.get("title","")),str(m.get("summary",""))," ".join(m.get("keywords",[]))]).lower()
        score=sum(1 for t in q if t in hay)
        if score: best.append((score,m))
    best.sort(key=lambda x:-x[0])
    rows=[]
    for _,m in best[:4]:
        rows.append(str(m.get("title",""))+" — "+str(m.get("summary",""))[:360]+" ["+str(m.get("url",""))+"]")
    return "\n\n".join(rows)
