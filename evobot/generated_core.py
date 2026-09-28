"""EvoBot evolved pure core. Generated and benchmarked by the protected supervisor."""
STOPWORDS=['the', 'and', 'for', 'with', 'that', 'this', 'from', 'into', 'your', 'you', 'are', 'was', 'were', 'have', 'has', 'had', 'but', 'not', 'can', 'will', 'would', 'about', 'what', 'when', 'where', 'which', 'their', 'there', 'than', 'then', 'them', 'they', 'its', 'our', 'out', 'all', 'also', 'more', 'most', 'how', 'why', 'who', 'an', 'of', 'to', 'in', 'on', 'at', 'is', 'it', 'as', 'be', 'or', 'by']
TRUSTED_HOSTS=['isro.gov.in', 'nasa.gov', 'noaa.gov', 'who.int', 'worldbank.org', 'imf.org', 'rbi.org.in', 'sebi.gov.in', 'pib.gov.in', 'data.gov.in', 'arxiv.org', 'nature.com', 'science.org', 'science.nasa.gov', 'www.nasa.gov', 'assets.science.nasa.gov', 'www.nature.com', 'spaceplace.nasa.gov', 'www.pib.gov.in', 'plus.nasa.gov', 'static.pib.gov.in', 'www.sebi.gov.in', 'www.imf.org', 'www.rbi.org.in']
QUERY_WEIGHT=3.0
TRUSTED_BONUS=8.0
HTTPS_BONUS=0.2
TITLE_BONUS=2.0
KEYWORD_BONUS=2.0
SUMMARY_BONUS=1.0
KEYWORD_MIN=3
ANSWER_TOP=4
SUMMARY_CHARS=360

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
    return "\n\n".join(out)
