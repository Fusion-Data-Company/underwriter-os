# Changelog

All notable changes to Underwriter OS. Format loosely follows Keep a Changelog.

## [Unreleased]
- **Rebranded to Underwriter OS; removed all firm-specific profiles and keys.** The pack is now firm-agnostic: no baked-in API keys, no named employees, and no single company's portfolio data. Each team supplies its own roster (`profiles/roster.md`), its own keys, and its own defaults (`config/firm-defaults.md`).

## [1.0.0] — 2026-06-22
First production release.

### Core
- One-paste installer (`START-HERE.md`) — desktop/Cowork, zero setup; Claude Code marketplace path too.
- Personalized `CLAUDE.md` + **persistent memory** (`memory/`) — remembers each user across sessions.
- **Identity by conversation** — one line asks who's working today and their role, then generates a personalized `CLAUDE.md` from the answer plus the firm's own defaults file.

### Analysis & rigor
- **`deal-evolution`** — governing V1→V2→V3 loop: every analysis drafts → self-critiques → hardens → finalizes from one prompt.
- **`rigor-standard`** — institutional metric set (IRR, equity multiple, untrended/trended yield-on-cost, spread over cost of capital, debt yield, replacement-cost basis, base/downside/upside, local-accuracy mandate).
- Deep references: `underwriting-model`, `property-data-dictionary`.
- **Cite-everything** standard with per-deal `sources.md` backlinks.

### Skills
deep-research · site-selection · market-comp-analysis · investor-sourcing · underwriting-research · deal-memo · deal-pipeline · quarry-parcels (parcel + owner data via Quarry, where connected) · report-visuals (infographic/slide/chart) · voice-onboarding (ElevenLabs, optional) · deal-packet (Excel + memo + deck + one-pager) · connect-tools (asks each user what the firm already uses; connects it or sets an export path; captures the firm's real actuals) · knowledge-packs.

### Data & calibration
- Optional live parcel lookups via Quarry; FRED, Census, Tavily, Exa, Firecrawl, Alpha Vantage wired for teams who bring their own keys.
- Power-layer (`config/`) for optional community MCP servers (Census, SEC EDGAR, FRED, Maps).

### Brand & deliverables
- `brand/STYLE.md`; branded infographic, one-pager, Excel model template, live Deal Tracker artifact.

### Docs
- Full OSS docs: README, INSTALL, docs/ (index, architecture, citations, data sources, how-to), CONTRIBUTING, SECURITY, MIT LICENSE, STATUS, WALKTHROUGH.
