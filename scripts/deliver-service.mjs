/** Operator CLI: attach exact reviewed bytes, preserving ambiguous uploads for recovery. */
import {mkdtemp,writeFile,readFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join,resolve} from 'node:path';
import {execFileSync} from 'node:child_process';
import {createHash} from 'node:crypto';
import {put,get} from '@vercel/blob';
import {config,reconcile} from '../server/configuration.mjs';
const [id,workspace]=process.argv.slice(2);
if(!id||!workspace)throw new Error('Usage: npm run deliver -- ENGAGEMENT_UUID REVIEWED_WORKSPACE');
const token=process.env.UNDERWRITER_BLOB_READ_WRITE_TOKEN;if(!token)throw new Error('Private Blob configuration required');
const r=await reconcile(id);if(r.payment_status!=='paid'||!r.accepted_revision)throw new Error('A paid accepted engagement is required');
const staging=await mkdtemp(join(tmpdir(),'underwriter-delivery-'));await writeFile(join(staging,'order.json'),JSON.stringify(r),{mode:0o600});
const archive=join(staging,'package.zip');const result=JSON.parse(execFileSync('python3',[resolve('scripts/package_service.py'),'--workspace',resolve(workspace),'--order',join(staging,'order.json'),'--output',archive],{encoding:'utf8'}));
const bytes=await readFile(archive);
if(bytes.length!==result.bytes||createHash('sha256').update(bytes).digest('hex')!==result.sha256)throw new Error('Prepared package identity mismatch');
const pathname=`underwriter/${id}/${result.sha256}.zip`;
if(r.package_path&&(r.package_path!==pathname||r.package_sha256!==result.sha256||r.package_bytes!==result.bytes))throw new Error('A different delivery is already attached; do not replace accepted work');
async function remoteMatches(){const blob=await get(pathname,{access:'private',token,useCache:false});if(!blob?.stream)return false;const reader=blob.stream.getReader(),hash=createHash('sha256');let size=0;try{for(;;){const {done,value}=await reader.read();if(done)break;size+=value.byteLength;if(size>result.bytes){await reader.cancel();return false;}hash.update(value);}}finally{reader.releaseLock();}return size===result.bytes&&hash.digest('hex')===result.sha256;}
if(!await remoteMatches()){
 try{await put(pathname,bytes,{access:'private',token,addRandomSuffix:false,allowOverwrite:false,contentType:'application/zip'});}catch(error){if(!await remoteMatches())throw error;}
}
if(!await remoteMatches())throw new Error('Uploaded package bytes could not be confirmed; retained for operator recovery');
const fresh=await reconcile(id);
if(fresh.payment_status!=='paid'||fresh.buyer!==r.buyer||fresh.accepted_revision!==r.accepted_revision)throw new Error('Engagement changed. Uploaded bytes retained; no delivery attached');
const {db}=config();
const attached=await db`WITH updated AS (UPDATE uw_engagements SET package_path=${pathname},package_sha256=${result.sha256},package_bytes=${result.bytes},delivery_note=${result.deliveryNote},delivered_at=now(),stage='delivered',updated_at=now() WHERE id=${id}::uuid AND buyer=${r.buyer} AND payment_status='paid' AND package_path IS NULL AND accepted_revision=${r.accepted_revision} RETURNING id), logged AS (INSERT INTO uw_service_events(engagement_id,actor,action,detail) SELECT id,'operator-cli','package_delivered',${JSON.stringify(result)}::jsonb FROM updated RETURNING engagement_id) SELECT engagement_id AS id FROM logged`;
if(!attached.length){const [existing]=await db`SELECT id FROM uw_engagements WHERE id=${id}::uuid AND buyer=${r.buyer} AND payment_status='paid' AND accepted_revision=${r.accepted_revision} AND package_path=${pathname} AND package_sha256=${result.sha256} AND package_bytes=${result.bytes}`;if(!existing)throw new Error('Attachment unconfirmed. Upload retained; rerun the same reviewed workspace to recover');}
console.log(JSON.stringify({engagementId:id,sha256:result.sha256,bytes:result.bytes,staging,customerAcceptanceVerified:false,sent:false}));
