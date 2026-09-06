# Firm defaults (pre-configured operating settings)

Generic starting defaults the plays use unless a user overrides them. The installer folds the relevant pieces into each person's `CLAUDE.md`. **Edit this file for your firm** — fill in your real markets and criteria below; everything here is a placeholder starting point, not law.

## Default target markets
**{{FILL IN: your firm's target metros/submarkets}}** — e.g. "Sunbelt secondary metros," "Mid-Atlantic infill," or a specific list of MSAs. Leave blank during first install and let intake fill it in from what the user tells Claude; update this file once the team's real footprint is confirmed.
> Treat whatever markets you list here as the default scan list. Add/remove per each user's actual focus during intake.

## Comp-set defaults (market-comp-analysis)
- Radius: **3 miles** urban infill · **5 miles** suburban/garden. (Adjust for your markets' density.)
- Vintage: prioritize comps built within **~10–15 years**; flag older as imperfect.
- Product match: same type (garden / mid-rise / urban) and comparable unit mix.
- Always report **effective rents** (after concessions) alongside asking; state which drove the conclusion.
- Minimum comp set: 4; target 6–8.

## Underwriting research defaults (underwriting-research)
- Always pull current macro context from **FRED**: `MORTGAGE30US` (30-yr mortgage), `DGS10` (10-yr Treasury), `CPIAUCSL` (CPI), `HOUST` (housing starts), `CSUSHPINSA` (Case-Shiller HPI).
- Treat **property taxes** (reassessment at stabilization) and **insurance** as **high-sensitivity** inputs — research both carefully every time; flag markets with known tax/insurance volatility.
- Present each assumption as a **low / base / high** range with source + date, not a single number.
- Flag the 2–3 inputs the deal is most sensitive to.

## Census variables of interest (site-selection / market sizing)
- `B19013` median household income · `B25064` median gross rent · `B25031` median rent by bedrooms · `B25003` tenure (renter vs owner) · `B01003` total population.
- Use at tract / place / ZIP level for market sizing and feasibility.

## Deliverable defaults (deal-memo)
- Lead with the **recommendation and the ask** — support follows.
- Every number sourced + dated; estimates labeled; numbers from the firm's own model tagged **"per {{FIRM NAME}} underwriting."**
- Risk section **leads with supply pipeline**, then basis.
- Default formats by audience: IC → Word memo + comp appendix; lenders → tight PDF; LPs → deck (Canva) + one-pager; internal → markdown.

## Deal criteria (fill in during onboarding)
**{{FILL IN: what makes a deal a yes or a no for your firm}}** — e.g. target yield-on-cost spread over market cap rate, minimum unit count, product type, hold period, target IRR/equity multiple. Ask each new user this during intake and refine it here once the team agrees on real criteria.

## Research defaults (deep-research)
- Prefer primary/authoritative sources; confirm material facts across 2+ sources; label single-source items.
- Note the date of every source; flag data older than ~12 months for fast-moving figures (rates, rents, pipeline).

## Accuracy (always)
- Cite sources with dates; label estimates.
