const SKEY="evobot.internet.state.v1",WKEY="evobot.internet.web.session",AKEY="evobot.internet.ai.session";
const $=id=>document.getElementById(id);
function baseState(){return {memory:{},failures:[],history:[],sources:0,generation:1,autoWeb:true}}
let state=load();
function load(){try{return Object.assign(baseState(),JSON.parse(localStorage.getItem(SKEY)||"{}"))}catch(e){return baseState()}}
function save(){localStorage.setItem(SKEY,JSON.stringify(state))}
function norm(x){return String(x==null?"":x).trim()}
function webCfg(){try{return JSON.parse(sessionStorage.getItem(WKEY)||"{}")}catch(e){return {}}}
function aiCfg(){try{return JSON.parse(sessionStorage.getItem(AKEY)||"{}")}catch(e){return {}}}
function webHeaders(){const c=webCfg(),h={Accept:"text/plain"};if(c.key)h.Authorization="Bearer "+c.key;return h}
function validUrl(u){try{const x=new URL(u);return /^https?:$/.test(x.protocol)?x.href:null}catch(e){return null}}

async function readUrl(url){
 const u=validUrl(url);if(!u)return "Invalid http/https URL.";
 const ctl=new AbortController(),tm=setTimeout(()=>ctl.abort(),30000);
 try{
  const r=await fetch("https://r.jina.ai/"+u,{headers:webHeaders(),signal:ctl.signal});
  const t=(await r.text()).slice(0,60000);
  if(!r.ok)throw new Error("HTTP "+r.status+" "+t.slice(0,220));
  state.sources++;save();render();
  return "SOURCE: "+u+"\n\n"+t;
 }catch(e){return "Web reader failed: "+e.message+"\n\nThe page may require login/CAPTCHA, block automated access, or the reader service may be rate-limited."}
 finally{clearTimeout(tm)}
}

async function searchWeb(q){
 q=norm(q);const c=webCfg();
 if(!q)return "Enter a search query.";
 if(!c.key)return "LIVE SEARCH NEEDS A KEY\n\nOpen Internet research connector and enter a Jina API key for this browser session. Direct URL reading can still work without a key.";
 const ctl=new AbortController(),tm=setTimeout(()=>ctl.abort(),35000);
 try{
  const r=await fetch("https://s.jina.ai/?q="+encodeURIComponent(q),{headers:webHeaders(),signal:ctl.signal});
  const t=(await r.text()).slice(0,80000);
  if(!r.ok)throw new Error("HTTP "+r.status+" "+t.slice(0,220));
  state.sources+=5;save();render();
  return t;
 }catch(e){return "Web search failed: "+e.message}
 finally{clearTimeout(tm)}
}

async function callAi(prompt){
 const c=aiCfg();if(!c.enabled||!c.endpoint||!c.model)return null;
 const h={"Content-Type":"application/json"};if(c.key)h.Authorization="Bearer "+c.key;
 try{
  const r=await fetch(c.endpoint,{method:"POST",headers:h,body:JSON.stringify({model:c.model,messages:[{role:"system",content:"You are EvoBot's reasoning brain. Use supplied web evidence carefully, preserve useful source URLs, distinguish facts from uncertainty, and answer directly."},{role:"user",content:prompt}],temperature:.2})});
  if(!r.ok)throw new Error("HTTP "+r.status);
  const j=await r.json(),o=j&&j.choices&&j.choices[0]&&j.choices[0].message?j.choices[0].message.content:(j.output_text||j.response);
  if(!o)throw new Error("No recognizable text response");return String(o);
 }catch(e){return "AI connector error: "+e.message}
}

async function research(q){
 const material=await searchWeb(q);
 if(material.startsWith("LIVE SEARCH NEEDS")||material.startsWith("Web search failed:"))return material;
 const ai=await callAi("Research question: "+q+"\n\nWeb search material:\n\n"+material.slice(0,65000)+"\n\nProduce a factual answer with a short Sources section using the URLs present above.");
 if(ai&&!ai.startsWith("AI connector error:"))return ai;
 return "WEB RESEARCH MATERIAL\n\n"+material+"\n\nConnect the optional AI brain if you want EvoBot to synthesize these sources into a single answer.";
}

function calc(t){
 let m;if((m=t.match(/^\s*(-?\d+(?:\.\d+)?)\s*([+\-*\/])\s*(-?\d+(?:\.\d+)?)\s*$/))){
  const a=+m[1],b=+m[3],op=m[2];if(op==="+")return String(a+b);if(op==="-")return String(a-b);if(op==="*")return String(a*b);if(op==="/")return b===0?"Division by zero is undefined.":String(a/b)
 }
 if((m=t.match(/^(\d+(?:\.\d+)?)%\s+of\s+(-?\d+(?:\.\d+)?)$/i)))return String((+m[1]/100)*(+m[2]));
 return null
}

async function solve(task){
 task=norm(task);if(!task)return {text:"Enter a task.",via:"none"};let m,x;
 if((x=calc(task))!==null)return {text:x,via:"local-math"};
 if((m=task.match(/^remember\s+(.+?)\s+(?:is|=)\s+([\s\S]+)$/i))){state.memory[m[1].trim()]=m[2].trim();save();return {text:"Remembered.",via:"memory"}}
 if((m=task.match(/^recall\s+(.+)$/i))){const k=m[1].trim();return {text:Object.prototype.hasOwnProperty.call(state.memory,k)?String(state.memory[k]):"I do not have that memory.",via:"memory"}}
 if(/^list memory$/i.test(task))return {text:JSON.stringify(state.memory,null,2),via:"memory"};
 if((m=task.match(/^forget\s+(.+)$/i))){delete state.memory[m[1].trim()];save();return {text:"Forgotten.",via:"memory"}}
 if((m=task.match(/^(?:browse|read|fetch)\s+(https?:\/\/\S+)$/i)))return {text:await readUrl(m[1]),via:"web-reader"};
 if((m=task.match(/^(?:search(?: the)? web for|web search\s*:)\s*([\s\S]+)$/i)))return {text:await searchWeb(m[1]),via:"web-search"};
 if((m=task.match(/^(?:research|deep research|browse the web for)\s*:?\s*([\s\S]+)$/i)))return {text:await research(m[1]),via:"web-research"};
 if(/^https?:\/\//i.test(task))return {text:await readUrl(task),via:"web-reader"};
 const c=webCfg();
 if(c.enabled&&c.key&&state.autoWeb)return {text:await research(task),via:"auto-web-research"};
 const ai=await callAi(task);if(ai)return {text:ai,via:"external-ai"};
 state.failures.push({task:task,at:new Date().toISOString(),generation:state.generation});state.failures=state.failures.slice(-100);save();render();
 return {text:"I need internet search or an AI connector for this task. Enable Public web and add a search key, or give me a public URL to read.",via:"capability-gap"}
}

async function runTask(){
 const t=$("task").value;$("answer").textContent="Working…";
 const r=await solve(t);$("answer").textContent=r.text+"\n\n[via: "+r.via+"]";render()
}
function clearTask(){$("task").value="";$("answer").textContent="Ready."}
function copyAnswer(){navigator.clipboard&&navigator.clipboard.writeText($("answer").textContent)}
$("task").addEventListener("keydown",e=>{if(e.ctrlKey&&e.key==="Enter")runTask()});

function toggleWeb(on){
 $("webCfg").classList.toggle("hidden",!on);$("webOn").classList.toggle("active",on);$("webOff").classList.toggle("active",!on);
 const c=webCfg();c.enabled=on;sessionStorage.setItem(WKEY,JSON.stringify(c));render()
}
function saveWeb(){sessionStorage.setItem(WKEY,JSON.stringify({enabled:true,key:$("jinaKey").value}));toggleWeb(true);$("webTest").textContent="Saved for this browser session only."}
async function testWeb(){saveWeb();$("webTest").textContent="Testing…";const r=await searchWeb("OpenAI");$("webTest").textContent=r.startsWith("Web search failed:")||r.startsWith("LIVE SEARCH NEEDS")?r:"Connected. Live public-web search is working."}

function toggleAi(on){
 $("aiCfg").classList.toggle("hidden",!on);$("aiOn").classList.toggle("active",on);$("aiOff").classList.toggle("active",!on);
 const c=aiCfg();c.enabled=on;sessionStorage.setItem(AKEY,JSON.stringify(c))
}
function saveAi(){sessionStorage.setItem(AKEY,JSON.stringify({enabled:true,endpoint:norm($("aiEndpoint").value),model:norm($("aiModel").value),key:$("aiKey").value}));toggleAi(true);$("evolution").textContent="AI connector saved for this browser session only."}
async function testAi(){saveAi();$("evolution").textContent="Testing AI…";const r=await callAi("Reply with exactly CONNECTED");$("evolution").textContent=r||"AI is not configured."}

function observe(){$("evolution").textContent=JSON.stringify({generation:state.generation,auto_web:state.autoWeb,recent_failures:state.failures.slice(-10),memory_keys:Object.keys(state.memory)},null,2)}
function evolve(){
 const before=state.autoWeb;state.autoWeb=true;state.generation++;
 const h={at:new Date().toISOString(),generation:state.generation,change:"Prefer live web research for unknown tasks",reason:state.failures.length?"Observed capability gaps":"General research routing",promoted:true};
 state.history.unshift(h);state.history=state.history.slice(0,30);save();$("evolution").textContent=JSON.stringify(h,null,2);render()
}
function resetLearning(){state=baseState();save();$("evolution").textContent="Learned state reset.";render()}

const examples=["search web for latest ISRO news","research: latest AI developments","browse https://www.isro.gov.in/","compare current quantum-computing platforms","find official sources about India's latest space missions","17% of 850","remember project is Orion","recall project"];
function render(){
 const wc=webCfg();$("webStat").textContent=wc.enabled?(wc.key?"ON":"READ"):"OFF";$("webStat").className="value "+(wc.enabled?"status-good":"status-bad");
 $("sourceCount").textContent=state.sources;$("memoryCount").textContent=Object.keys(state.memory).length;$("failureCount").textContent=state.failures.length;
 $("memory").textContent=Object.keys(state.memory).length?JSON.stringify(state.memory,null,2):"No memory yet.";
 $("examples").innerHTML=examples.map(x=>'<span class="chip" data-x="'+encodeURIComponent(x)+'">'+x+"</span>").join("");
 document.querySelectorAll("[data-x]").forEach(el=>el.onclick=()=>{$("task").value=decodeURIComponent(el.dataset.x);runTask()});
 $("history").innerHTML=state.history.length?state.history.map(x=>'<div class="event"><b>Generation '+x.generation+'</b> · '+x.change+'<br><small>'+new Date(x.at).toLocaleString()+' · '+x.reason+"</small></div>").join(""):'<div class="sub">No evolution events yet.</div>';
}
(function init(){
 const w=webCfg();if(w.key)$("jinaKey").value=w.key;if(w.enabled)toggleWeb(true);
 const a=aiCfg();if(a.endpoint)$("aiEndpoint").value=a.endpoint;if(a.model)$("aiModel").value=a.model;if(a.enabled)toggleAi(true);
 render()
})();