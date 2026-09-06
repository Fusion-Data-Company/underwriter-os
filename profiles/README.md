# Profiles

This folder is empty on purpose. Underwriter OS ships with **no roster, no real employees, and no keys** — your firm builds this folder once, locally, and it never leaves your own machines.

## What goes here

### `roster.md` (your team, one row each)
Create `profiles/roster.md` with a simple table:

| name | email | title | focus | top plays |
|---|---|---|---|---|
| Jane Doe | jane@yourfirm.com | Acquisitions Director | Southeast multifamily | site-selection, deal-memo |
| ... | ... | ... | ... | ... |

- **name** — how Claude should address them.
- **email** — used to auto-match the signed-in Claude account to a roster row.
- **title** — their role at the firm.
- **focus** — markets, product type, or mandate they work on.
- **top plays** — the 2–3 skills (from `plugins/underwriter-os/skills/`) they'll use most, so Claude can tailor their `CLAUDE.md` without a long interview.

Anyone not on the roster just gets a quick 2-question interview during setup (role + what they work on) instead — the roster is a shortcut, not a requirement.

### `example-profile.md` (a template you can copy)
A fictional, fully worked example — **Jordan Reyes, Acquisitions Associate** — showing what a complete individual profile/`CLAUDE.md` seed looks like. Copy its structure for any team member who wants a fuller pre-built profile instead of the quick roster row (e.g. a principal whose voice/detail preferences are worth spelling out once).

## Privacy
Nothing in this folder is committed back to the public Underwriter OS repo. `roster.md`, any per-person profile you write, and every generated `CLAUDE.md` stay on your own machines — see `SECURITY.md`.
