# Underwriter OS — Citation & Backlinking Standard (cite EVERYTHING)

**Rule:** every number, claim, comp, owner, rate, and date in any Underwriter OS deliverable must be traceable to a source that anyone can click and verify. No exceptions. If it can't be sourced, it's labeled an estimate or omitted.

## The three labels (every figure is one of these)
- **Sourced fact** — has a citation `[S#]` pointing to a real, checkable source.
- **Estimate** — Claude's reasoning; written as "est." and explained.
- **Per [Firm] underwriting** — a number from the firm's own model; tagged that way.

## The sources registry (the backlink target)
Every deal folder gets a `sources.md` — the single registry every deliverable links back to. Each entry:

```
### [S3] [County] Assessor — parcel [APN]
- URL: https://...           (direct link to the record/page)
- Source type: County assessor record
- Accessed: 2026-06-22
- Pulled via: Quarry /api/parcels/at
- Note: 2.59 ac, Light Industrial, $6.24M market value
```

Assign IDs in order: `S1, S2, …`. Reuse an ID if the same source backs multiple figures.

## How to cite in each format (backlinks everywhere)
- **Markdown (memos, one-pagers, research):** inline `[S3]` after the figure, linked to the registry: `… $6.24M assessed value [[S3]](sources.md#s3).` End every doc with a **Sources** section that reproduces the registry entries with live URLs.
- **Infographic / SVG snapshot:** small superscript `[S#]` next to figures; a footer line "Sources S1–S6 — see one-pager." The companion one-pager/sources.md holds the links.
- **Excel (.xlsx):** a dedicated **Sources** tab (ID, source, URL, date, pulled-via). In data cells, put the source ID in an adjacent "Src" column or cell comment so every number traces to a row on the Sources tab.
- **Slides (.pptx):** a footnote on each data slide ("Source: FRED DGS10, 2026-06-22 [S2]") and a final **Sources** slide listing all entries with URLs.
- **PDF:** numbered endnotes mapping to the registry with URLs.

## Source-quality hierarchy (prefer the highest available)
1. Primary records & official data — county assessor/recorder, Secretary of State, SEC EDGAR, Census, FRED, BLS, Quarry.
2. Institutional market reports — CBRE, JLL, Cushman, Marcus & Millichap, Yardi Matrix.
3. Reputable trade press / local news of record.
4. General web (label clearly; corroborate with a 2nd source).
Confirm material figures across **2+ independent sources**; flag any single-source item.

## Freshness
Every source carries an **access date**. Flag anything older than ~12 months for fast-moving figures (rates, rents, cap rates, supply pipeline) and refresh.

## What "pulled via" should say (so it's reproducible)
Name the exact path so a colleague can re-run it: `FRED series DGS10`, `Census ACS5 2022 B19013`, `Quarry /api/parcels/at`, `Tavily search: "<query>"`, `Exa: "<query>"`, `Firecrawl: <url>`, or the direct web URL.

## Hard rules
- Never present an unsourced number as fact. Never invent a URL, owner, comp, or figure.
- If a source can't be located, say so and mark the figure an estimate.
- Every deliverable Underwriter OS produces ends with, or links to, its sources registry — so anyone can fact-check everything.
