# Contributing to Underwriter OS

Underwriter OS is a set of Markdown skills + templates + references that Claude reads. No build step — edits to the repo flow to users on their next install/update.

## Add or change a skill
1. Create `plugins/underwriter-os/skills/<name>/SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: <kebab-name>
   description: When to use this skill (be specific — this is how Claude decides to fire it).
   ---
   ```
2. Write the body as **instructions to Claude**: when to use, how to do it, what to output, guardrails. Keep it concrete; reference live data via `docs/DATA-SOURCES.md` and standards via `reference/rigor-standard.md`.
3. Add helper scripts in the same folder if useful (see `quarry-parcels/quarry_lookup.py`, `voice-onboarding/generate_voice.py`).
4. **Wire it in:** add the file to the pull list in `START-HERE.md`, list it in `templates/CLAUDE.md.template` §4, and add a row to `onboarding/what-each-tool-does.md`.

## House rules (match the existing system)
- **Every analysis runs the `deal-evolution` loop (V1→V2→V3)** and meets `reference/rigor-standard.md`.
- **Cite everything** per `docs/CITATIONS.md`; label estimates; never invent figures, owners, or URLs.
- **Brand**: all deliverables follow `brand/STYLE.md`.
- **Audience is institutional** — lead with judgment, not definitions.
- **Do it for them** — skills should perform the task, not hand the user instructions.

## Never commit secrets or PII
- This repo ships **no keys, ever** — not encoded, not plaintext. Never add a real `.env`, a user's `CLAUDE.md`, `memory/`, or deal data, and never add any firm's or employee's real information (name, email, portfolio, numbers). `.gitignore` enforces this — keep it that way. See [SECURITY.md](SECURITY.md).

## Verify before you push
- Confirm referenced files exist and resolve (raw URLs return 200).
- If you add an `.xlsx`/model with formulas, recalculate and confirm **zero formula errors**.
- Run a quick end-to-end sanity check the way `README`/`STATUS` describe.
