# Configuration engagement operations

The public toolkit remains free under the unchanged LICENSE. The service at `/configuration.html` is a separately quoted configuration engagement, not a software subscription. No public price or agreement was invented. Generated public artwork, starter ZIP and canonical workspace/deal scripts are preserved.

## Required deployment configuration (not provisioned)

Use a Vercel Node deployment with root at this repository, `web` output, the included API route and `npm run build`. Existing estate services use this same Neon/Clerk/Stripe/private-Blob stack. Required values:

- `UNDERWRITER_SERVICE_ENABLED=true`
- `UNDERWRITER_PUBLIC_ORIGIN`: exact canonical HTTPS origin
- `UNDERWRITER_DATABASE_URL`: dedicated Neon database
- `CLERK_SECRET_KEY`, `CLERK_PUBLISHABLE_KEY`
- `UNDERWRITER_OPERATOR_CLERK_IDS`: explicit comma-separated operator user IDs
- `UNDERWRITER_STRIPE_SECRET_KEY`, `UNDERWRITER_STRIPE_WEBHOOK_SECRET`
- `UNDERWRITER_BLOB_READ_WRITE_TOKEN`: private Blob store

No environment file is loaded by these scripts. Run `npm run db:migrate` in the intended configured environment. Configure Clerk's app/origin and sign-in permissions. Configure the Stripe signed webhook at `/api/configuration/webhook` for Checkout completed/async success/failure/expired, charge refund and dispute created/closed events. No provider resource or configuration was created in this implementation.

## Customer and operator path

1. Customer signs in and submits actual firm identity, runtime, scope, constraints and acceptance criteria. Records persist by Clerk account. Inquiry idempotency prevents an identical browser retry from making another request. Five requests/account/day is a bounded service guard, not a global anti-abuse guarantee.
2. An allowlisted operator selects Operator view. They review private requests, record an internal handling note, and publish an actual USD amount, scope, acceptance criteria, terms and expiry. Terms must reflect the real engagement, including delivery and refund expectations; no terms are auto-filled.
3. Customer sees the exact quote revision and explicitly accepts before Stripe checkout. Server-side quote data sets the amount. Accepted quotes are frozen; neither a buyer-supplied price nor a browser return URL grants fulfillment.
4. Signed webhooks reconcile current Stripe state. Manual refresh and every download also reconcile. Refunds (including partial) and disputes block paid package download. A refund does not delete already downloaded files or revoke the free MIT license. Payment does not declare configuration completed.
5. Operator performs the actual configuration in an isolated workspace created with the canonical `scripts/create_workspace.py`. Review actual deliverables against the quote. Update `DELIVERY-MANIFEST.json` hashes for every changed file; do not merely rename a blank starter and claim completion.
6. Add `SERVICE-HANDOFF.json` containing the exact `engagementId`, accepted `quoteRevision`, requested `runtime`, `operatorReviewed: true`, a substantive `completedScope` string and `acceptanceEvidence` array describing real review evidence. These are operator assertions, not automated proof of customer acceptance. Do not include credentials.
7. Run `npm run deliver -- ENGAGEMENT_UUID REVIEWED_WORKSPACE`. The CLI checks canonical paid state, matching firm/runtime/revision, actual manifest bytes and required license/instructions. It packages only manifest-listed files plus the handoff, rejects symlinks, credential extensions/common key signatures and archives over 4 MB, uploads privately and attaches once to the still-paid order. Temporary staging is retained for review; the command prints its path. No emails are sent and no provider setup is inferred.
8. Customer downloads while paid, reviews against the agreed criteria, and explicitly accepts delivery. Customer acceptance is separate from operator delivery and payment.

Operator and customer records are separate views with server-enforced authorization. Internal notes, raw billing IDs and package storage paths are not exposed to customers. User input is rendered with textContent, not HTML. No signup gives operator authority.

## Limits and verification

Expired or abandoned accepted checkout sessions require operator reconciliation; the app intentionally does not issue another charge or silently replace accepted scope. Automated amendment/cancellation/refund workflows, email notifications, attachments, automated connector setup and customer-machine acceptance testing are not implemented. The operator handles unusual payment/quote recovery through the provider and an audited repair; no unsafe admin reset button is provided. The lease prevents routine duplicate processing but does not substitute for production concurrency testing. SQL mutations and separate audit event inserts are not one transaction, so an interruption can leave the state saved without its companion audit event. Core quote/acceptance/payment fields remain durable.

The Python packaging check cannot detect every possible embedded credential or establish the truth of operator acceptance evidence. Manual inspection and customer acceptance remain required. Private download streaming and Blob limits need verification on the target hosting plan. The 4 MB compressed archive limit is intentional.

One syntax check passed for the new JavaScript/Python sources. No database migration, provider request, payment, Blob upload, packaging delivery or browser flow was executed. No live URL exists from this work. I have NOT verified this in a browser. You should test before trusting me.

Implementation reference: [Stripe fulfillment](https://docs.stripe.com/checkout/fulfillment) and [Clerk JavaScript quickstart](https://clerk.com/docs/js-frontend/getting-started/quickstart).
