const $ = id => document.getElementById(id);
const LOCAL_KEY = 'evobot.chat.v6';
const SETTINGS_KEY = 'evobot.session.v6';
const REMOTE_STATE = 'https://raw.githubusercontent.com/EduChronical/my-second-website/main/evobot/state.json';
const READER = 'https://r.jina.ai/';
const SEARCH = 'https://s.jina.ai/?q=';

let local = loadLocal();
let remote = null;
let busy = false;

function loadLocal(){
  try { return Object.assign({messages:[],memory:{},failures:[],learning:true,web:true,localCycles:0,lastLocalCycle:null}, JSON.parse(localStorage.getItem(LOCAL_KEY)||'{}')); }
  catch { return {messages:[],memory:{},failures:[],learning:true,web:true,localCycles:0,lastLocalCycle:null}; }
}
function saveLocal(){ localStorage.setItem(LOCAL_KEY, JSON.stringify(local)); }
function settings(){ try{return JSON.parse(sessionStorage.getItem(SETTINGS_KEY)||'{}')}catch{return {}} }
function saveSettings(x){ sessionStorage.setItem(SETTINGS_KEY, JSON.stringify(x)); }
function esc(s){ return String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function now(){ return new Date().toISOString(); }
function toast(msg){ const t=$('toast'); t.textContent=msg; t.classList.add('show'); setTimeout(()=>t.classList.remove('show'),1800); }
const STOP=new Set(['the','and','for','with','that','this','from','into','your','you','are','was','were','have','has','had','but','not','can','will','would','about','what','when','where','which','their','there','than','then','them','they','its','our','out','all','also','more','most','how','why','who','an','of','to','in','on','at','is','it','as','be','or','by']);
function tokens(text){ return (String(text).toLowerCase().match(/[a-z0-9][a-z0-9_-]{2,}/g)||[]).filter(x=>!STOP.has(x)); }

function addMessage(role,text,meta='',sources=[]){
  local.messages.push({role,text,meta,sources,at:now()});
  local.messages=local.messages.slice(-80); saveLocal(); renderMessages();
}
function shortUrl(u){ try{const x=new URL(u);return x.hostname+x.pathname.slice(0,42)}catch{return u.slice(0,52)} }
function renderMessages(){
  const box=$('messages');
  $('empty').style.display=local.messages.length?'none':'grid';
  box.innerHTML=local.messages.map(m=>{
    const srcList=[...new Set(m.sources||[])].slice(0,8);
    const src=srcList.length?'<details class="sourcebox"><summary>Sources · '+srcList.length+'</summary><div class="source-list">'+srcList.map(u=>'<a class="source" href="'+esc(u)+'" target="_blank" rel="noopener noreferrer">'+esc(shortUrl(u))+'</a>').join('')+'</div></details>':'';
    return '<div class="msg"><div class="avatar '+(m.role==='user'?'user':'bot')+'">'+(m.role==='user'?'You':'E')+'</div><div class="bubble '+(m.role==='user'?'user':'bot')+'">'+esc(m.text)+(m.meta&&/error|failure|required/i.test(m.meta)?'<div class="meta">'+esc(m.meta)+'</div>':'')+(src||'')+'</div></div>';
  }).join('');
  setTimeout(()=>window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'}),20);
}

function openDrawer(){ $('overlay').classList.add('show'); refreshDrawer(); }
function closeDrawer(){ $('overlay').classList.remove('show'); }
window.openDrawer=openDrawer; window.closeDrawer=closeDrawer;
function toggleLearning(){ local.learning=!local.learning; saveLocal(); refreshDrawer(); toast(local.learning?'Continuous learning on':'Continuous learning paused'); }
function toggleWeb(){ local.web=!local.web; saveLocal(); refreshDrawer(); toast(local.web?'Public web on':'Public web off'); }
window.toggleLearning=toggleLearning; window.toggleWeb=toggleWeb;
function saveJina(){ const s=settings(); s.jinaKey=$('jinaKey').value.trim(); saveSettings(s); toast('Web key saved for this tab'); }
window.saveJina=saveJina;
function saveAI(){ const s=settings(); s.aiEndpoint=$('aiEndpoint').value.trim(); s.aiModel=$('aiModel').value.trim(); s.aiKey=$('aiKey').value; saveSettings(s); toast('AI connector saved for this tab'); }
window.saveAI=saveAI;
async function testWeb(){ toast('Testing web…'); try{const t=await webSearch('ISRO'); toast(t.text.length>80?'Web connected':'Web returned little data')}catch(e){toast('Web test failed')} }
window.testWeb=testWeb;
async function testAI(){ toast('Testing AI…'); try{const r=await callAI('Reply with exactly CONNECTED', ''); toast(String(r).includes('CONNECTED')?'AI connected':'AI response received')}catch(e){toast('AI test failed')} }
window.testAI=testAI;
function newChat(){ local.messages=[]; saveLocal(); renderMessages(); closeDrawer(); }
window.newChat=newChat;

async function refreshRemote(){
  try{
    const r=await fetch(REMOTE_STATE+'?t='+Date.now(),{cache:'no-store'});
    if(!r.ok) throw new Error('HTTP '+r.status);
    remote=await r.json();
    updateStatus(); refreshDrawer();
  }catch(e){ updateStatus(true); }
}
function updateStatus(failed=false){
  const el=$('statusText');
  if(failed){el.textContent='learner reconnecting';return;}
  if(!remote||!remote.last_run){el.textContent='learner starting';return;}
  const age=(Date.now()-Date.parse(remote.last_run))/60000;
  el.textContent=age<20?'24/7 learner online':'learner delayed';
}
function refreshDrawer(){
  $('learnToggle').classList.toggle('on',!!local.learning);
  $('webToggle').classList.toggle('on',!!local.web);
  const s=settings();
  if(document.activeElement!==$('jinaKey')) $('jinaKey').value=s.jinaKey||'';
  if(document.activeElement!==$('aiEndpoint')) $('aiEndpoint').value=s.aiEndpoint||'';
  if(document.activeElement!==$('aiModel')) $('aiModel').value=s.aiModel||'';
  if(document.activeElement!==$('aiKey')) $('aiKey').value=s.aiKey||'';
  $('coreVersion').textContent='v'+(remote?.core_version||1);
  $('knowledgeCount').textContent=remote?.pages_learned||0;
  $('failureCount').textContent=(remote?.failures||[]).length+(local.failures||[]).length;
  $('sourceCount').textContent=remote?.metrics?.successful_fetches||0;
  $('lastCycle').textContent=remote?.last_run?new Date(remote.last_run).toLocaleString():'starting…';
  const events=(remote?.events||[]).slice(0,12);
  $('activity').innerHTML=events.length?events.map(e=>'<div class="event"><b>'+esc(e.kind||'event')+'</b><br>'+esc(e.message||'')+'<br><small>'+esc(e.at||'')+'</small></div>').join(''):'<div class="small">Background learner is starting.</div>';
}

function searchRemoteMemory(query,limit=6){
  if(!remote||!Array.isArray(remote.memory)) return [];
  const q=tokens(query), qset=new Set(q);
  return remote.memory.map(m=>{
    const hay=(String(m.title||'')+' '+String(m.summary||'')+' '+(m.keywords||[]).join(' ')).toLowerCase();
    let score=0; for(const t of qset){ if(hay.includes(t)) score+=2; if((m.keywords||[]).includes(t)) score+=2; }
    return {score,m};
  }).filter(x=>x.score>0).sort((a,b)=>b.score-a.score).slice(0,limit).map(x=>x.m);
}
function memoryContext(query){
  const ms=searchRemoteMemory(query,6);
  if(!ms.length) return {text:'',sources:[]};
  const text=ms.map((m,i)=>'[Memory '+(i+1)+'] '+m.title+'\n'+m.summary+'\nSource: '+m.url).join('\n\n');
  return {text,sources:ms.map(m=>m.url).filter(Boolean)};
}

async function readUrl(url){
  const u=new URL(url); if(!/^https?:$/.test(u.protocol)) throw new Error('Only public http/https URLs are supported');
  const r=await fetch(READER+url,{headers:{Accept:'text/plain'}});
  const t=await r.text(); if(!r.ok) throw new Error('Reader HTTP '+r.status);
  return {text:t.slice(0,60000),sources:[url]};
}
function extractUrls(text){
  const re=/https?:\/\/[^\s)\]}>"']+/g; const out=[]; const seen=new Set();
  for(const m of String(text).match(re)||[]){ const u=m.replace(/[.,;]+$/,''); if(!seen.has(u)){seen.add(u);out.push(u)} }
  return out.slice(0,24);
}
async function webSearch(query){
  const s=settings();
  if(s.jinaKey){
    const r=await fetch(SEARCH+encodeURIComponent(query),{headers:{Accept:'text/plain',Authorization:'Bearer '+s.jinaKey}});
    const t=await r.text(); if(!r.ok) throw new Error('Search HTTP '+r.status);
    return {text:t.slice(0,70000),sources:extractUrls(t)};
  }
  throw new Error('Live search currently needs a Jina key; background learned memory is still available.');
}

async function callNativeAI(prompt,context){
  try{
    if(window.LanguageModel&&typeof window.LanguageModel.create==='function'){
      const session=await window.LanguageModel.create(); return await session.prompt((context?context+'\n\n':'')+prompt);
    }
    if(window.ai?.languageModel?.create){
      const session=await window.ai.languageModel.create(); return await session.prompt((context?context+'\n\n':'')+prompt);
    }
  }catch(e){}
  return null;
}
async function callAI(prompt,context){
  const native=await callNativeAI(prompt,context); if(native) return native;
  const s=settings(); if(!s.aiEndpoint||!s.aiModel) return null;
  const headers={'Content-Type':'application/json'}; if(s.aiKey) headers.Authorization='Bearer '+s.aiKey;
  const r=await fetch(s.aiEndpoint,{method:'POST',headers,body:JSON.stringify({model:s.aiModel,temperature:.2,messages:[{role:'system',content:'You are EvoBot, a polished general-purpose conversational assistant. Give a direct, coherent, well-structured answer comparable in presentation quality to leading AI assistants. Use supplied evidence when relevant, distinguish established facts from uncertainty, never expose raw search markup, crawler logs, query strings, URL-encoded text, internal routing notes, or unprocessed snippets. Use concise Markdown and natural prose. Do not fabricate facts or citations.'},{role:'user',content:(context?context+'\n\n':'')+prompt}]})});
  if(!r.ok) throw new Error('AI HTTP '+r.status);
  const j=await r.json(); return j?.choices?.[0]?.message?.content||j?.output_text||j?.response||null;
}

function localMath(q){
  const m=String(q).trim().match(/^(-?\d+(?:\.\d+)?)\s*([+\-*\/])\s*(-?\d+(?:\.\d+)?)$/); if(!m)return null;
  const a=+m[1],b=+m[3],op=m[2]; if(op==='+')return String(a+b); if(op==='-')return String(a-b); if(op==='*')return String(a*b); if(op==='/')return b===0?'Division by zero is undefined.':String(a/b);
}
function maybeMemoryCommand(q){
  let m;
  if((m=q.match(/^remember\s+(.+?)\s+(?:is|=)\s+([\s\S]+)$/i))){local.memory[m[1].trim()]=m[2].trim();saveLocal();return 'Remembered.'}
  if((m=q.match(/^recall\s+(.+)$/i))){return Object.prototype.hasOwnProperty.call(local.memory,m[1].trim())?String(local.memory[m[1].trim()]):'I do not have that local memory yet.'}
  return null;
}
async function solve(q){
  const math=localMath(q); if(math!==null) return {text:math,meta:'local reasoning',sources:[]};
  const memcmd=maybeMemoryCommand(q); if(memcmd!==null) return {text:memcmd,meta:'persistent local memory',sources:[]};
  const direct=q.trim().match(/https?:\/\/\S+/);
  let gathered={text:'',sources:[]};
  const learned=memoryContext(q);
  if(direct){
    try{gathered=await readUrl(direct[0]);}catch(e){gathered={text:'',sources:[]};}
  } else if(local.web){
    try{gathered=await webSearch(q);}catch(e){gathered={text:'',sources:[]};}
  }
  const combined=[learned.text,gathered.text].filter(Boolean).join('\n\n--- LIVE / LEARNED EVIDENCE ---\n\n').slice(0,65000);
  const sources=[...new Set([...(learned.sources||[]),...(gathered.sources||[])])].slice(0,12);
  try{
    const ai=await callAI(q,combined);
    if(ai) return {text:String(ai),meta:'core v'+(remote?.core_version||1)+' · web+memory synthesis',sources};
  }catch(e){ local.failures.push({at:now(),task:q,error:String(e)});local.failures=local.failures.slice(-100);saveLocal(); }
  if(combined){
    return {
      text:'I found relevant source material, but this browser does not currently have a general reasoning model connected. I will not dump raw search text or encoded URLs into the chat. Connect a reasoning model in Settings for a coherent ChatGPT-style answer.',
      meta:'reasoning model required',
      sources
    };
  }
  local.failures.push({at:now(),task:q,error:'no reasoning backend and no retrieved evidence'}); local.failures=local.failures.slice(-100); saveLocal();
  return {text:'The 24/7 learner is running, but this browser still needs either retrievable web evidence or a reasoning model for this open-ended question. I recorded this as a capability gap for future evolution.',meta:'capability gap recorded',sources:[]};
}
async function submit(){
  if(busy)return; const q=$('prompt').value.trim(); if(!q)return;
  busy=true; $('send').disabled=true; $('prompt').value=''; resizePrompt(); addMessage('user',q);
  const id='typing-'+Date.now(); $('messages').insertAdjacentHTML('beforeend','<div id="'+id+'" class="msg"><div class="avatar bot">E</div><div class="bubble bot typing">Thinking…</div></div>'); window.scrollTo({top:document.body.scrollHeight,behavior:'smooth'});
  try{ const r=await solve(q); document.getElementById(id)?.remove(); addMessage('bot',r.text,r.meta,r.sources); }
  catch(e){ document.getElementById(id)?.remove(); local.failures.push({at:now(),task:q,error:String(e)}); saveLocal(); addMessage('bot','I hit an error while handling that request: '+e.message,'failure recorded'); }
  finally{busy=false;$('send').disabled=false;$('prompt').focus();refreshDrawer();}
}
function resizePrompt(){const el=$('prompt');el.style.height='auto';el.style.height=Math.min(el.scrollHeight,180)+'px';}
$('prompt').addEventListener('input',resizePrompt);
$('prompt').addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();submit()}});
$('send').addEventListener('click',submit);
document.querySelectorAll('.suggestion').forEach(b=>b.addEventListener('click',()=>{$('prompt').value=b.dataset.prompt;resizePrompt();submit()}));

async function runLearningCycle(manual=false){
  if(!local.learning&&!manual)return;
  const recent=local.messages.slice(-12).map(x=>x.text).join(' ');
  for(const t of tokens(recent).slice(0,20)) local.memory['topic:'+t]=(local.memory['topic:'+t]||0)+1;
  local.localCycles=(local.localCycles||0)+1; local.lastLocalCycle=now(); saveLocal();
  await refreshRemote(); if(manual)toast('Learning state refreshed');
}
window.runLearningCycle=runLearningCycle;
setInterval(()=>runLearningCycle(false),60000);

function boot(){
  renderMessages(); refreshDrawer(); refreshRemote();
  setInterval(refreshRemote,60000);
  setTimeout(()=>runLearningCycle(false),15000);
  $('prompt').focus();
}
boot();
