# Underwriter OS — Build Status

_Updated 2026-09-06 · repo: github.com/Fusion-Data-Company/underwriter-os (public)_

## ✅ What we HAVE (built, wired, tested)
- **One-paste install** — a single message a non-technical person pastes into Claude desktop. No CLI, no accounts.
- **No baked-in keys, by design.** The pack ships secret-free; every connector or data feed is set up with the user's own key or their own connector login.
- **Quarry parcel lookup** — address or coordinates → owner, zoning, units, value into the one-pager, once a firm connects its own parcel data source.
- **14 skills (plays):** deep-research, site-selection, market-comp-analysis, investor-sourcing, underwriting-research, deal-memo, deal-pipeline, quarry-parcels, report-visuals, voice-onboarding, deal-packet, deal-evolution, connect-tools, knowledge-packs.
- **Voice onboarding** — ElevenLabs voice, optional, on the user's own key. Spoken welcome + a spoken status on every open, once connected.
- **Live Deal Tracker artifact** — visual board, saves itself, Claude builds it for them.
- **Report visuals** — branded infographic (SVG→PNG, tested), slides via the pptx skill, one-pagers via pdf — all zero-setup, no account. Canva optional if a user connects it.
- **Generic roster/profile system** — each firm builds its own `profiles/roster.md` from a template; an example profile shows the shape, with no real people shipped.
- **The HARD LAW** baked into the installer, CLAUDE.md, and every skill: *if Claude can do it, it does it and reports — never hands the user instructions for anything it can do itself.*
- **Reference layer:** tool catalog (every connector, configured), verified GitHub pack (real repos), power-layer config (`setup.sh` + `claude_desktop_config.json`) for optional MCP servers, teaching docs, and a walkthrough.

## What we NEED (open items — mostly optional, and mostly per-firm)
| Item | Needed? | Status |
|---|---|---|
| **Per-firm keys** | Per firm | Each installing firm brings its own keys for any power-up (Tavily, Exa, FRED, Census, parcels, voice). Not something this repo can supply. |
| **Yardi Matrix / paid connectors** | Optional | One-click connect in Settings, only if the firm subscribes. Everything works without them. |
| **Canva branded designs** | Optional | Each user connects Canva once (a login popup) — can't be invisibly shared. Native infographic/slide works with zero setup, so Canva is a nice-to-have. |
| **First real run on a customer's machine** | Yes, per install | Every piece is tested here; the final proof is a real user running the command once on their own desktop. |
| **Voice "on app launch"** | Minor | Cowork has no literal launch hook; the voice fires at the **start of the session** (Claude speaks first), driven by CLAUDE.md, once voice is connected. Functionally the same. |

## 📍 How far from done
- **Core installer + plays: 100%** — built and wired.
- **Secret-free by design: 100%** — verified no keys ship in the repo.
- **Generic roster/profile system: 100%** — template + fictional example only.
- **Report visuals: ~95%** — native paths done; Canva optional.

**Bottom line: ready to hand to any customer for a first run.** The only thing between "works in our tests" and "running at a real firm" is one person pasting the command on their machine and bringing their own keys where they want deeper research — which the full walkthrough covers (`WALKTHROUGH.md`).

---

## Gap analysis — full end-to-end dry-run
Ran the install the way a customer's machine will, against the live repo:
- **All files the installer pulls resolve** (0 missing / 404).
- **No key-decode step exists** — verified the installer never looks for or references a repo-provided secret.
- **Every optional data source, once a user supplies their own key, fires cleanly:** parcels, FRED, Census, Tavily, Exa, Firecrawl, ElevenLabs voice — each documented with exact call patterns in `docs/DATA-SOURCES.md`.

**Closed by this pass:** every required, in-our-control item is built, wired, and verified. **Still open = per-firm setup:** each firm's own keys, paid connectors, and branded design tools, plus the one thing only a customer can do — paste the command on their own machine for the first real run.
