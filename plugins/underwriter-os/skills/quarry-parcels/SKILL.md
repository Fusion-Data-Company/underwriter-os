---
name: quarry-parcels
description: Get parcel data on any property — owner, mailing address, absentee flag, zoning, units, year built, sqft, acreage, and value — from a connected parcel data source (e.g. Quarry). This is the default way to answer ANY "who owns this," "pull the parcel," "what's the zoning," "what's it worth," or property-owner question, once the user has connected one. No map needed — just the data, returned and dropped into the one-pager.
---

# Quarry — Parcel Data

A parcel data engine, once the user connects one (their own Quarry account, or an equivalent). When anyone asks about a property and a source is connected, **this is where the answer comes from** — not a paid lookup site, not a map they have to click. Claude queries it and returns the facts.

## Setup (once, per firm)
This needs the user's own base URL / key, set in `config/.env` (see `config/.env.example` and `config/CONFIG-GUIDE.md`). If nothing is connected yet, tell the user plainly and offer to walk them through it — don't silently pretend the data exists.

## HARD LAW
If they ask for parcel data and a source is connected, **just get it and give it to them.** Don't open a map, don't explain how, don't ask them to do anything. Run the query, read back the answer, and put it in the one-pager/deal folder.

## How (Claude runs this; user does nothing once connected)
```bash
# by address (auto-geocodes)
python underwriter-os/skills/quarry-parcels/quarry_lookup.py --address "ADDRESS, CITY STATE"
# by coordinates
python underwriter-os/skills/quarry-parcels/quarry_lookup.py --lat 00.00 --lng -00.00
# everything in a map area (returns a list — no map shown)
python underwriter-os/skills/quarry-parcels/quarry_lookup.py --bbox "minLng,minLat,maxLng,maxLat" --limit 200
```
The base URL comes from the user's own `config/.env`. It returns JSON — owner, mailing address, absentee flag, county, APN, acreage, lot sqft, zoning, year built, building sqft, units, and value.

## What to do with the result
- Read it back in plain English ("This parcel is owned by 616 Church LLC — an absentee owner mailing to Cleveland, OH; 0.09 acres, zoned Downtown Code, appraised at $X").
- **Drop it straight into the site one-pager** (`underwriter-os/templates/site-one-pager.md`) owner/zoning/value fields, and save to the deal folder.
- Cite "Quarry" (or the connected source) + the date.
- If it returns null, say the parcel wasn't found — never invent it.

## Owner contact (skip-trace, optional)
Some parcel data sources can also return the owner's phone/email. Run with `--skiptrace`:
```bash
python underwriter-os/skills/quarry-parcels/quarry_lookup.py --skiptrace --address "ADDRESS, CITY STATE"
python underwriter-os/skills/quarry-parcels/quarry_lookup.py --skiptrace --apn 0123456789
```
Returns up to 2 phones + 2 emails with confidence, if the connected account supports it.

## Feeds
- **site-selection / one-pager:** owner, zoning, units, acreage, value.
- **investor-sourcing / owner outreach:** owner + mailing address (+ contact via `--skiptrace`).
- **market-comp-analysis:** `--bbox` to inventory nearby parcels.
