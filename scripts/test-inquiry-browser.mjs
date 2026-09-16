import {createRequire} from 'node:module';
import {readFile,mkdir} from 'node:fs/promises';
import assert from 'node:assert/strict';
const require=createRequire(process.env.PLAYWRIGHT_PACKAGE||new URL('../package.json',import.meta.url));
const {chromium}=require('playwright');const browser=await chromium.launch({headless:true});
await mkdir('verification',{recursive:true});
try {
 for(const scenario of ['success','retry','refresh-failure','validation','html-error']) {
  const page=await browser.newPage({viewport:{width:390,height:844}});let posts=[],records=[],listCalls=0;
  await page.addInitScript(()=>{window.Clerk={user:{id:'fixture'},session:{getToken:async()=>'fixture'},load:async()=>{},mountUserButton:()=>{}}});
  if(!process.env.TEST_LIVE_ASSETS) await page.route('**/configuration.html',async r=>r.fulfill({contentType:'text/html',body:await readFile('web/configuration.html','utf8')}));
  if(!process.env.TEST_LIVE_ASSETS) await page.route('**/configuration.js',async r=>r.fulfill({contentType:'text/javascript',body:await readFile('web/configuration.js','utf8')}));
  await page.route('https://clerk.example.test/**',r=>r.fulfill({body:'',contentType:'text/javascript'}));
  await page.route('**/api/configuration/**',route=>{const action=new URL(route.request().url()).pathname.split('/').pop();
   if(action==='config')return route.fulfill({json:{publishableKey:'pk_test_'+Buffer.from('clerk.example.test$').toString('base64')}});
   if(action==='inquiry'){
    const request=route.request().postDataJSON();posts.push(request);
    if(scenario==='html-error')return route.fulfill({status:502,contentType:'text/html',body:'<html>Unavailable</html>'});
    if(scenario==='validation')return route.fulfill({status:400,json:{error:'Invalid or incomplete request fields',fields:{scope:['Provide at least 20 characters.']}}});
    if(!records.length)records.push({id:request.id,request,stage:'new',paymentStatus:'unpaid'});
    if(scenario==='retry'&&posts.length===1)return route.fulfill({status:503,json:{error:'Temporary connection failure'}});
    return route.fulfill({status:201,json:records[0]});
   }
   listCalls++;if(scenario==='refresh-failure'&&listCalls>1)return route.fulfill({status:503,json:{error:'List unavailable'}});
   return route.fulfill({json:{operator:false,engagements:records}});
  });
  await page.goto('https://underwriter.fusiondataco.com/configuration.html');await page.locator('#workspace').waitFor({state:'visible'});
  for(const [name,value] of Object.entries({firm:'Fictional fixture',contactEmail:'fixture@example.test',scope:'Configure isolated workflow for demonstration.',acceptanceCriteria:'Validate isolated fixture request is persisted.'}))await page.locator(`[name="${name}"]`).fill(value);
  await page.locator('[name="consent"]').check();await page.getByRole('button',{name:'Submit inquiry'}).click();
  await page.waitForFunction(()=>{const s=document.querySelector('#request-status').textContent;return s&&!s.includes('Submitting');});
  if(scenario==='retry'){
   assert.equal(await page.locator('[name=firm]').inputValue(),'Fictional fixture');await page.getByRole('button',{name:'Submit inquiry'}).click();await page.waitForFunction(()=>document.querySelector('#request-status').textContent.includes('Inquiry saved'));
   assert.equal(posts.length,2);assert.equal(posts[0].id,posts[1].id);assert.equal(records.length,1);
  }
  const status=await page.locator('#request-status').innerText();assert.ok(!status.includes('Unexpected token'));
  if(['success','retry','refresh-failure'].includes(scenario)){
   assert.ok(status.includes(posts[0].id));assert.ok(status.includes('Inquiry saved'));assert.equal(await page.locator('[name=firm]').inputValue(),'');
   if(scenario==='refresh-failure')assert.ok(status.includes('Do not submit another inquiry'));
   else {await page.reload();await page.locator('#workspace').waitFor({state:'visible'});await page.waitForFunction(()=>document.querySelector('#engagements').textContent.includes('Fictional fixture'));assert.ok((await page.locator('#engagements').innerText()).includes(posts[0].id));}
  } else {assert.equal(await page.locator('[name=firm]').inputValue(),'Fictional fixture');assert.equal(await page.locator('#request-status').getAttribute('role'),'alert');}
  if(scenario==='validation')assert.equal(await page.locator('[name=scope]').evaluate(e=>e.validationMessage),'Provide at least 20 characters.');
  if(scenario==='refresh-failure'){const rect=await page.locator('#request-status').boundingBox();assert.ok(rect.y>=0&&rect.y<844);await page.screenshot({path:'verification/inquiry-saved-mobile.png'});}
  console.log(`PASS ${scenario}: ${status}`);await page.close();
 }
}finally{await browser.close();}
