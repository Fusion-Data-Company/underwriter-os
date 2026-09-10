import {neon} from '@neondatabase/serverless';
import {statements} from '../server/service-schema.mjs';
if(!process.env.UNDERWRITER_DATABASE_URL)throw new Error('UNDERWRITER_DATABASE_URL required; no migration executed');
const db=neon(process.env.UNDERWRITER_DATABASE_URL);await db.transaction(statements.map(s=>db.query(s)));console.log('Configuration service migration completed');
