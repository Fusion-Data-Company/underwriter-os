import {execFileSync} from 'node:child_process';
for(const file of ['server/configuration.mjs','server/service-schema.mjs','api/configuration/[action].js','web/configuration.js','scripts/deliver-service.mjs','scripts/migrate-service.mjs'])execFileSync(process.execPath,['--check',file],{stdio:'inherit'});
execFileSync('python3',['-c',"import ast,pathlib; ast.parse(pathlib.Path('scripts/package_service.py').read_text())"],{stdio:'inherit'});
console.log('Configuration service JavaScript and Python syntax checks passed');
