---
name: deep-research
description: Go deep on any question across many sources and return a cited, decision-ready briefing. Use when the user asks to "research," "look into," "go deep on," "find out everything about," or needs a sourced answer to a non-trivial question — markets, regulations, competitors, costs, trends, people/companies, or any topic where a single web result isn't enough.
---

# Deep Research

Turn a plain-language question into a thorough, source-cited briefing. This is the research engine the other plays lean on.

## When to use
The user wants more than a quick answer: "research the Nashville multifamily market," "what's happening with construction costs," "look into this developer," "find everything on this incentive program."

## Tools, in order of preference
1. **Claude's built-in web search** — always available, no setup.
2. **Tavily, Exa, Firecrawl** if the user has connected them (their own keys) — exact call patterns in `underwriter-os/docs/DATA-SOURCES.md`. Also **FRED**/**Census** for macro & demographic facts, and a connected parcel data source (`quarry-parcels`) for property/owner facts.
3. **Yardi Matrix / finance connectors** if connected (real estate / market data).
Run the full method below regardless of which tools fire.

## Method
1. **Clarify the decision.** One sharp question if scope is unclear: what decision will this inform, and how deep do they need it? Then proceed.
2. **Decompose** the question into 4–8 sub-questions. State them.
3. **Fan out:** search each sub-question. Prefer primary and authoritative sources (government data, company filings, official market reports, reputable trade press). Note the date of every source.
4. **Triangulate:** confirm important facts across 2+ independent sources. Flag anything you can only find once as "single-source — verify."
5. **Adversarially check:** actively look for data that contradicts the emerging answer. Note disagreements rather than smoothing them over.
6. **Synthesize** into the output format below. Lead with the answer.
7. **Cite everything** with source + date. Never present an unsourced number as fact.

## Output (save to the workspace, e.g. `research/<topic>-<date>.md`)
- **Bottom line** — the answer in 3–5 sentences.
- **Key findings** — the important points, each with a source and date.
- **What's uncertain / contested** — gaps, conflicting data, single-source items.
- **So what** — implications for the deal/market/decision at hand.
- **Sources** — list with links and dates.

## Accuracy
- If you can't verify a claim, say so. Do not fabricate figures, comps, dates, or names.
- Distinguish fact (sourced) from estimate (your reasoning) — label estimates.
