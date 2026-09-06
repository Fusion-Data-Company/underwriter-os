---
name: market-comp-analysis
description: Pull rent comps, occupancy, supply pipeline, absorption, and cap-rate trends for a submarket, then build a market study. Use when the user asks for "comps," "rent comps," "market study," "what are rents doing," "cap rates," "what's the competition," or needs the market picture behind a deal.
---

# Market & Comp Analysis

Build the market picture behind a deal: what rents are achievable, what's competing, where the market is heading.

## When to use
"Pull comps for [submarket]," "build me a market study," "what are rents/cap rates doing in [market]," "who are the competitive properties near [site]?"

## Inputs
- Subject property/site location and product type.
- Unit mix if known (studio/1BR/2BR/3BR), target rent band if any.
- Radius or named submarket for the comp set.

## What to assemble (cite sources + dates)
1. **Comparable set** — 4–8 competing communities: name, location, year built, units, unit mix, current asking rents (by unit type and per SF), concessions, occupancy. Note the source for each.
2. **Rent trend** — direction and rate of rent growth over the last 1–3 years for the submarket.
3. **Occupancy / vacancy** — current and trend.
4. **Supply pipeline** — units under construction and planned nearby; expected delivery timing; absorption pace. Call out oversupply risk explicitly.
5. **Cap-rate & sales trend** — recent multifamily sales/cap rates in the market if available; direction of movement.
6. **Concessions & lease-up reads** — what new deliveries are offering to lease up.

## Tools
- **Yardi Matrix** connector if connected — best for rents, comps, pipeline, ownership.
- Otherwise built-in web search / Tavily / Exa: pull from property marketing sites, market reports (CBRE/JLL/Cushman/Marcus & Millichap), census/BLS, local news on new developments.
- The user can also paste CoStar/RealPage exports — fold those in and cite them as firm-provided.

## Output
- **Market study** using `underwriter-os/templates/market-study.md`, saved to the deal folder.
- **Comp table** (clean, sortable): community, rents by type, $/SF, occupancy, vintage, distance.
- **Read on achievable rent** for the subject + the supply risk verdict.
- Bottom line: is the market supportive of this deal's rent and absorption assumptions?

## Accuracy
- Every comp and number gets a source + date. If a rent is an estimate, label it.
- Don't average across non-comparable product — note when comps are imperfect.
- Distinguish asking rents (advertised) from effective rents (after concessions) and say which you used.
