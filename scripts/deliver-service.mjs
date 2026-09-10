/** Operator CLI: publish a reviewed workspace only for an existing paid engagement. */
import {mkdtemp,writeFile,readFile} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join,resolve} from 'node:path';
import {execFileSync} from 'node:child_process';
import {randomUUID} from 'node:crypto';
import {put,del} from '@vercel/blob';
import {config,reconcile} from '../server/configuration.mjs';
const [id,workspace]=process.argv.slice(2);
if(!id||!workspace)throw new Error('Usage: npm run deliver -- ENGAGEMENT_UUID REVIEWED_WORKSPACE');
const token=process.env.UNDERWRITER_BLOB_READ_WRITE_TOKEN;if(!token)throw new Error('Private Blob configuration required');
const r=await reconcile(id);if(r.payment_status!=='paid'||r.package_path||!r.accepted_revision)throw new Error('An undelivered paid accepted engagement is required');
const staging=await mkdtemp(join(tmpdir(),'underwriter-delivery-'));await writeFile(join(staging,'order.json'),JSON.stringify(r),{mode:0o600});
const archive=join(staging,'package.zip');const result=JSON.parse(execFileSync('python3',[resolve('scripts/package_service.py'),'--workspace',resolve(workspace),'--order',join(staging,'order.json'),'--output',archive],{encoding:'utf8'}));
await reconcile(id);
const blob=await put(`underwriter/${id}/${randomUUID()}.zip`,await readFile(archive),{access:'private',token,addRandomSuffix:false,contentType:'application/zip'});
const {db}=config();try{const rows=await db`UPDATE uw_engagements SET package_path=${blob.pathname},package_sha256=${result.sha256},package_bytes=${result.bytes},delivery_note=${result.deliveryNote},delivered_at=now(),stage='delivered',updated_at=now() WHERE id=${id}::uuid AND payment_status='paid' AND package_path IS NULL AND accepted_revision=${r.accepted_revision} RETURNING id`;if(!rows[0])throw new Error('Engagement changed before attachment');}catch(e){await del(blob.pathname,{token});throw e;}
await db`INSERT INTO uw_service_events(engagement_id,actor,action,detail) VALUES(${id}::uuid,'operator-cli','package_delivered',${JSON.stringify(result)}::jsonb)`;
console.log(JSON.stringify({engagementId:id,sha256:result.sha256,bytes:result.bytes,staging,customerAcceptanceVerified:false,sent:false}));
