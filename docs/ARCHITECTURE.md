# Underwriter OS — Architecture

## The idea
A **public GitHub repo carries the machinery**; **secrets and personal data never live in it** — this repo ships with zero keys and zero client/employee data. A team member pastes one message; Claude fetches `START-HERE.md`, writes a personalized workspace on their machine, and from then on behaves as Underwriter OS in that folder.

## Repo layout
```
START-HERE.md            the installer Claude reads and executes
INSTALL.md / README.md   human entry points
plugins/underwriter-os/
  .claude-plugin/        plugin.json (+ marketplace.json at root) for the Claude Code path
  skills/                the "plays" — each a SKILL.md (+ helper scripts)
templates/               CLAUDE.md, memo / market-study / one-pager / infographic / tracker / Excel model / intake / sources
profiles/                README + roster template + a fictional example profile (each firm builds its own)
reference/               underwriting-model, property-data-dictionary, rigor-standard
catalog/                 TOOL-CATALOG (connectors) + GITHUB-PACK (verified repos)
brand/STYLE.md           the look of every deliverable
docs/                    this documentation
config/                  firm-defaults.md (placeholder until filled in), power-layer MCP config, setup.sh — no keys
memory/                  persistent memory (per-user records written at onboarding)
```

## What happens on install
1. Pull the pack into the user's `underwriter-os/` workspace. No keys to decode — there aren't any in the repo.
2. **Identify the person** (one line: who they are + their role; check `profiles/roster.md` if the firm has built one) and write their `CLAUDE.md` + `memory/<slug>.md` from that plus `config/firm-defaults.md`.
3. Build their **Deal Tracker** artifact, welcome them, run a real task to prove it.
4. **Ask what tools the firm uses** (`connect-tools`) and connect them or set an export path; capture the firm's real actuals for calibration.

## The governing behavior: V1 → V2 → V3 (`deal-evolution`)
Every analysis auto-evolves from one prompt: **draft (V1) → self-critique → harden (V2) → finalize (V3)** to the **[rigor standard](../reference/rigor-standard.md)** (IRR, yield-on-cost untrended/trended, spread over cost of capital, debt yield, replacement-cost basis, base/downside/upside, local-accuracy mandate). The user asks once; Claude delivers the final. Output is tuned per person, per their stated format preference — brevity for some, full detail for others.

## Two install paths
- **Desktop / Cowork (default, non-technical):** the one-paste bootstrap above. Web search works immediately; connectors and any deeper data source are one-click / bring-your-own-key upgrades.
- **Claude Code (technical):** `/plugin marketplace add Fusion-Data-Company/underwriter-os` (the repo is also a plugin marketplace).

## Data & trust
- Parcels via a connected parcel data source (e.g. Quarry), once set up. Research via web search always, plus FRED/Census/Tavily/Exa/Firecrawl once the user brings their own keys. Optional pro feeds (CoStar/Yardi) connected per-user via `connect-tools`.
- **Citations everywhere** (`docs/CITATIONS.md`): every figure backlinks to a `sources.md`; estimates labeled; numbers reconcile across model/memo/deck/one-pager.

## Privacy
Per-user `CLAUDE.md`, `memory/`, and any firm data stay on the user's machine — never committed to the public repo (`.gitignore` enforces it).
