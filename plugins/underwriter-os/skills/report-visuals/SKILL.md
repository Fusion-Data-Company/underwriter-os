---
name: report-visuals
description: Make an infographic, slide, or chart for a report — firm-branded, zero setup. Use whenever a deliverable would land better with a visual (deal snapshot, market study, IC deck, one-pager header), or when the user says "make an infographic," "add a slide," "make it look good," "chart this." Proactively add a visual when it helps — don't wait to be asked.
---

# Report Visuals

Turn numbers into something that looks like one institutional firm made it. **Works with zero setup — no account, no key.** Claude builds it and shows it (HARD LAW: do it for them).

## Pick the format
1. **Infographic (default, zero setup):** fill `underwriter-os/templates/infographic-deal-snapshot.svg` with the deal/market numbers (it's plain text with `{{PLACEHOLDERS}}`), save it, and show it. **XML-escape every value you insert** — replace `&`→`&amp;`, `<`→`&lt;`, `>`→`&gt;` (an unescaped `&` breaks the SVG). To hand them a PNG too, convert in the sandbox: `pip install cairosvg --break-system-packages -q && python -c "import cairosvg;cairosvg.svg2png(url='in.svg',write_to='out.png',output_width=1600)"`. You can also render it as a live artifact (create_artifact) so it's pinned in the sidebar.
2. **Slide / deck:** use the **pptx** skill (Tier 0, no account) — build a branded slide or a short IC deck. Navy `#0f2233` / gold `#c8a14a`.
3. **Chart:** for trends/comps, render a chart as an artifact with Chart.js, or embed an image in the docx/pdf via the doc skills.
4. **Branded via Canva (optional):** if the user has the **Canva** connector enabled, you may generate a Canva design with their brand kit. Canva needs a one-time per-person login, so it is NOT required — only use it if it's already connected. The native paths above always work.

## The look
- Colors: deep navy `#0f2233`, secondary `#1b3a57`, gold accent `#c8a14a`, light bg `#f4f1ea`, ink `#0d1b26`.
- Clean, executive, lots of whitespace. Lead with the headline number. Label every figure; cite source + date in small footer text.

## When to add a visual (proactive)
- **Deal one-pager / IC memo:** add the deal-snapshot infographic header (units, basis, yield-on-cost, market).
- **Market study:** add a rent-comp bar chart and a supply-pipeline callout.
- **Investor materials:** a clean stat block / deck.
Don't ask permission for a small visual — make it, include it, and mention you added it.

## Output
- Save visuals into the deal folder alongside the memo. Note what you made. Never invent numbers for a chart — use the researched/model figures and cite them.
