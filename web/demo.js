const KEY='fusion-underwriter-demo-v1';
const $=selector=>document.querySelector(selector);
const message=text=>{$('#status').textContent=text;};
let state={version:1,deals:[]},active='';
try{const stored=JSON.parse(localStorage.getItem(KEY)||'null');if(stored?.version===1&&Array.isArray(stored.deals))state=stored;}catch{message('Previous browser storage could not be loaded. You can create a new workspace.');}
function save(){try{localStorage.setItem(KEY,JSON.stringify(state));return true;}catch{message('Browser storage is unavailable. Your work remains in this tab; export it before closing.');return false;}}
function current(){return state.deals.find(deal=>deal.id===active);}
function render(){
 const select=$('#deals');select.replaceChildren();
 for(const deal of state.deals){const option=document.createElement('option');option.value=deal.id;option.textContent=deal.name;select.append(option);}
 select.value=active;const deal=current();$('#workspace').hidden=!deal;if(!deal)return;
 $('#deal-title').textContent=deal.name;$('#deal-address').textContent=deal.address;
 for(const field of ['question','facts','assumptions'])$('#memo').elements[field].value=deal[field]||'';
 const sources=$('#sources');sources.replaceChildren();
 for(const source of deal.sources){const article=document.createElement('article');article.className='source';const heading=document.createElement('h4');heading.textContent=source.title;article.append(heading);
  const detail=document.createElement('p');detail.textContent=`Published: ${source.published||'not supplied'} | Recorded: ${source.recorded}`;article.append(detail);
  if(source.url){const link=document.createElement('a');link.href=source.url;link.textContent=source.url;link.target='_blank';link.rel='noopener noreferrer';article.append(link);}
  if(source.sha256){const hash=document.createElement('p');hash.textContent=`${source.fileName} (${source.bytes} bytes) | SHA-256: ${source.sha256}`;article.append(hash);}sources.append(article);
 }
}
$('#new-deal').addEventListener('submit',event=>{event.preventDefault();const form=event.currentTarget;const name=form.elements.name.value.trim(),address=form.elements.address.value.trim();if(!name||!address)return;
 if(state.deals.length>=100){message('This browser demo supports 100 deals. Export your work and use the local toolkit for larger collections.');return;}
 const deal={id:crypto.randomUUID(),name,address,created:new Date().toISOString(),question:'',facts:'',assumptions:'',sources:[]};state.deals.push(deal);active=deal.id;const saved=save();render();form.reset();if(saved)message('Deal workspace created and saved in this browser.');});
$('#deals').addEventListener('change',event=>{active=event.target.value;render();});
function saveNotes(){const deal=current();if(!deal)return;for(const field of ['question','facts','assumptions'])deal[field]=$('#memo').elements[field].value.trim();deal.updated=new Date().toISOString();return save();}
$('#memo').addEventListener('submit',event=>{event.preventDefault();if(saveNotes())message('Research notes saved.');});
$('#source').addEventListener('submit',async event=>{
 event.preventDefault();const deal=current();if(!deal)return;const form=event.currentTarget,button=form.querySelector('button');button.disabled=true;
 try{if(deal.sources.length>=200)throw Error('This demo supports 200 sources per deal. Export the workspace to continue locally.');const file=form.elements.file.files[0],rawUrl=form.elements.url.value.trim();let url='';if(rawUrl){const parsed=new URL(rawUrl);if(!['https:','http:'].includes(parsed.protocol))throw Error('Use an HTTP or HTTPS source URL.');url=parsed.href;}
  const source={id:crypto.randomUUID(),title:form.elements.title.value.trim(),url,published:form.elements.published.value,recorded:new Date().toISOString()};if(!source.title)throw Error('Enter a source title.');
  if(file){if(file.size>20*1024*1024)throw Error('Choose a file smaller than 20 MB.');const digest=await crypto.subtle.digest('SHA-256',await file.arrayBuffer());source.sha256=Array.from(new Uint8Array(digest),n=>n.toString(16).padStart(2,'0')).join('');source.fileName=file.name;source.bytes=file.size;if(deal.sources.some(s=>s.sha256===source.sha256))throw Error('These exact file bytes already have a source record in this deal.');}
  deal.sources.push(source);const saved=save();saveNotes();render();form.reset();if(saved)message('Source record saved. This records provenance, not verification of the source claims.');
 }catch(error){message(error instanceof Error?error.message:'Source could not be recorded.');}finally{button.disabled=false;}
});
function download(name,text,type){const url=URL.createObjectURL(new Blob([text],{type}));const link=document.createElement('a');link.href=url;link.download=name;link.click();setTimeout(()=>URL.revokeObjectURL(url),1000);}
$('#export-workspace').addEventListener('click',()=>{saveNotes();const deal=current();if(deal)download(`deal-${deal.id}.json`,JSON.stringify({version:1,kind:'underwriter-browser-workspace',deal},null,2),'application/json');});
$('#export-memo').addEventListener('click',()=>{saveNotes();const deal=current();if(!deal)return;const text=`# ${deal.name}\n\nLocation: ${deal.address}\n\n## Research question\n${deal.question||'Not supplied'}\n\n## Known facts (author supplied; not independently verified)\n${deal.facts||'Not supplied'}\n\n## Assumptions and open questions\n${deal.assumptions||'Not supplied'}\n\n## Source records\n${deal.sources.map((s,i)=>`${i+1}. ${s.title}\n   URL: ${s.url||'Not supplied'}\n   Published: ${s.published||'Not supplied'}\n   Recorded: ${s.recorded}\n   File: ${s.fileName||'None'}\n   SHA-256: ${s.sha256||'No file fingerprint'}`).join('\n\n')}\n\nExported from Underwriter OS browser demo. Original source files are not included.\n`;download(`deal-${deal.id}.md`,text,'text/markdown');});
active=state.deals[0]?.id||'';render();
