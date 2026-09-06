# Security

## What's in this public repo
- **Code, skills, templates, and docs — no secrets, ever.** This repo ships with zero API keys, zero credentials, and zero baked-in access of any kind.
- **No plaintext keys, no `.env`, no client data, no per-user `CLAUDE.md`/memory** — `.gitignore` blocks them, and nothing of the kind is ever committed here.
- Every team that installs Underwriter OS brings its **own** keys (research connectors, data providers, voice) and stores them only on its own machines, in its own `config/.env` or its own connector logins. Nothing flows through this repository.

## Per-user data
Each person's `CLAUDE.md`, `underwriter-os/memory/`, and any deal files live **only on their own machine**, never in this repo.

## Rotating keys
There is nothing here to rotate — this repo has no keys. If your firm's own keys (stored locally, in your own vault, or in your connector settings) are ever compromised, rotate them at the provider as you normally would; that has no effect on this repo.

## Reporting an issue
Open a GitHub issue (omit any secret) or contact Fusion Data Company directly.

## Scope / use
Underwriter OS produces research and analysis to inform decisions. It is **not** legal, tax, securities, or investment advice. Any owner/entity research uses public records and licensed business data your firm connects; any property/skip-trace tooling should enforce its own suppression/opt-out controls.
