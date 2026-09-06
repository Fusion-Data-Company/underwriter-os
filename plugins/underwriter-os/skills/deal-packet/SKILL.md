---
name: deal-packet
description: Produce the full institutional deal packet for a deal — Excel underwriting model + Word IC memo + PowerPoint deck + PDF one-pager — all firm-branded, fully cited, and cross-linked to one sources registry. Use when the user says "build the packet," "full workup," "put together the IC package," "model this deal," or wants the complete set of deliverables.
---

# Deal Packet — the full institutional set

The flagship deliverable: one cohesive, branded, fully-cited package a principal or IC can act on. Claude builds all of it (HARD LAW: do it for them) and saves it to the deal folder.

## Read first
- `underwriter-os/reference/underwriting-model.md` — every line item, formula, sensitivity (the analytical authority).
- `underwriter-os/reference/property-data-dictionary.md` — parcel → development read.
- `underwriter-os/brand/STYLE.md` — the look (colors, type, tables, charts) for ALL pieces.
- `underwriter-os/docs/CITATIONS.md` — cite everything; build the sources registry.
- `underwriter-os/reference/rigor-standard.md` — the institutional metric set + checks every piece must hit. **Produce the packet via the `deal-evolution` loop (V1→V2→V3) — don't ship a first draft.**

## Build order (gather data once, render four ways)
1. **Pull the data** (cite each as you go into `deals/<name>/sources.md`):
   - Parcel/owner via `quarry-parcels` (owner, zoning, units, acreage, value).
   - Market & comps via `market-comp-analysis` (rents, occupancy, supply pipeline).
   - Macro via FRED (rates), demographics via Census, deeper context via Tavily/Exa (see `docs/DATA-SOURCES.md`).
   - the firm's model inputs from the user (tag "per [Firm] underwriting").
2. **Excel model** (`xlsx` skill) — build from the model-tab outline in `underwriting-model.md`: Inputs, Revenue, OpEx, Dev Budget, Returns, Sensitivity, Comps, **Sources** tab. Branded per STYLE.md (navy headers, input cells highlighted, number formats, "Src" columns). Save `deals/<name>/<name>-model.xlsx`.
3. **IC memo** (`docx` skill) — from `templates/investment-memo.md`: recommendation & ask, snapshot, market, site, assumptions (with sensitivity), capital, risks/mitigants, appendix. Every figure `[S#]`; sources as endnotes. Save `deals/<name>/<name>-IC-memo.docx`.
4. **Deck** (`pptx` skill) — ~8–10 slides: title, recommendation, market, site/parcel, returns, sensitivity, capital stack, risks, sources slide. STYLE.md master. Save `deals/<name>/<name>-deck.pptx`.
5. **One-pager** (`report-visuals` → `infographic-deal-snapshot.svg` → PDF/PNG) — the at-a-glance snapshot with cited figures. Save `deals/<name>/<name>-one-pager.pdf`.
6. **Sources registry** — `deals/<name>/sources.md` populated; every deliverable backlinks to it.

## Tune to the person (read their profile/memory)
- **Brevity mode:** lead with the one-pager + a 20-second spoken brief (voice-onboarding). Build the full packet, but PRESENT the one-pager first and keep talk to the bottom line; offer the rest. Simplicity up front.
- **Full-detail mode:** lead with the Excel model and the complete packet; walk the tables; overkill is under-rated. Hand over every file.

## Quality bar (check before delivering)
- One consistent look across sheet/doc/slides (STYLE.md).
- Every figure carries `[S#]` and resolves in `sources.md`; estimates labeled; firm-model numbers tagged.
- Numbers reconcile across the four pieces (the memo, model, deck, one-pager agree).
- Recommendation + the ask are unmistakable. Risks are honest (lead with supply).

## Output
- A `deals/<name>/` folder with the 4 deliverables + `sources.md`, added to the Deal Tracker. Tell them what you built and where; for brevity-mode, show the one-pager and speak the bottom line.
