---
name: deal-evolution
description: The governing way Underwriter OS produces ANY analysis (feasibility, deal, market study, memo, model, site/market read). From ONE request, automatically evolve the work through V1 → V2 → V3 — drafting, then hardening, then finalizing — without the user asking again. Always invoked for analytical deliverables. The user asks once; you deliver the FINAL.
---

# Deal Evolution — V1 → V2 → V3 (automatic, one prompt)

**The skill is the evolution.** When someone asks for an analysis, you do NOT hand back a first draft and wait. You run the whole arc yourself — draft it, attack it, finish it — and deliver the V3. The user prompts once.

## The discipline (this is the part that matters)
- **Finish each version before you plan the next.** Do not pre-plan all three. Produce V1 completely → THEN look at what you actually made → THEN decide how to harden it → produce V2 → THEN critique again → produce V3. Plan the next phase only from the finished prior one. (Don't over-plan up front — build, then critique, then build.)
- **Each version must already carry full rigor** (see `underwriter-os/reference/rigor-standard.md`). V1 is not "sloppy" — it's the honest first pass with best-available data. V2 and V3 raise verification and depth, not basic competence.
- Keep going until V3 meets the bar. Don't stop at V1 or V2 and ask "want me to keep going?" — you already know they do.

## V1 — DRAFT (get a real, defensible answer on the page)
- Build the full structure and a first-pass answer using the best data you can pull now (parcel data if connected, FRED/Census if connected, web/Tavily/Exa, `config/firm-defaults.md` for the firm's calibration).
- Compute the core metrics. Label every estimate as an estimate.
- **End V1 when:** the deliverable is complete end-to-end and internally consistent — a real answer, not an outline.

## Self-critique gate (run between every version — adversarial, in writing to yourself)
Ask, and act on the answers:
1. **What's estimated that should be sourced?** Replace guesses with real, named, cited comps/figures.
2. **What's unverified or single-source?** Confirm across 2+ primary sources; flag what can't be.
3. **What local detail could be wrong?** Jurisdiction, submarket, corridor, school zone, zoning, who owns what — **readers who know this market will catch any off detail.** Verify every local specific against primary sources.
4. **What elite metric is missing?** (rigor-standard.md) — untrended/trended yield-on-cost, spread over exit cap AND cost of capital, IRR, equity multiple, cash-on-cash, debt yield, replacement-cost basis, rate-environment context.
5. **What would a top-tier sponsor poke?** Add the stress case, the rate sensitivity, the supply-pipeline check, the basis-vs-replacement check.
6. **Does it reconcile?** Every number agrees across model, memo, deck, one-pager; every source resolves.
7. **Any error?** (e.g., a wrong/mislabeled source, a transposed figure, a mis-attributed project.) Fix it.

## V2 — HARDEN
Apply every fix from the gate: real comps replace estimates, base/downside/upside, primary-source verification, the full elite metric set, errors corrected, basis checked vs. replacement and recent sales.

## V3 — FINAL (institutional, audience-tuned, QA'd)
- Full deliverable set per `deal-packet`: Excel model + IC memo + deck + one-pager (+ spoken brief, if voice is connected), all branded (`brand/STYLE.md`), all cross-cited to one `sources.md`.
- **Tune to the person's stated format preference (from their CLAUDE.md), both fully rigorous:**
  - **Brevity mode:** the one-page verdict + the 3–5 metrics that actually decide it + a short spoken brief if voice is connected. Never less rigorous — just the rigor that matters, with depth one layer down.
  - **Full-detail mode:** the complete model, every metric, every assumption with its source, sensitivity tables, the full packet. Overkill is the point.
- **Final QA pass:** numbers reconcile across all pieces; every `[S#]` resolves to a real URL; all local facts verified; estimates labeled; the recommendation/ask is unmistakable. Use a subagent for the QA read on high-stakes work.

## The audience truth
You are not explaining real estate to learners. You are briefing operators at the top of the industry. Assume fluency in cap-rate spreads, cost of capital, IRR vs. yield-on-cost, the rate cycle, replacement cost, and supply dynamics. Lead with judgment, not definitions.

## Output
Deliver the V3 (and keep V1/V2 working notes in the deal folder if useful). One prompt in → final-grade analysis out.
