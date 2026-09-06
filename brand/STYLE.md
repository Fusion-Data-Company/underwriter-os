# Underwriter OS — Brand & Style System

Apply this to EVERY deliverable so Underwriter OS output looks like one institutional firm made it. Executive, restrained, data-dense, lots of whitespace.

## Color
| Token | Hex | Use |
|---|---|---|
| Navy (primary) | `#0F2233` | headers, bars, dark blocks, primary text on light |
| Navy 2 | `#1B3A57` | secondary fills, subheads |
| Gold (accent) | `#C8A14A` | accent rule, key labels, the ONE thing to highlight |
| Bg (paper) | `#F4F1EA` | report background |
| Card | `#FFFFFF` | cards/blocks |
| Ink | `#0D1B26` | body text |
| Muted | `#5D6B76` | labels, captions, source lines |
| Positive | `#2E7D52` | favorable deltas (spread, growth) |
| Caution | `#B7791F` | watch items |
| Risk | `#B23B3B` | risk flags, negative deltas |
| Hairline | `#E3DDCF` | borders, gridlines |

**Chart palette (in order):** `#0F2233`, `#C8A14A`, `#1B3A57`, `#5D6B76`, `#2E7D52`, `#B7791F`. Subject property always navy; comps gold/grey.

## Typography
- Family: system sans (Helvetica/Arial/Inter) for screen + Office; serif (Georgia) only for long memo body if desired.
- Scale (pt): Display 30 / H1 22 / H2 18 / H3 15 / Body 11–12 / Caption 9–10.
- Weights: 700 headers & key numbers, 600 labels, 400 body. Numbers in tabular figures.
- Big numbers get the spotlight: stat values 40–46px, labels 14–16px uppercase muted.

## Wordmark
Type wordmark (no logo file): **YOUR FIRM NAME** in navy 700, with a gold subtitle for the document type (e.g., "Investment Committee Memo"). 6px gold rule under the navy header band. Swap in the firm's real name and, if they have one, their logo.

## Layout & components
- Generous margins; 12-col mental grid; align everything.
- **Stat block:** white card, hairline border, 12px radius; uppercase muted label, big navy value, tiny `[S#]` citation.
- **Recommendation badge:** navy block, gold "RECOMMENDATION" kicker, big white verdict.
- **Tables:** navy header row (white text), zebra `#FAF8F2`, right-align numbers, hairline rules, no heavy borders. Include a "Src" column referencing `[S#]`.
- **Callouts:** left gold bar for thesis; left red bar for risk.
- **Deltas:** ▲ positive (green), ▼ risk (red), with the number.

## Charts (decks, Excel, artifacts)
- No chartjunk: no 3D, no gradients, thin gridlines `#E3DDCF`, direct labels over legends where possible.
- Subject vs comps: subject navy + bold, comps muted. Title states the takeaway, not the metric ("Subject rents sit 6% below new deliveries").
- Always a source line under the chart.

## Per-format styling
- **Word (.docx):** navy H1/H2, gold H3 accents, 1" margins, 11pt body, footer with page # + "[Your Firm] — Confidential" + date; sources as endnotes.
- **Excel (.xlsx):** navy header fills + white bold text; inputs in `#FFF8E1` (editable), calcs locked/grey; number formats — $ #,##0, 0.0%, 0.00x; a **Sources** tab + "Src" columns; freeze header row; tab colors navy.
- **PowerPoint (.pptx):** navy title bar + gold rule master; one idea per slide; big number + chart; final Sources slide.
- **PDF / SVG one-pager:** the deal-snapshot / parcel-snapshot layout; footer cites sources.

## Voice
Institutional, confident, concise. Lead with the recommendation/number. No hype, no filler. Plain English a principal reads in 30 seconds, with the depth underneath.

## Non-negotiables
- Every figure carries a `[S#]` (see `docs/CITATIONS.md`).
- Consistent colors/fonts across sheet + doc + slides in a packet (one firm, one look).
- Label estimates; tag the firm's own model numbers (e.g. "per [Firm] underwriting").
