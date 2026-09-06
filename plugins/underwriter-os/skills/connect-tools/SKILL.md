---
name: connect-tools
description: Ask the user what tools and data their firm already pays for, then connect them — or set up an export/drop path for the ones with no connector — and capture the firm's real numbers for calibration. Runs during onboarding and any time someone says "connect," "add data," "make it more accurate," "hook up CoStar/Yardi," or wants better comps. Claude does the asking and the walking-through; the user just answers and clicks.
---

# Connect Tools & Data (Claude asks them; Claude can't assume)

The single biggest accuracy upgrade is **the firm's own data** + a **real comp/cap-rate feed**. Nobody else can connect these — only the user themselves can, using their own logins and keys. So **you** run this with them: ask what they have, connect it, and for tools with no connector, set up the export-and-drop path. Hands-off (HARD LAW: do it for them; for the few clicks only they can do, walk them through exactly).

## Step 1 — See what's already connected (don't ask what you can check)
Look at the connectors already enabled in this Claude. Greet what's there, then only ask about the gaps.

## Step 2 — Ask the checklist (plain English, a few at a time)
"To make my analysis match how your firm actually underwrites, what does the firm already use? No wrong answers — tell me what you've got:"
- **Market data:** CoStar? Yardi Matrix? RealPage / Axiometrics? Apartments.com/ALN? (rents, cap rates, supply pipeline, sale comps)
- **Underwriting/asset mgmt:** ARGUS? Yardi Voyager? an in-house Excel model?
- **Workspace:** Google Workspace or Microsoft 365? (Drive/Gmail/Calendar or OneDrive/Outlook)
- **CRM:** HubSpot? Salesforce? (investors, deals)
- **Accounting:** QuickBooks? Yardi? (actuals, T-12s)
- **Storage:** Dropbox / Box / SharePoint? (where deal files live)

## Step 3 — Connect each one they have
- **Has a first-party Claude connector** (Yardi Matrix, Google Drive/Gmail/Calendar, HubSpot, QuickBooks, Slack, Notion, Salesforce, Box/Dropbox): walk them in plain words — **Settings → Connectors → find it → Connect → sign in on the popup.** That's it. Confirm, then use it.
- **No Claude connector** (CoStar, RealPage, ARGUS, Yardi Voyager): set up the **export-and-drop path** — "In [tool], export the rent comp set / submarket report / sale comps / T-12 as PDF, Excel, or CSV, and drop it in your Underwriter OS folder (or paste it here). I'll read it directly and cite it." This gets you CoStar-grade comps with no API.
- Tell them which is which; never ask them to do anything technical beyond a login or an export.

## Step 4 — Capture the firm's real numbers (the calibration gold)
Ask, and ingest whatever they'll share:
- **One past deal** — a model, an OM, or even a rent roll + cost summary.
- **Their return hurdles** — target IRR, yield-on-cost, development spread, and the exit caps they've actually traded at.
- **Their cost of capital / typical debt terms.**
When they provide any of it, extract the real assumptions (achieved effective rents & $/SF, true hard-cost/SF by product, exit caps, hurdle rates) into **`underwriter-os/reference/firm-actuals.md`** (cite the source doc + date). From then on, **use the firm's actuals over generic market estimates** — that's the difference between an outside read and how this firm underwrites.

## Step 5 — Record it
Update the person's `CLAUDE.md` "connected tools" line and their `underwriter-os/memory/<slug>.md` with what's connected and what export-feeds exist, so every future session knows. If they connected a market-data feed or shared actuals, note it so `underwriting-research` and `market-comp-analysis` use it first.

## Tone & rules
- Make it effortless: most answers are "yes/no," then one login or one export.
- Never expose keys or config. This is between you and the user — no one else needs access to their tools.
- If they have nothing beyond web search, that's fine — say so and proceed; the OS still delivers. Offer to revisit when they're ready.
