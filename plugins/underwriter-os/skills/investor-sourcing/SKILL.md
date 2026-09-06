---
name: investor-sourcing
description: Research capital partners and LPs for a raise, and research who owns or controls a parcel or entity and how to contact them. Use when the user says "find investors," "who could fund this," "research this capital partner," "who owns this land/parcel," "who's behind this LLC," or needs investor/owner background and contact.
---

# Investor & Owner Sourcing

Two clean jobs: (1) research **capital partners / LPs** for a raise, and (2) identify **who owns or controls** a property or entity from public records — the legitimate, defensible version of "finding the right person."

## When to use
"Who could we raise this from?", "research [firm] as a capital partner," "who owns this site?", "what's behind this LLC?", "background on [investor/owner]."

## Data sources
- **Capital partners / firms:** public records (SEC, Secretary of State filings), licensed B2B data (Apollo, Lusha, Harmonic, CB Insights, ZoomInfo), company websites, reputable press, professional networks.
- **Property owners:** a connected parcel data source (`quarry-parcels` skill), if set up, for owner of record, mailing address, and owner phone/email; plus Yardi `search_by_owner` and county records.

## Job 1 — Capital partner / LP research
1. Define the raise: amount, structure (LP equity, JV, preferred, debt), deal profile, market.
2. Identify candidate partners that fit (active multifamily allocators, family offices, funds, JV equity groups, regional banks/debt). Use CB Insights/Harmonic if connected, else web research.
3. For each candidate, assemble a profile: focus (product/market/check size), recent activity, what they look for, and the right business point of contact (B2B sources only).
4. Rank by fit to this deal and to the firm's profile.
5. Output: a **target list** with profiles, fit rationale, and suggested approach. Save to the deal folder.

## Job 2 — Owner / entity research (who controls a parcel)
1. Start with the parcel: county assessor/recorder records for owner of record; Yardi `search_by_owner` if connected.
2. If the owner is an entity (LLC/LP), trace it through Secretary of State business filings to the registered agent/principals (public filings).
3. Summarize: owner of record, entity chain, principals/contacts available from public/business sources, and any relevant transaction history.
4. Output: an **owner brief** for outreach or acquisition strategy. Cite each record.

## Output
- Target list or owner brief saved to the deal folder, every fact sourced (record name + date).
- Clear "how to approach" recommendation.

## Accuracy
- Cite each source; don't fabricate names, contacts, or figures.
- This is research — hand the firm the list/contacts; the firm runs the outreach.
