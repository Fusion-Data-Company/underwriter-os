# Underwriter OS — What happens, minute by minute

This is exactly what a team member at an institutional real-estate firm experiences from the moment they open Cowork and run the install command. They type nothing technical and configure nothing.

---

## The one thing they do
1. Open the **Claude desktop app** and start Cowork.
2. Paste this and hit enter:

> **Install Underwriter OS for me. Fetch this file and follow every instruction in it exactly, then walk me through setup step by step in plain English: https://raw.githubusercontent.com/Fusion-Data-Company/underwriter-os/main/START-HERE.md**

That's the whole ask of them. Everything below, Claude does.

---

## Minute 0–1 — It greets them and sets up silently
- Claude reads START-HERE, says a one-line hello ("Setting up Underwriter OS — give me a couple minutes, you don't need to do anything"), and asks them to pick a folder (or uses the one that's connected). That folder becomes their workspace.
- In the background it pulls the whole pack from GitHub into an `underwriter-os/` folder. There's nothing to decode — the pack ships with no keys at all.

## Minute 1–2 — It asks who they are
- Claude asks one line: *"Who am I working with today, and what's your role?"* — then a quick follow-up on what they work on (markets, deal types, how their work is judged).
- If the firm has already built a `profiles/roster.md`, Claude checks it first and uses whatever's there to skip ahead.

## Minute 2–3 — It writes their brief
- Claude writes their personalized **CLAUDE.md** into the workspace (who they are, the firm's deal criteria, their markets, how they like deliverables) from their answers plus `config/firm-defaults.md`, and tells them in one sentence what it is: *"That's your permanent briefing — I read it every time so you never re-explain yourself. I keep it updated."*

## Minute 3–4 — It builds their live tracker
- Claude creates their **Deal Tracker** — a live visual board pinned in the sidebar — and says: *"I made you a live Deal Tracker; click any card to update a deal and it saves itself."* They didn't build or find anything.

## Minute 4–6 — It proves it on something real
- Claude does a real task end to end, then shows the result. If a parcel data source is connected, it pulls a real parcel for a site they care about — *"That parcel at [address] is owned by [LLC], an absentee owner mailing to [city]; 0.4 acres, zoned [X], appraised at [$]."* — and drops it into a clean one-pager with a branded infographic. Otherwise, it runs a quick sourced market read using web search. It saves the file to the deal folder and adds the deal to the tracker.

## Minute 6+ — They just talk
From here they say things in plain English and Claude **does them** (never tells them how):
- *"Who owns this parcel and what's it worth?"* → parcel data answers instantly, once connected.
- *"Is this submarket good for 260 units? Give me a one-pager."* → site read + infographic, saved.
- *"Pull rent comps and build a market study."* → comp table + study + chart.
- *"Research my underwriting assumptions — taxes, insurance, construction."* → sourced ranges (web, plus FRED/Census once connected).
- *"Turn this into an IC memo."* → Word memo with the deal-snapshot infographic.
- *"What's on my plate?"* → status + the tracker.
- *"Make me more powerful."* → Claude walks them through connecting any optional tool, using their own keys.

## Every time they open the folder after that
- Claude greets them by name, says what's ready and the one thing that needs a next step, then waits for what they need — and does it.

---

## What's powering it (they never see the mechanics)
- **Parcels/owners:** a connected parcel data source (e.g. Quarry), once the firm sets one up.
- **Research/market/macro:** web search always; Tavily, Exa, FRED, Census, Alpha Vantage, Firecrawl once the user brings their own keys.
- **Voice:** ElevenLabs, optional, on the user's own key.
- **Deliverables:** Word/Excel/PDF/PowerPoint + branded infographics, all zero-setup.
- **Tracking:** the live Deal Tracker artifact.
- **The rule over all of it:** if Claude can do it, it does it and tells them what it did.
