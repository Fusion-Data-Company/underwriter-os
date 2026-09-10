export const statements=[`CREATE TABLE IF NOT EXISTS uw_engagements (
 id uuid PRIMARY KEY, buyer text NOT NULL, request jsonb NOT NULL, request_hash text NOT NULL,
 stage text NOT NULL DEFAULT 'new', operator_note text NOT NULL DEFAULT '', quote jsonb, quote_revision integer NOT NULL DEFAULT 0,
 accepted_revision integer, accepted_at timestamptz, checkout_id text UNIQUE,payment_intent text UNIQUE,payment_status text NOT NULL DEFAULT 'unpaid',
 lease uuid,lease_until timestamptz,package_path text,package_sha256 text,package_bytes integer,delivery_note text,delivered_at timestamptz,customer_accepted_at timestamptz,
 created_at timestamptz NOT NULL DEFAULT now(),updated_at timestamptz NOT NULL DEFAULT now())`,
 `CREATE TABLE IF NOT EXISTS uw_service_events(id uuid PRIMARY KEY DEFAULT gen_random_uuid(),engagement_id uuid NOT NULL REFERENCES uw_engagements(id),actor text NOT NULL,action text NOT NULL,detail jsonb NOT NULL DEFAULT '{}',created_at timestamptz NOT NULL DEFAULT now())`,
 `CREATE TABLE IF NOT EXISTS uw_stripe_events(id text PRIMARY KEY,engagement_id uuid NOT NULL REFERENCES uw_engagements(id),received_at timestamptz NOT NULL DEFAULT now())`,
 `CREATE INDEX IF NOT EXISTS uw_buyer_requests ON uw_engagements(buyer,created_at DESC)`];
