# Property / Parcel Data Dictionary — Reference

**Scope:** How Underwriter OS interprets parcel and property records (as returned by the **Quarry** engine) and turns a raw parcel into a development/acquisition thesis. Focus: ground-up Class A multifamily and value-add in the U.S. Southeast.

This document defines **every field Quarry returns**, how to read it for development/acquisition, the gotchas, and then how to go from a single parcel to a pursuit decision — including owner/entity research and the additional third-party data to pull.

---

## 0. Reading rules & the citation standard

- **Assessor data is administrative, not market truth.** Parcel records are maintained for taxation. Assessed values, and even some physical attributes, can be stale, lagged, or wrong. Verify anything load-bearing against a second source (deed, GIS, site visit, broker).
- **Citation standard (non-negotiable).** Every figure that lands in a deliverable — a value, an acreage, a unit count, a zoning conclusion — must carry **source + as-of date** (e.g., "Davidson County Assessor parcel record, pulled 2026-06-22"; "Metro Nashville zoning ordinance §17.x, current"). Conclusions derived from parcel data (e.g., buildable units) must cite the assumptions used.
- **Quarry is one input.** It seeds the analysis; the thesis is built by layering zoning, environmental, utility, demographic, and comp data on top (see §3–§6).

---

## 1. Field-by-field dictionary (Quarry output)

For each field: **what it is → how to read it → gotchas.**

### Ownership & contact

| Field | What it is | How to read it (dev/acquisition) | Gotchas |
|---|---|---|---|
| **apn** | Assessor's Parcel Number (a.k.a. PIN/Parcel ID) — the unique tax-map identifier for the parcel | The primary key. Use it to pull the assessor card, deed history, GIS layers, and to assemble adjacent parcels. Always carry it on every record | Format varies by county; one project often spans **multiple APNs** (assemblage). Re-platting changes APNs. Don't assume 1 APN = 1 developable site |
| **ownerName** | Primary owner of record (person or entity) | Who you negotiate with / send the letter to. An **LLC/LP/Trust** signals a sophisticated or estate-planning owner; an individual signals a potential off-market, relationship-driven deal | Owner of record can lag a recent sale; an entity name hides the real principals (see §4 entity research). Name may be a nominee/holding entity |
| **ownerName2** | Second owner / co-owner / "c/o" or additional vesting party | Co-tenancy (spouses, partners, multiple LLC members) — **all** signatories may be needed to contract | Can indicate fractional/heir ownership (harder to assemble) or a property-manager "care of" line rather than a true co-owner |
| **mailAddress** | Owner's mailing address (where the tax bill goes) | Compare to **situsAddress**: if different → **absentee owner** (see absenteeOwner). The mailing address often reveals the owner's home market or the manager's office | Mail may route to an attorney/CPA/PM, not the decision-maker. A PO box obscures the principal |

### Location

| Field | What it is | How to read it | Gotchas |
|---|---|---|---|
| **situsAddress / situsCity / situsState / situsZip** | The physical street address/location of the parcel ("situs" = where it sits) | Geolocate the site; anchor comps, demographics, flood, school, and traffic lookups; assess micro-location (corridor, walkability, adjacency) | Vacant/raw land may have **no situs address** or only a "0 Main St" placeholder — rely on APN + GIS centroid/coordinates instead. Address ≠ parcel boundary |
| **county** | County of record | Drives **which** assessor, GIS, deed registry, and **millage** apply; county sets the tax and (often with the municipality) the entitlement regime | A parcel can be in a county but inside or outside a **municipal** boundary — that determines zoning authority and tax overlays. Check city limits/ETJ, not just county |

### Owner-behavior signals

| Field | What it is | How to read it | Gotchas |
|---|---|---|---|
| **absenteeOwner** | Flag that the owner's mailing address differs from the property's location (owner doesn't live/operate there) | **A primary acquisition signal.** Absentee owners are statistically more likely to sell — especially out-of-state owners, tired landlords, or inherited holders. Prioritize for outreach | Absentee ≠ motivated by itself; a professional out-of-area investor may be a long-term holder. Combine with hold length (lastSaleDate), entity type, and absentee + long-hold for the strongest signal |

### Physical / site attributes

| Field | What it is | How to read it | Gotchas |
|---|---|---|---|
| **acreage** | Land area in acres | The denominator for **density** (units/acre) and the starting point for buildable-units math. Compare to zoning's max density and min lot size | Gross vs. **net** acreage differ — subtract unbuildable area (wetlands, floodway, easements, ROW dedication, steep slope). Always reconcile acreage with lotSqft (1 acre = 43,560 SF) |
| **lotSqft** | Land area in square feet | Use for **FAR** math (buildable SF = FAR × lot SF) and $/land-SF | Should equal acreage × 43,560; discrepancies flag a data error or an irregular/partial parcel |
| **useDesc** | Assessor's land-use / property-class description (e.g., "vacant residential," "garden apartments," "commercial," "single-family") | Tells you the **current** use and class. "Vacant" = ground-up candidate; an existing apartment class = value-add/operating comp; a low-intensity use on a high-density zoning = **underutilized** redevelopment target | This is the **assessor's** use code, not the legal **zoning**. Current use may be non-conforming or far below what zoning allows — the gap is the redevelopment opportunity. Codes are county-specific |
| **zoning** | The zoning district code assigned by the governing jurisdiction (e.g., "RM-20," "MU-G," "PUD") | The single most important development field — it governs **allowable use, density, height, FAR, setbacks, parking** (decode against the local ordinance; see §3) | Quarry's zoning may be stale or simplified. **Always verify against the live municipal ordinance/GIS.** Overlays (historic, design, flood, TOD, opportunity zone) modify base zoning and may not appear here. PUD/PD zoning means rules are in a **negotiated** site-specific document, not the base code |
| **zoningType** | A higher-level zoning category/classification (residential / commercial / mixed-use / industrial / agricultural) | Quick screen for whether multifamily is even plausible; mixed-use and higher-density residential are the targets | Coarse; never substitute for the actual district code and ordinance. "Residential" can still prohibit multifamily (single-family-only districts) |

### Improvement (building) attributes — for existing structures / value-add

| Field | What it is | How to read it | Gotchas |
|---|---|---|---|
| **yearBuilt** | Year the existing improvement was constructed | Vintage drives value-add scope, capex, functional obsolescence, and remaining economic life; very old or absent = likely **teardown/ground-up** | Reflects original construction, not renovations; a "1985" asset may be fully repositioned. Blank/zero = vacant land or missing data |
| **buildingSqft** | Gross building area of existing improvements | For value-add: basis for $/SF and rent/SF. For redevelopment: compare existing SF to **buildable** SF — a large delta signals upside | May be gross vs. net, may exclude/include garages or common areas, and is often approximate. Reconcile with units × avg unit SF |
| **units** | Number of dwelling units in the existing improvement | Confirms it's multifamily and its scale (for operating/value-add comps and per-unit metrics) | Assessor unit counts can be wrong or omit ADUs/converted space; verify with rent roll/site plan |
| **stories** | Number of building stories | Indicates building type (garden 2–3, mid-rise/podium 4–6, high-rise) → construction cost, parking strategy, and what's allowed under height limits | Existing stories ≠ what zoning permits for a new build (could be more or less) |
| **beds / baths** | Bedroom & bathroom counts (often the unit-level or aggregate config) | Helps infer unit mix and rentability (for value-add). For SFR/small parcels it's literal | For multifamily this field is often blank, an aggregate, or unreliable — confirm mix from the rent roll/plans |

### Valuation (assessment)

| Field | What it is | How to read it | Gotchas |
|---|---|---|---|
| **landValue** | Assessor's value attributed to the **land** | Indicates the assessor's land basis; compare to land **sale comps** to judge whether assessed land is low (room before reassessment) or rich | **Assessed ≠ market.** Many jurisdictions assess below market and/or at a fixed ratio. Use only as a relative/triangulation input, never as the land price |
| **improvementValue** | Assessor's value of the **building(s)** | If improvementValue is small relative to landValue, the structure contributes little → **redevelopment** signal (you're buying dirt). High improvement value = an operating asset | Same assessed-vs-market caveat; depreciation schedules can understate a renovated building |
| **totalValue** | Land + improvement assessed value | The tax base (subject to ratio/exemptions) and a rough floor reference | Not market value; do **not** cap-rate or price off it. Drives the **current** tax bill — but development triggers **reassessment** (see underwriting model §2.3) |
| **valueType** | What kind of value is reported (e.g., assessed, appraised, market, taxable) | **Read this first** — it tells you how to interpret landValue/improvementValue/totalValue and whether a ratio must be applied to get to market | If "assessed" in a fractional-assessment state, you must gross up by the assessment ratio to approximate market. If unstated, treat as assessed/administrative and verify |

### Transaction history

| Field | What it is | How to read it | Gotchas |
|---|---|---|---|
| **lastSaleDate** | Date of the most recent recorded sale | **Hold length = today − lastSaleDate.** Long holds (and absentee + long-hold) signal embedded gain, possible tax-deferral motive (1031), estate/retirement timing → seller motivation. Recent sale may mean a new, non-seller owner | Intra-family transfers, refinances, or deed corrections can reset the date without a true arm's-length sale. Pair with the deed (price, grantor/grantee) from the registry |
| **previousOwner** | Prior owner of record before the last sale | Context on chain of title; a recent change from an individual to an LLC may indicate repositioning or a flip; from estate to heirs indicates inherited property (often motivated) | Doesn't tell you price/terms — pull the recorded deed for that |
| **legalDescription** | The formal legal description (lot/block/subdivision or metes-and-bounds) | Definitive parcel identity for title, assemblage, platting, and the eventual PSA/closing | Metes-and-bounds and outdated plat references require a **current survey/ALTA** to trust boundaries and area. Never rely on it for buildable area |

---

## 2. Cross-field reads (the signals that matter most)

These combinations, not single fields, drive prioritization:

- **Underutilized land:** Low `improvementValue` relative to `landValue` (or `useDesc` far below what `zoning`/`zoningType` allows) → existing structure adds little; the value is the dirt and the entitlement → **redevelopment target**.
- **Motivated seller composite:** `absenteeOwner = true` + long hold (`lastSaleDate` many years ago) + individual/trust `ownerName` (or estate via `previousOwner`) → highest-probability off-market seller.
- **Assemblage candidate:** Multiple adjacent `apn`s with the same/related `ownerName`, or a target parcel too small alone but contiguous to others → plan a multi-parcel assemblage (control all before committing).
- **Density headroom:** `acreage`/`lotSqft` × allowed units-per-acre (or FAR) >> existing `units` → quantified upside (the core of the buildable-units estimate, §3).
- **Teardown vs. value-add:** Old `yearBuilt` + low `improvementValue` + high land basis → ground-up. Recent `yearBuilt` + meaningful `improvementValue` + apartment `useDesc` → value-add/operating play.

---

## 3. From parcel to development thesis (zoning → buildable program)

This is the core analytical move. Decode the zoning, derive the buildable program, and price the land per buildable unit.

### 3.1 Decode the zoning regulations (always against the live ordinance/GIS)

From the `zoning` district code, pull these parameters from the **municipal zoning ordinance and GIS** (Quarry's field is a pointer, not the answer):

| Parameter | What it controls | Why it matters |
|---|---|---|
| **Permitted/conditional uses** | Whether multifamily is by-right, requires a conditional/special-use permit, or is prohibited | By-right is far lower entitlement risk than rezoning/CUP |
| **Max density (units/acre)** | Cap on dwelling units per acre | Often the **binding** constraint on unit count for garden/mid-rise |
| **FAR (Floor Area Ratio)** | Max building floor area ÷ lot area | Binds on denser/urban sites; `buildable SF = FAR × lot SF` |
| **Height (ft / stories)** | Vertical limit | Determines building type (garden vs. podium vs. high-rise) → cost & parking |
| **Setbacks / yards** | Required distances from property lines | Reduce the **buildable footprint**; deep setbacks can sharply cut yield |
| **Lot coverage / impervious limits** | Max % of lot built/paved | Constrains footprint and surface parking; stormwater implications |
| **Parking ratio** | Required spaces per unit (and visitor/ADA/EV) | A major cost & feasibility driver — high ratios may force structured parking (expensive) or kill density |
| **Open space / amenity / landscaping** | Required green/amenity area | Further reduces net buildable land |
| **Overlays** | Historic, design-review, TOD, flood, opportunity-zone, inclusionary/affordable | Modify or override base zoning; can add density bonuses **or** restrictions/affordability mandates |

### 3.2 Estimate buildable units (two methods — take the lesser)

Run both density- and FAR-based estimates and use the **more restrictive** (then haircut for setbacks/parking/open space):

1. **Density method:** `Max units ≈ net acreage × max units-per-acre`.
   - Use **net** acreage (subtract floodway/wetlands/ROW/easements).
2. **FAR / envelope method:**
   - `Max building SF ≈ FAR × lot SF` (or derive from footprint × stories within height/setback/coverage limits).
   - `Max units ≈ (Max building SF × efficiency factor) / avg gross unit SF`, where efficiency (net rentable ÷ gross) accounts for corridors, walls, amenities (apply a realistic loss factor).
3. **Parking reality check:** Confirm the required parking **fits** (surface vs. deck) on the remaining land; parking, not zoning density, frequently caps real yield.

**Always express the result as a range** (conservative/base/aggressive) with the binding constraint named, and cite the ordinance section and date.

### 3.3 Land pricing per the program

- **Land $/unit:** `land price / buildable units` — the cleanest cross-deal land metric (self-adjusts for density). Compare to land-comp $/unit.
- **Land $/buildable-SF:** `land price / buildable building SF` — ties land cost to the entitlement.
- **Residual land value (the disciplined view):** Work **backward** from the supportable deal: `Residual land value = (stabilized value at target yield-on-cost) − (all hard + soft costs + developer profit)`. This is the maximum you can pay for land and still hit return targets — the right way to price a development site (feeds underwriting model §4.3, §5).
- **Source live:** Land comps from county deed records / CoStar / brokers (dated); costs from GC/indices; value/yield from the underwriting model.

### 3.4 Entitlement risk read

Classify the path and price the risk/time:

- **By-right (as-of-right):** Lowest risk/fastest — multifamily permitted and program fits base zoning. Preferred.
- **Administrative (site plan / minor variance):** Moderate — staff-level approvals.
- **Discretionary (rezoning / PUD / conditional use / variance / comp-plan amendment):** Highest risk — public hearings, political/community process, uncertain timing and outcome. Structure site control to **close subject to entitlements** and budget time/cost accordingly (underwriting model §8 schedule).

Check the **comprehensive/future land-use plan** alignment, recent rezoning track record in the jurisdiction, and any moratoria, concurrency, or impact-fee changes.

---

## 4. Owner / entity research (who, and how motivated)

Turn `ownerName` / `ownerName2` / `mailAddress` / `absenteeOwner` / `lastSaleDate` / `previousOwner` into a contact and a motivation read.

### 4.1 Pierce the entity (LLC/LP/Trust → real people)

- **Secretary of State business registry** (state of formation/registration): look up the LLC/LP to find the **registered agent, principals/members/managers, organizer, and formation date**. Cross-reference the entity's principal-office address against `mailAddress`.
- **Linked-entity / portfolio mapping:** The same principals or registered agent across multiple entities reveal a **portfolio owner** (negotiate at the portfolio level; different motivation than a one-asset owner).
- **Property appraiser / deed registry:** Confirm vesting and pull the **recorded deed** for true sale price, terms, lender (mortgage/DOT), and grantor/grantee — fills the price gap Quarry's `lastSaleDate` leaves.
- **Trust/estate:** A trust or recently-inherited parcel (estate → heirs in `previousOwner`) often signals **motivated, unsophisticated, or time-pressured** sellers.

### 4.2 Motivation signals (rank outreach by these)

- **Absentee + long hold:** Out-of-area owner holding many years → tired-landlord / estate-planning / 1031 candidate. **Top priority.**
- **Long hold, large embedded gain:** Tax-deferral motive; a structured (installment/1031) deal can unlock.
- **Distress markers (pull separately):** tax delinquency, code violations, liens, pre-foreclosure/lis pendens, deferred maintenance → motivated, but diligence the liabilities.
- **Free-and-clear (no recent mortgage on deed):** More flexible on price/terms/seller-financing.
- **Recent purchase / new LLC:** Likely **not** a seller (or a flipper) — deprioritize for off-market acquisition.

### 4.3 Outreach posture

Use the cleanest contact path (principal via SoS over a "c/o" mail line), reference the specific parcel/APN, and tailor the pitch to the inferred motivation (estate/retirement vs. portfolio recycling vs. distress relief).

---

## 5. Additional data to pull (and from where) — the diligence layer

Quarry seeds the site; these third-party sources turn it into an underwritable thesis. Pull each with **source + date**.

| Data | Why it matters for multifamily dev | Where to pull (live) |
|---|---|---|
| **FEMA flood zone** | Flood-zone land is partly unbuildable, raises cost (fill/elevation), and mandates flood insurance; floodway is effectively no-build | **FEMA National Flood Hazard Layer / Flood Map Service Center** (geocode the situs/APN); confirm against local floodplain GIS |
| **Wetlands** | Wetlands trigger Army Corps (Section 404) permitting, mitigation cost, and reduce **net** buildable acreage | **USFWS National Wetlands Inventory**; require a field **wetlands delineation** before committing |
| **Environmental — Phase I triggers** | Prior industrial/gas-station/dry-cleaner/agricultural use can trigger contamination, cost, delay, and liability; lenders require Phase I | **EPA databases** (Superfund/NPL, RCRA, brownfields, UST), state environmental agency; commission a **Phase I ESA** (Phase II if RECs found). Cross-read `useDesc`/`previousOwner` for red flags |
| **Utilities & sewer/water capacity** | A site is undevelopable without adequate water, sewer, power, and stormwater capacity at the needed scale; capacity constraints and extension costs are deal-makers/breakers | **Local water/sewer authority** (capacity letters, tap/impact fees, moratoria), electric utility, civil engineer. Confirm gravity vs. pump-station sewer |
| **Topography / geotech** | Steep slopes, rock, poor soils, high water table raise sitework cost and cut yield | County/USGS topo & LiDAR GIS; **geotechnical report** for design |
| **Easements / ROW / encumbrances** | Utility/access/drainage easements reduce buildable area and constrain layout | **Title commitment** + current **ALTA survey** (definitive over `legalDescription`) |
| **School zones / attendance areas** | School quality is a major demand and rent driver for family-oriented suburban product | District GIS / attendance-zone lookups; ratings via state DOE / GreatSchools (context) |
| **Traffic counts (AADT)** | Visibility/access for retail-adjacent or corridor sites; arterial frontage helps lease-up and any retail component | **State DOT / MPO traffic-count maps** (AADT) |
| **Demographics & demand** | Population growth, household formation, income, renter share, age mix define the depth of the renter pool and supportable rent | **U.S. Census** (ACS for income/age/tenure, Building Permits Survey for supply, Population Estimates for growth); BLS (LAUS employment, QCEW wages); 1/3/5-mile rings around the situs |
| **Employment / economic drivers** | Job and wage growth underpin rent growth and absorption; major employer announcements move submarkets | BLS, state labor dept, EDC/Chamber announcements, news (Firecrawl) |
| **Rent & sale comps** | Validate achievable rents ($/unit, $/SF, concessions) and exit cap; the spine of the underwrite | Yardi Matrix / CoStar / RealPage + live comp shop; deed records & RCA/CoStar for sale/cap comps |
| **Supply pipeline** | Units under construction/permitted within the submarket determine lease-up and stabilized-vacancy risk | Yardi/CoStar pipeline; Census Building Permits; planning-department approvals |
| **Crime / safety context** | Perceived safety affects lease-up and rent | Local crime data portals (context, caveat reliability) |
| **Entitlement/comp-plan status** | Future land-use designation, overlays, recent rezonings, moratoria | Municipal planning dept & GIS; comp/future land-use plan |

---

## 6. Parcel-to-Pursuit Checklist

Work top to bottom; kill early on a fatal flaw. Capture **source + date** for every line.

**A. Identify & confirm the parcel**
- [ ] Record `apn`; confirm `county` and whether inside a **municipal boundary/ETJ** (sets zoning + tax authority).
- [ ] Reconcile `acreage` ↔ `lotSqft` (×43,560); flag discrepancies.
- [ ] Map adjacency — any contiguous `apn`s under same/related `ownerName` (assemblage)?
- [ ] Geolocate `situsAddress` (or APN centroid for raw land).

**B. Zoning & buildable program**
- [ ] Decode `zoning`/`zoningType` against the **live ordinance/GIS** (use, density, FAR, height, setbacks, parking, coverage, open space, overlays).
- [ ] Compute buildable units (density method **and** FAR/envelope method → take lesser; haircut for setbacks/parking/open space); express as a range with the binding constraint named.
- [ ] Confirm parking strategy physically fits (surface vs. structured).
- [ ] Classify entitlement path: by-right / administrative / discretionary → estimate time & risk.
- [ ] Check comprehensive/future land-use plan alignment and any moratoria/concurrency.

**C. Owner & motivation**
- [ ] Read `absenteeOwner`, hold length (today − `lastSaleDate`), `ownerName` type, `previousOwner` (estate?).
- [ ] Pierce entity via **Secretary of State** (principals, agent, linked portfolio).
- [ ] Pull recorded **deed** (price/terms/lender) and check free-and-clear vs. leveraged.
- [ ] Score motivation; set outreach priority and tailored pitch.

**D. Site diligence (fatal-flaw screen)**
- [ ] FEMA **flood** zone / floodway.
- [ ] **Wetlands** (NWI; plan a delineation).
- [ ] **Environmental** red flags (`useDesc`/`previousOwner` + EPA/state DBs → Phase I).
- [ ] **Utilities/sewer/water capacity** + tap/impact fees + moratoria (capacity letters).
- [ ] **Topo/geotech**, easements/ROW (title + ALTA survey).
- [ ] Compute **net** developable acreage after all deductions; re-run buildable units if it moved.

**E. Market & demand**
- [ ] Demographics (1/3/5-mile rings: growth, income, renter share, age) — Census.
- [ ] Employment/economic drivers — BLS + local EDC.
- [ ] Rent comps ($/unit, $/SF, concessions) + supply pipeline — Yardi/CoStar + comp shop.
- [ ] School zones, traffic counts, safety context as relevant to product type.
- [ ] Sale/cap comps for the exit — deed records + RCA/CoStar/broker BOVs.

**F. Underwrite & decide**
- [ ] Land $/unit and $/buildable-SF; **residual land value** (max supportable price).
- [ ] Feed into the underwriting model (revenue, OpEx incl. **tax reassessment at stabilization**, budget, schedule, returns).
- [ ] Compute untrended/trended yield-on-cost and **development spread vs. exit cap**; IRR, multiple, DSCR/debt yield.
- [ ] Run sensitivities (rent × cap, cost × rent, rate × cost) and break-evens.
- [ ] **Citation pass:** every figure carries source + date; flag assumptions.
- [ ] Go / no-go / control-and-entitle decision with the binding risks named and mitigants assigned.

---

*End of property-data-dictionary.md. Parcel records are administrative inputs — verify load-bearing facts against deeds, GIS, survey, and site work; every figure in any deliverable must carry a source and date.*
