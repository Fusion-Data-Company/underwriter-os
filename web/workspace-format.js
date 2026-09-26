const uuid=/^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
function text(value,max,label,required=false){if(typeof value!=='string'||value.length>max||(required&&!value.trim()))throw Error(`Invalid ${label}.`);return value;}
function id(value){if(typeof value!=='string'||!uuid.test(value))throw Error('Invalid record identity.');return value;}
function stamp(value){if(typeof value!=='string'||value.length>40||!Number.isFinite(Date.parse(value)))throw Error('Invalid record timestamp.');return value;}
export function publicationDate(value){if(value==='')return '';if(typeof value!=='string'||!/^\d{4}-\d{2}-\d{2}$/.test(value)||!Number.isFinite(Date.parse(value))||new Date(value).toISOString().slice(0,10)!==value)throw Error('Enter a real publication date.');return value;}
export function sourceUrl(value){if(!value)return '';text(value,2000,'source URL');const url=new URL(value);if(!['http:','https:'].includes(url.protocol)||url.username||url.password)throw Error('Use an HTTP or HTTPS source URL without embedded credentials.');return url.href;}
export function dealRecord(value){
 if(!value||typeof value!=='object'||!Array.isArray(value.sources)||value.sources.length>200)throw Error('Invalid deal or source count.');
 const result={id:id(value.id),name:text(value.name,160,'deal name',true),address:text(value.address,400,'location',true),created:stamp(value.created),question:text(value.question||'',5000,'research question'),facts:text(value.facts||'',15000,'facts'),assumptions:text(value.assumptions||'',15000,'assumptions'),sources:value.sources.map(source=>{
  if(!source||typeof source!=='object')throw Error('Invalid source record.');
  const item={id:id(source.id),title:text(source.title,200,'source title',true),url:sourceUrl(source.url||''),published:publicationDate(source.published||''),recorded:stamp(source.recorded)};
  if(source.sha256!==undefined){if(typeof source.sha256!=='string'||! /^[a-f0-9]{64}$/.test(source.sha256)||!Number.isSafeInteger(source.bytes)||source.bytes<0||source.bytes>20*1024*1024)throw Error('Invalid file fingerprint.');Object.assign(item,{sha256:source.sha256,fileName:text(source.fileName,255,'file name',true),bytes:source.bytes});}return item;
 })};
 if(value.updated!==undefined)result.updated=stamp(value.updated);
 if(new Set(result.sources.map(s=>s.id)).size!==result.sources.length)throw Error('Duplicate source identities.');return result;
}
export function workspaceRecord(value){if(value?.version!==1||!Array.isArray(value.deals)||value.deals.length>100)throw Error('Invalid workspace format.');const deals=value.deals.map(dealRecord);if(new Set(deals.map(d=>d.id)).size!==deals.length)throw Error('Duplicate deal identities.');return{version:1,deals};}
