# Underwriter OS — Persistent Memory

This folder is Underwriter OS's long-term memory. It's how Claude remembers each person and every deal **from one conversation to the next** in this workspace — not a chatbot that forgets, a teammate that builds on yesterday.

## Files
- `memory/<person-slug>.md` — one record per person (e.g., `memory/jordan-reyes.md`). Captured at onboarding from the interview, then grown over time. Holds: identity, role, **format mode** (brevity vs. full detail), markets, active deals, preferences, key people/contacts, decisions, and a **dated running log**.
- `memory/INDEX.md` — a one-line-per-person + per-deal index so Claude can orient fast and CLAUDE.md can backlink to everything.

## How Claude uses it (every session)
1. **On open:** read `memory/INDEX.md` and the current person's `memory/<person>.md`. Now you already know who they are, what they're working on, and what was decided last time.
2. **As you work:** append durable new facts — a new deal, a decision, a preference, a contact, a key number (with its source) — to that person's record under a dated log entry. Update `INDEX.md`.
3. **CLAUDE.md backlinks here** (§0) so memory is loaded automatically at the top of every session.

## What goes in (and what doesn't)
- IN: durable facts — deals, markets, criteria, decisions, preferences, relationships, recurring asks. Always dated; cite the source for any external figure.
- OUT: secrets/keys, one-off scratch, anything the person asks to keep private. This stays in the workspace, never anywhere public.

## Rules
- Append, don't overwrite history — the running log is the audit trail.
- Keep entries tight and skimmable. Summarize long threads to their durable takeaway.
- If something changes (new market, new role), update the top of the record AND log the change with a date.
