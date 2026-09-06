# Underwriter OS

**Turn Claude into a research-and-underwriting teammate for your institutional real-estate or multifamily team — in one paste, no setup, no subscriptions, no command line.**

Underwriter OS installs itself by telling Claude to read its own instructions. A team member pastes one message into the Claude desktop app; Claude pulls the pack, interviews them, writes them a personalized `CLAUDE.md`, teaches them how it works, and runs a real research task live.

---

## ✅ How to install (give this to anyone on your team)

1. Open the **Claude desktop app**.
2. Paste this message and send it:

> **Install Underwriter OS for me. Fetch this file and follow every instruction in it exactly, then walk me through setup step by step in plain English: https://raw.githubusercontent.com/Fusion-Data-Company/underwriter-os/main/START-HERE.md**

3. Answer Claude's questions. That's it — Claude does the rest (about 5–10 minutes).

There is nothing to download, no account to create, and no code to run. The free version works with the web search already built into Claude.

---

## What it gives each person
- A personalized **CLAUDE.md** so Claude always knows their role, their deals, and how your firm works.
- Seven research **plays** (skills): deep research, site selection, market & comp analysis, investor & owner sourcing, underwriting research, deal memos, and deal-pipeline tracking.
- Plain-English coaching on what it can do and how to use it.
- Optional, guided upgrades for deeper research (Tavily, Exa, Apollo, Yardi Matrix, and more) — bring your own keys; nothing is pre-configured for you.

## What it deliberately won't do
- It won't invent numbers — everything is sourced and dated, and it says when it can't verify something.
- It informs decisions; it doesn't give legal, tax, securities, or investment advice.

## Tools & repos it can pull in
Underwriter OS ships a fully-configured **tool catalog** and a **verified GitHub pack**:
- `catalog/TOOL-CATALOG.md` — every recommended connector (research, real estate, finance, investor/owner, docs, CRM, PM), tiered into *zero-cost defaults* vs *paid power-ups*, each mapped to the play it powers.
- `catalog/GITHUB-PACK.md` — ~30 verified public repos (Anthropic skills, MCP directories, real-estate/Census/SEC/FRED/Maps MCP servers, doc generators). Every repo confirmed live via the GitHub API with real star counts; archived ones flagged.

## Two paths, on purpose
- **Basic users** get one-click first-party connectors only — Connect → log in on the popup → done. Nobody non-technical is ever asked to touch a command line.
- **Power layer** (`config/`), for a technical teammate — ready-to-run setup for community MCP servers (Census, SEC EDGAR, FRED, OpenStreetMap, Tavily, Exa, Firecrawl, Google Maps, Alpha Vantage). Every run command is verified from each project's README.
```bash
cp config/.env.example config/.env     # paste in whatever keys your firm has
bash config/setup.sh                    # wires up only what your keys + runtimes allow; backs up your config
```
`config/CONFIG-GUIDE.md` has the exact steps, per-server nuance, and the two clone-and-build servers. `config/firm-defaults.md` holds your firm's own tuned defaults (markets, comp radius, FRED series, Census variables) — fill it in once, and every teammate's `CLAUDE.md` inherits it.

## Documentation
- **[INSTALL.md](INSTALL.md)** — the one-paste command + what happens.
- **[docs/](docs/README.md)** — documentation home: [how to use](docs/how-to-use-underwriter-os.md), [architecture](docs/ARCHITECTURE.md), [citations](docs/CITATIONS.md), [data sources](docs/DATA-SOURCES.md), [what is a CLAUDE.md](docs/claude-md-explained.md).
- **[reference/](reference/rigor-standard.md)** — [rigor standard](reference/rigor-standard.md), [underwriting model](reference/underwriting-model.md), [property-data dictionary](reference/property-data-dictionary.md).
- **[profiles/](profiles/README.md)** — how your team adds its own roster and profiles (none are shipped with this repo).
- **[CONTRIBUTING.md](CONTRIBUTING.md)** · **[SECURITY.md](SECURITY.md)** · **[CHANGELOG.md](CHANGELOG.md)** · **[STATUS.md](STATUS.md)** · **[WALKTHROUGH.md](WALKTHROUGH.md)** · **[LICENSE](LICENSE)** (MIT)

## What's in this repo
```
START-HERE.md            ← the installer Claude reads and executes
templates/CLAUDE.md.template
onboarding/              ← interview + connector setup + tool guide
catalog/                 ← TOOL-CATALOG.md + GITHUB-PACK.md
plugins/underwriter-os/skills/   ← 8 plays (7 research + knowledge-packs)
templates/               ← memo, market study, one-pager, folder structure
profiles/                ← roster template + a fictional example profile (your team fills this in)
docs/                    ← "what is a CLAUDE.md" + how-to guide
.claude-plugin/marketplace.json  ← optional, for Claude Code users
```

## Privacy
This repository ships with **no secrets, and no data about any specific firm or person**. Each person's information and their `CLAUDE.md` are generated and stored only on their own computer — never uploaded here.

---

## Want this configured for your firm?
Underwriter OS out of the box gets any team most of the way there. If you want it dialed in — your real markets, your deal criteria, your data connectors, your comp-set rules, your brand — **Fusion Data Company** will build it for you.

**[Reserve a build →](https://buy.stripe.com/5kQbJ12mT1TuaIn0OGaAw0b)** — $1,500 deposit, applied to your project. Fusion Data Company customizes the pack, the plays, and the connectors to your markets and tools. Full builds run **$3,500 to $15,000**, scoped to what you need.

Questions before you reserve? Contact Fusion Data Company (Rob Yeager) directly.

---
*Built by Fusion Data Company · MIT License · v1.0*
