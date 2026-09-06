---
name: deal-memo
description: Assemble research into a polished investment committee memo, market study, or deal one-pager. Use when the user says "write the memo," "put together an IC memo," "make a one-pager," "turn this into a document for the committee/lenders/LPs," or wants research packaged into a deliverable.
---

# Deal Memo / Document Builder

Package the research from the other plays into a clean, audience-ready document.

## When to use
"Write the investment committee memo," "make a one-pager on this deal," "turn what we found into something for the lenders/LPs," "draft the market study writeup."

## First, ask one thing: audience & format
- **Audience:** Investment Committee, lenders, LPs/investors, internal, or partners? (Sets tone and what to emphasize.)
- **Format:** Word doc, PDF, slides, or one-page? (Use the matching builder/skill to produce the final file.)
Default to the user's CLAUDE.md format preference if set.

## Pull together
Gather outputs already produced (site one-pager, market study, comp table, assumptions memo, investor/owner brief). If something's missing and material, run that play first or flag the gap.

## Templates (in `underwriter-os/templates/`)
- `investment-memo.md` — full IC memo.
- `market-study.md` — market section.
- `site-one-pager.md` — quick deal/site snapshot.

## Structure of a strong IC memo
1. **Recommendation & ask** — what's being decided, the recommendation, the specific ask (approve pursuit, approve capital, etc.).
2. **Deal snapshot** — location, product, units, basis, business plan, key return metrics (as provided by the firm's model — don't invent returns).
3. **Market** — demand drivers, rents, supply pipeline, why this market now (from market study).
4. **Site** — site specifics, zoning/entitlement, owner/control status.
5. **Underwriting assumptions** — key inputs with sources and the sensitivity flags.
6. **Capital** — debt + equity plan, target partners (from investor sourcing).
7. **Risks & mitigants** — honest, specific; lead with supply and basis.
8. **Appendix** — comp table, sources.

## Output
- The finished document saved to the deal folder, in the requested format.
- Lead with the recommendation. Keep numbers sourced. Mark anything provided by the firm's model as "per [Firm] underwriting."

## Guardrails
- Don't fabricate returns, comps, or figures. Use the firm's model numbers as given; research-sourced numbers get citations.
- Present analysis, not investment advice; final decision and any legal/securities review stays with the firm and counsel.
- Keep it honest about risks — a memo that hides the supply pipeline isn't doing its job.
