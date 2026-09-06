# Multifamily Underwriting Model — Reference

**Scope:** Ground-up Class A multifamily development and value-add acquisitions — adapt scope/geography to your firm. This document is the canonical underwriting reference for Underwriter OS. It defines every metric used in a deal, the exact formula, why it matters, the typical drivers, and **where to source each input live**.

---

## 0. How to use this document (and the citation standard)

Underwriter OS pulls **live** data. Do **not** treat any dollar figure, rate, or cap rate in this document as a current fact — illustrative ranges are labeled **"illustrative — verify live."** Every input must be sourced at run time.

**Citation standard (non-negotiable).** Every figure in any deliverable — a number in a memo, a cell in a model, a line in a table — must carry:
1. **Source** (e.g., "Yardi Matrix," "FRED series DGS10," "Davidson County Assessor," "CBRE Cap Rate Survey H2," "contractor GMP bid 2026-05-14").
2. **As-of date** of the data point.
3. **Pull method** when programmatic (API/series ID, scrape target, file name).

If a figure cannot be sourced, label it **ASSUMPTION** and state the basis. Never present an unsourced number as fact. A deliverable with uncited numbers is not done.

**Live-source quick map (used throughout):**

| Data class | Primary live sources |
|---|---|
| Interest rates / macro | FRED (DGS10 = 10yr UST, DGS2, SOFR = `SOFR`, T10Y2Y, MORTGAGE30US, FEDFUNDS), CME Term SOFR, Treasury.gov |
| Market rents / occupancy / supply | Yardi Matrix, CoStar, RealPage/Apartments.com, market-comp play (live comp shop), Census ACS for context |
| Cap rates / sales comps | CBRE/JLL/CoStar/RCA (MSCI Real Capital Analytics) cap rate surveys, broker BOVs, county deed records |
| Construction costs | Contractor/GC budgets & GMP bids (authoritative), RSMeans, Turner/Mortenson cost indices, ENR Construction Cost Index, Firecrawl of trade/supplier sources, BLS PPI for materials |
| Property taxes | County assessor (assessed value, ratio), county/municipal millage/levy ordinances, state DOR |
| Insurance | Broker quotes (authoritative), reinsurance trend commentary (e.g., Marsh/Aon), state DOI rate filings |
| Demographics / demand | U.S. Census (ACS, Building Permits Survey, Population Estimates), BLS (LAUS employment, QCEW wages), local MPO traffic counts |
| Entitlement / zoning | Municipal zoning ordinance & GIS, county GIS parcel layer, planning department |

---

## 1. Revenue (the rent roll → Effective Gross Income)

Revenue is built bottom-up from the unit mix. Underwrite **in-place** (T-12 / current rent roll) and **market/pro-forma** side by side; the gap is the value-add thesis.

### 1.1 Revenue waterfall (the canonical order of operations)

```
Gross Potential Rent (GPR, at market)
  – Loss-to-Lease (LTL)
  = Gross Scheduled Rent (in-place contract rent)
  – Vacancy loss (physical)
  – Concessions
  – Bad debt / credit loss
  – Non-revenue / model / employee units
  = Net Rental Revenue
  + Other Income (RUBS, parking, fees, etc.)
  = Effective Gross Income (EGI)
```

### 1.2 Gross Potential Rent (GPR)

- **Definition:** The total rent the property would collect if 100% occupied at **market** rents for the unit mix, annualized.
- **Formula:** `GPR = Σ (units of type i × market rent_i × 12)`
- **Why it matters:** The ceiling on rental revenue; the denominator for loss-to-lease and economic occupancy.
- **Drivers:** Unit mix (studio/1BR/2BR/3BR), unit size (SF), finish level, submarket rent, amenity premium, micro-location (views, floor).
- **Source live:** Market rents from the **market-comp play / Yardi Matrix / CoStar**; corroborate with a live comp shop (call/scrape 4–8 truly competitive properties for asking rent, concessions, availability) within the same submarket and vintage. Unit mix from the rent roll (acquisitions) or the architectural unit-mix schedule (development).

### 1.3 Loss-to-Lease (LTL)

- **Definition:** The gap between market rent and in-place contract rent across occupied units (leases signed below today's market).
- **Formula:** `LTL = GPR(market) – Gross Scheduled Rent(in-place)` ; as a % `= LTL / GPR`.
- **Why it matters:** A large positive LTL is embedded upside that rolls to market on renewal/turn — central to value-add. A negative LTL (gain-to-lease) means in-place rents exceed current market (a warning that asking rents are softening).
- **Drivers:** Speed of recent market rent growth, lease term/expiration schedule, renewal vs. new-lease spread, prior management's pricing discipline.
- **Source live:** In-place rents from the **rent roll**; market rents from the comp set. Track lease expiration schedule to model the roll-to-market pace.

### 1.4 Vacancy — physical vs. economic

- **Physical vacancy:** Share of **units** unoccupied. `Physical vacancy % = vacant units / total units`. Physical **occupancy** = 1 – that.
- **Economic vacancy:** Share of **potential revenue** not collected for ANY reason (vacancy + concessions + bad debt + non-revenue units + LTL on a market basis).
  - `Economic occupancy = Net Rental Revenue / GPR`
- **Why it matters:** Economic occupancy is the honest number — a property can be 95% physically occupied but collect far less economically due to concessions/delinquency. Lenders and buyers underwrite **economic**.
- **Drivers:** Submarket supply/absorption, seasonality, management quality, concession environment, screening standards (affects bad debt), unit-down/renovation downtime.
- **Underwriting convention:** For stabilized Class A, a **physical vacancy / general vacancy allowance** in the low-to-mid single digits is typical; use a **stabilized economic vacancy** that also absorbs concessions and credit loss. *Illustrative — verify live:* general vacancy assumptions commonly land around the mid-single-digit range for stabilized Class A, but this must be set from the live submarket (Yardi/CoStar submarket vacancy + your comp set).
- **Source live:** Submarket vacancy and absorption from **Yardi Matrix / CoStar**; property physical occupancy from the rent roll; new-supply pipeline (units under construction within the submarket radius) to stress lease-up and stabilized vacancy.

### 1.5 Concessions

- **Definition:** Rent given away to sign/renew leases — free weeks, look-and-lease specials, gift cards, waived fees.
- **Formula:** `Concession % = total concessions / GPR` (or expressed as weeks free ÷ 52).
- **Why it matters:** Concessions convert **face/asking rent** to **net effective rent**; lease-up and oversupplied markets run heavy concessions that crush real revenue even when asking rents look strong.
- **Drivers:** Lease-up phase, competitive new supply, seasonality (Q4/winter heavier in many Southeast markets), submarket softness.
- **Source live:** Live comp shop is the truth — ask each comp what they are **actually** offering this week. Yardi/CoStar report concession trends. During lease-up, model a concession burn-off curve.

### 1.6 Bad debt / credit loss

- **Definition:** Billed rent that is never collected (skips, evictions, write-offs).
- **Formula:** `Bad debt % = uncollected billed rent / GPR (or / Gross Scheduled Rent)`.
- **Why it matters:** Directly reduces EGI; post-2020 it has been structurally elevated and lumpy, and eviction timelines vary by state/county.
- **Drivers:** Resident credit profile / screening, local eviction law and court backlog, economic stress, asset class (Class A typically lower than B/C).
- **Source live:** Property operating statements / T-12 (acquisitions); for development, set from comparable lease-ups and submarket norms. Note state-specific eviction process timing.

### 1.7 Other income

Material to Class A economics; often **5–15% of EGI** *(illustrative — verify live)*. Build each line:

| Line | What it is | Source live |
|---|---|---|
| **RUBS / utility reimbursement** | Ratio Utility Billing System — recover water/sewer/trash (sometimes gas/electric in common areas) from residents | T-12 ledger; utility invoices; local statute on what's billable; comp set practices |
| **Parking** | Surface/covered/garage/reserved/EV | Comp set parking rates; site parking count vs. code |
| **Pet** | Pet rent + non-refundable fees/deposits | Comp set pet policy/rates |
| **Application & admin fees** | One-time at lease execution | Comp set; state caps |
| **Storage** | On-site storage units | Comp set; site program |
| **Amenity / package / tech** | Package lockers, valet trash, common-area WiFi, smart-home, amenity fees | Comp set; vendor contracts |
| **Late fees, lease-break, transfer** | Ancillary | T-12 |
| **Short-term / corporate / furnished premium** | If program allows | Comp set; local STR rules |

- **Why it matters:** High-margin, often grows faster than base rent; a real value-add lever (e.g., installing RUBS, adding paid parking/storage).
- **Caution:** Other income must be **sustainable and lease-supported** — one-time fees and aggressive RUBS recovery should be haircut for a conservative underwrite.

### 1.8 Net Effective Rent (NER), $/unit, $/SF

- **Net effective rent:** Face rent net of concessions amortized over the lease term.
  - `NER = (face rent × lease months – total concession value) / lease months`
- **$/unit:** `monthly rent / unit` — the headline comp metric.
- **$/SF:** `monthly rent / unit SF` — normalizes across unit sizes; the cleanest cross-comp metric. (Smaller units carry higher $/SF.)
- **Why they matter:** $/SF and NER let you compare your pro forma to the comp set apples-to-apples and detect when "asking rent" overstates reality.
- **Source live:** Comp set (asking + concessions → NER) from comp shop / Yardi / CoStar; SF from unit plans.

### 1.9 Trended vs. untrended revenue

- **Untrended:** Today's market rents held flat (the conservative "as-if-stable-today" view). **Untrended yield-on-cost is the primary development go/no-go screen.**
- **Trended:** Rents grown at an assumed annual rate from today to stabilization (recognizing that a development delivers in ~2–4 years).
- **Why it matters:** Development takes years; trending captures real growth but introduces forecast risk. Always show **both**; never justify a deal on trending alone.
- **Source live:** Rent-growth forecasts from Yardi Matrix / CoStar / CBRE-EA submarket forecasts; sanity-check against historical submarket CAGR and supply pipeline. State trend rate, source, and date.

---

## 2. Operating Expenses (OpEx)

Underwrite OpEx **per-unit** and as **% of EGI**, and benchmark every line against the comp set and the T-12. Split **controllable** (management can move) vs. **non-controllable** (taxes, insurance, utilities — largely exogenous).

### 2.1 Benchmark frame (qualitative — verify live)

Total stabilized OpEx for Class A commonly runs a meaningful share of EGI, with **taxes + insurance** often the two largest and fastest-growing lines in the Southeast. Do not anchor to a fixed ratio — derive from line-item build, then sanity-check the total per-unit and expense ratio against comps. *All ranges below are illustrative — verify live* against the T-12, comp set, and the sources noted.

| Line | Type | What it covers | Source live / benchmark method |
|---|---|---|---|
| **Payroll & benefits** | Controllable | On-site staff: manager, leasing, maintenance, make-ready; burdened with taxes/benefits | T-12; staffing plan by unit count; market wage data (BLS QCEW). Larger assets gain payroll efficiency per unit |
| **Repairs & Maintenance (R&M)** | Controllable | Day-to-day repairs, parts, minor supplies | T-12; rises with age/vintage; new construction lower early |
| **Contract services** | Controllable | Landscaping, pest, pool, elevator, janitorial, security, snow (rare in SE) | T-12; vendor contracts; comp set |
| **Turnover / make-ready** | Controllable | Paint, clean, flooring, repairs between residents | T-12; function of turnover rate × cost/turn |
| **Marketing & advertising** | Controllable | ILS (Apartments.com, Zillow), SEO/PPC, signage, locator fees | T-12; spikes during lease-up; per-unit or % of EGI |
| **General & Administrative (G&A)** | Controllable | Office, software (PMS/screening), legal/eviction, bank fees, telecom | T-12 |
| **Management fee** | Semi-controllable | Third-party PM fee | **% of EGI**, typically low-single-digit percent *(illustrative — verify live)*; from PM agreement / market standard |
| **Utilities (owner-paid)** | Non-controllable | Common-area + vacant-unit electric/gas/water/sewer/trash, net of RUBS recovery | T-12; utility tariffs; offset by RUBS in revenue |
| **Property taxes** | Non-controllable | See §2.3 — usually the **largest** single line | County assessor + millage (see §2.3) |
| **Insurance** | Non-controllable | Property/casualty/liability; named-storm/wind/hail exposure in SE | Broker quote (see §2.4) |
| **Replacement reserves** | Non-controllable (lender-required) | Capital reserve for roofs, HVAC, etc. | $/unit/yr; lender/agency requirement (see §2.5) |

### 2.2 Controllable vs. non-controllable — why the split matters

- **Controllable** expenses are where operational value-add lives (renegotiate contracts, right-size staffing, reduce turnover, sharpen marketing spend).
- **Non-controllable** (taxes, insurance, and to a degree utilities) are exogenous and have been the **primary OpEx inflation drivers in the Southeast**. A great operator cannot offset a tax reassessment or a hard insurance market — model these conservatively and independently.

### 2.3 Property taxes (the single most important OpEx line)

- **Definition:** Ad valorem tax = assessed value × assessment ratio × millage (mill levy), less abatements.
- **Formula:** `Annual tax = Assessed Value × Assessment Ratio × (Millage / 1000)` (mechanics vary by state; some states tax a % of market value directly).
- **Why it matters:** Usually the largest OpEx line and the **biggest pro-forma trap in development**: the property is taxed on land/partial value during construction, then **reassessed at or near completed/stabilized value** — a step-change that can dwarf the lease-up budget if not modeled.
- **Key methodology points:**
  - **Assessment methodology:** Assessors use cost, sales-comparison, and/or **income** approaches. For stabilized multifamily, many jurisdictions move toward an income-based assessment → your own NOI can drive your tax bill.
  - **Assessment ratio / equalization:** Some states assess at a fraction of market value; confirm the ratio for the specific county/state.
  - **Millage / levy:** Sum of overlapping jurisdictions (county + municipality + school district + special districts). Can change annually via budget/levy votes.
  - **Reassessment-at-stabilization risk:** Model taxes to **step up at certificate-of-occupancy/stabilization** to the assessor's likely view of completed value (often anchored to your sale value or income). Underestimating this is a classic way deals miss.
  - **Appeals:** Budget for a likely post-stabilization assessment appeal; many owners over-assessed at lease-up win reductions.
- **Incentives — abatements / PILOT / TIF (material in the Southeast):**
  - **Tax abatement:** Temporary reduction/exemption (often tied to affordable set-asides or downtown/opportunity-zone development). Model the abatement schedule **and the cliff** when it burns off.
  - **PILOT (Payment In Lieu Of Taxes):** A negotiated fixed payment replacing ad valorem tax for a term — common with housing authorities / IDBs in the SE; can be a major value driver. Model the PILOT payment and its expiration.
  - **TIF (Tax Increment Financing):** Incremental taxes from the new development fund district infrastructure; affects net carrying cost and sometimes site/offsite cost.
- **Source live:** **County assessor** (current assessed value, ratio, recent comparable assessments, reassessment cycle); **county/municipal millage ordinances** and **levy** history; **state Department of Revenue** for methodology; the city/county economic-development office for abatement/PILOT/TIF terms. State the assessor parcel basis, ratio, millage, and as-of date for every tax figure. For development, document the explicit step-up assumption and its trigger date.

### 2.4 Insurance (rising fast in the Southeast)

- **Definition:** Property (replacement cost), general liability, and excess/umbrella; in the SE, **named-storm/wind/hail (and sometimes separate flood)** drive cost and deductibles.
- **Why it matters:** Insurance has hardened dramatically and is now a top-three OpEx line in coastal and hail-exposed SE markets; deductibles (esp. **named-storm % deductibles**) and **insurance-to-value** requirements affect both expense and downside risk.
- **Drivers:** Replacement-cost valuation (construction-cost inflation pushes RCV up), catastrophe (wind/hail/flood) exposure by location, construction type (wood-frame vs. masonry/podium affects rate), roof age/type, loss history, reinsurance cycle, statewide market conditions.
- **Modeling notes:**
  - Underwrite on a **$/unit/yr** basis and verify against a real broker indication; do not use a stale per-unit figure.
  - Confirm **replacement cost** (not market value) drives the property limit; under-insuring triggers coinsurance penalties.
  - Capture **wind/hail and flood deductibles** separately (often % of insured value) for downside/sensitivity.
- **Source live:** **Broker quote/indication is authoritative** — obtain a marketed indication for the specific asset/location/construction type. Corroborate trend with reinsurance market commentary (Marsh/Aon/Gallagher) and state DOI filings. Use FEMA flood zone (see data dictionary) to flag flood-insurance need.

### 2.5 Replacement reserves

- **Definition:** Annual capital set-aside for long-lived component replacement (roofs, HVAC, parking, appliances).
- **Formula:** `Reserves = $/unit/yr × units`.
- **Why it matters:** Lenders/agencies **require** it; it should reflect real long-term capital need, not just the loan minimum. New construction can use a lower reserve early; aging assets need more.
- **Source live:** Agency/lender requirement (Fannie/Freddie set minimums) and a PCA (Property Condition Assessment) for acquisitions. State the basis.

---

## 3. NOI, expense ratio, breakeven occupancy

### 3.1 Net Operating Income (NOI)

- **Definition:** Property cash flow from operations before debt service, capital expenditures, income taxes, and depreciation.
- **Formula:** `NOI = EGI – Total Operating Expenses` (OpEx **excludes** debt service, capex, reserves-above-line treatment varies, and non-operating items).
- **Why it matters:** The single most important operating number — it drives value (NOI ÷ cap rate), debt sizing (debt yield, DSCR), and yield-on-cost.
- **Conventions:** Be explicit whether **reserves**, **management fee**, and **non-recurring items** are above or below the NOI line — inconsistency here is the most common source of bad comps. Common convention: management fee and reserves **above** the line (in OpEx) for a conservative, financeable NOI; document any deviation.
- **Source live:** Built from §1 and §2 — every component cited.

### 3.2 Expense ratio (OpEx ratio)

- **Definition:** Operating expenses as a share of EGI.
- **Formula:** `Expense Ratio = Total OpEx / EGI`. (Operating margin = NOI / EGI = 1 – expense ratio.)
- **Why it matters:** Fast sanity check on the underwrite; an out-of-range ratio vs. comps flags an aggressive (too low) or bloated (too high) expense model. New Class A trends lower early (low taxes/R&M), then normalizes.
- **Source live:** Compare to comp set and submarket norms (Yardi/CoStar operating data, broker OMs). State the comp basis.

### 3.3 Breakeven occupancy (economic breakeven)

- **Definition:** The physical/economic occupancy at which EGI exactly covers OpEx **plus debt service** (and reserves).
- **Formula:** `Breakeven Occupancy = (Operating Expenses + Annual Debt Service) / GPR` (add reserves if treated below NOI; use stabilized GPR).
- **Why it matters:** The core **downside** metric — how much occupancy can fall before the deal can't pay its bills. Lenders watch the cushion between breakeven and projected occupancy.
- **Drivers:** Leverage (higher debt → higher breakeven), expense load, rent level.
- **Source live:** Derived from the model; debt service from the loan terms (§7).

---

## 4. Development Budget (uses of funds)

Total Project Cost (TPC) = Land + Hard Costs + Soft Costs (+ Financing + Reserves). Build per-line, then express **$/unit** and **$/SF** (both **gross SF** and **net rentable SF**), and benchmark.

### 4.1 Budget structure

| Bucket | Line items | Source live |
|---|---|---|
| **Land** | Purchase price, closing, broker, title, survey, carry/option | Deed comps, broker, PSA; see land $/unit & $/buildable-SF in §4.3 |
| **Hard costs — building shell** | Foundation, structure, envelope, roof, MEP, interiors, vertical | **GC budget / GMP bid (authoritative)**, RSMeans, regional cost indices, ENR CCI |
| **Hard costs — sitework** | Grading, utilities to/through site, stormwater, paving, retaining, offsite improvements | Civil engineer estimate + GC; utility authority for capacity/extension |
| **Hard costs — amenities** | Pool, clubhouse, fitness, dog park, garages/parking structure | GC budget; comp amenity set |
| **Hard cost contingency** | Buffer on hard costs | % of hard cost (see §4.4) |
| **Soft costs — A&E** | Architecture, civil, structural, MEP, landscape, geotech, survey | Design contracts |
| **Soft costs — permits & fees** | Building permits, **impact/tap/connection fees**, plan review, inspections | Municipal fee schedules; utility authority — *impact fees can be very large per unit in growing SE jurisdictions* |
| **Soft costs — financing** | Loan origination/points, lender legal, appraisal, **interest reserve / construction-period interest**, rate cap/hedge | Lender term sheet; see §7 |
| **Soft costs — legal & org** | Entity formation, acquisition legal, financing legal, JV docs | Counsel estimate |
| **Soft costs — marketing & lease-up** | Branding, leasing center, model units, advertising during lease-up, pre-stabilization operating shortfall | Lease-up budget |
| **Soft costs — taxes/insurance during construction** | Property tax on land/WIP, builder's risk insurance | Assessor; builder's-risk broker quote |
| **Developer fee** | Sponsor compensation for development services | % of cost (commonly mid-single-digit % of TPC) *(illustrative — verify live)*; per JV/program |
| **Soft cost contingency** | Buffer on soft costs | % of soft cost |
| **FF&E / pre-opening** | Common-area furniture, operating supplies, startup | Vendor quotes |

### 4.2 Total Project Cost, $/unit, $/SF

- **Formula:** `TPC = Land + Hard + Soft`. `Cost/unit = TPC / units`. `Cost/GSF = TPC / gross SF`. `Cost/NRSF = TPC / net rentable SF`.
- **Why it matters:** $/unit and $/SF are the headline cost-discipline metrics; they're how you compare your basis to peer deals and to replacement cost, and they feed yield-on-cost.
- **Source live:** Each component cited; benchmark $/unit and $/SF against recent regional development comps and current cost indices (ENR CCI, Turner/Mortenson, RSMeans) with dates.

### 4.3 Land basis metrics

- **Land $/unit:** `land cost / planned units` — the cleanest land-pricing metric for multifamily (it self-adjusts for density).
- **Land $/buildable-SF:** `land cost / buildable (zoning-allowed) building SF` — ties land price to entitlement.
- **Land as % of TPC:** Sanity check; high land share pressures returns and demands higher density or rent.
- **Source live:** Land sale comps from county deed records / CoStar / brokers; buildable SF from the zoning analysis (FAR × lot area, or units-allowed × avg unit size + common areas) — see Property Data Dictionary.

### 4.4 Contingency

- **Definition:** Reserve for cost overruns and unknowns; separate **hard** (construction risk) and **soft** (design/fee/timing).
- **Convention:** A meaningful hard-cost contingency is standard (larger for complex/podium/structured-parking deals, smaller for stick-built garden); plus a soft-cost contingency. *Illustrative — verify live* against deal complexity, design completeness, and the GC's own contingency. Do not double-count GC contingency vs. owner contingency — track separately.
- **Why it matters:** Cost overruns and schedule slips are the top development risks; thin contingency is how good projects become distressed.

---

## 5. Returns & feasibility

### 5.1 Yield-on-Cost (Development Yield / Return on Cost)

- **Definition:** Stabilized NOI ÷ total project cost — the development analog to a cap rate.
- **Formula:** `Yield-on-Cost = Stabilized NOI / Total Project Cost`.
  - **Untrended YoC** uses today's rents (primary go/no-go screen).
  - **Trended YoC** uses stabilized (grown) rents.
- **Why it matters:** The core feasibility test for ground-up; compared against the market exit cap to compute the **development spread**.
- **Source live:** NOI from §1–3; TPC from §4. Show both untrended and trended.

### 5.2 Development spread (margin over cap)

- **Definition:** Yield-on-cost minus the market exit cap rate — the reward for taking development risk (you build to a yield above where stabilized assets trade).
- **Formula:** `Spread = Yield-on-Cost – Exit Cap Rate` (in basis points).
- **Why it matters:** The single cleanest development go/no-go. A thin spread means you are not being paid for construction, lease-up, and market risk. The required spread widens when costs/rates are volatile.
- **Convention:** A disciplined sponsor targets a healthy positive spread of stabilized development yield over the prevailing exit cap; the **required** spread should be set to current market risk conditions, not a fixed number. *Illustrative — verify live.*
- **Source live:** Exit cap from CBRE/JLL/RCA cap-rate surveys + broker BOVs for the specific submarket/vintage, dated; YoC from §5.1.

### 5.3 Stabilized value & profit

- **Stabilized value:** `Stabilized NOI / Exit Cap Rate`.
- **Development profit:** `Stabilized Value – Total Project Cost`.
- **Profit margin (return on cost):** `(Stabilized Value – TPC) / TPC`. (Equivalently the value created above basis.)
- **Why it matters:** The absolute and percentage payoff; pairs with IRR/multiple to judge whether the risk is worth it.
- **Source live:** Exit cap (dated, sourced); NOI and TPC as above.

### 5.4 Cap rate (for acquisitions and exit)

- **Definition:** `Cap Rate = NOI / Value (or Price)`. Inverse is the value multiple.
- **Why it matters:** Pricing benchmark for acquisitions and the exit assumption for development; small cap-rate moves swing value massively (cap-rate risk dominates long-hold value).
- **Source live:** Transaction comps and cap-rate surveys (CBRE/JLL/RCA/CoStar), broker BOVs — dated. **Exit cap should generally be set at or above entry/current cap (a conservative spread above going-in)** to reflect terminal uncertainty; justify any compression with evidence.

### 5.5 IRR (Internal Rate of Return) — levered & unlevered

- **Definition:** The discount rate that sets the NPV of all project cash flows to zero — the time-weighted return.
- **Formula:** Solve `0 = Σ CF_t / (1+IRR)^t` over the hold (negative equity outflows, operating cash flows, sale proceeds).
  - **Unlevered IRR:** On total project cash flows (no debt) — measures the asset.
  - **Levered IRR:** On equity cash flows after debt service and loan paydown/payoff — measures the equity return; amplified by leverage (and by risk).
- **Why it matters:** The headline return metric for equity and LPs; captures timing (early cash flow and a faster exit boost IRR).
- **Limitations:** IRR is sensitive to timing/exit assumptions and assumes reinvestment at the IRR; always pair with **equity multiple** (which IRR can flatter on short holds).
- **Source live:** Built from the full pro forma; exit value sourced (§5.3–5.4); debt terms (§7).

### 5.6 Equity Multiple (MOIC)

- **Definition:** Total cash returned to equity ÷ total equity invested.
- **Formula:** `Equity Multiple = Σ distributions / Σ equity contributions` (e.g., 2.0x = double your money over the hold, regardless of time).
- **Why it matters:** Measures **absolute** wealth creation; complements IRR (a high IRR on a quick flip can be a low multiple). LPs evaluate both.
- **Source live:** From the equity cash-flow schedule.

### 5.7 Cash-on-Cash (cash yield)

- **Definition:** Annual pre-tax cash flow after debt service ÷ equity invested.
- **Formula:** `CoC = (NOI – Annual Debt Service) / Total Equity Invested`.
- **Why it matters:** Current-income view for each year; for development it's near-zero/negative during construction and lease-up, then ramps post-stabilization. Income-oriented LPs care about stabilized CoC.
- **Source live:** NOI (§3), debt service (§7), equity (§7).

### 5.8 DSCR (Debt Service Coverage Ratio)

- **Definition:** NOI ÷ annual debt service — the lender's cash-flow cushion test.
- **Formula:** `DSCR = NOI / Annual Debt Service`. (1.0x = NOI exactly covers debt; below 1.0x = shortfall.)
- **Why it matters:** Primary debt-sizing constraint for stabilized/permanent loans; a minimum DSCR (commonly comfortably above 1.0x for agency perm) caps proceeds. Construction loans use an interest reserve instead during the no-cash-flow period.
- **Source live:** NOI from model; debt service and minimum DSCR from lender/agency term sheet (dated).

### 5.9 Debt Yield

- **Definition:** NOI ÷ loan amount — leverage-independent measure of lender risk (no rate/amortization noise).
- **Formula:** `Debt Yield = NOI / Loan Amount`.
- **Why it matters:** A key permanent/agency sizing constraint that protects lenders regardless of rate; in a low-cap, high-rate environment debt yield (not LTV or DSCR) is often the **binding** sizing test.
- **Source live:** NOI from model; minimum debt yield from lender term sheet (dated).

### 5.10 LTC / LTV

- **Loan-to-Cost (LTC):** `Loan / Total Project Cost` — governs **construction** loan sizing.
- **Loan-to-Value (LTV):** `Loan / Appraised (or stabilized) Value` — governs **permanent** loan sizing.
- **Why they matter:** Set the debt/equity split and therefore equity need and levered returns; construction lenders cap LTC, perm lenders cap LTV and often the binding constraint is the **lesser** of LTV, DSCR, and debt yield.
- **Source live:** Lender term sheets; value from appraisal/comps. State the constraint that actually binds.

### 5.11 Hold period & exit assumptions

- **Hold period:** Time from acquisition/groundbreaking to sale/refi (development: construction + lease-up + a stabilized seasoning period; value-add: through the business-plan execution).
- **Exit assumptions (state every one, sourced):** exit cap rate, terminal NOI (with one more year of growth/expense step-ups, taxes reassessed), selling costs (broker + transfer/closing), and whether exit is **sale** or **refi-and-hold**.
- **Why it matters:** Exit cap and terminal NOI dominate long-hold returns; small changes swing IRR/multiple more than operations.
- **Source live:** Exit cap and selling-cost norms from brokers/RCA; growth from forecasts — all dated.

### 5.12 Sensitivity & break-even analysis (mandatory)

No multifamily deal ships without sensitivity tables. Run two-variable grids and single-variable break-evens on the items deals are most sensitive to:

- **Rent** (achieved rent ±, and rent-growth rate ±) — vs. **exit cap** (the canonical 2-way table for value/IRR).
- **Construction / hard cost** (± per unit) — vs. **rent** or **exit cap**.
- **Interest rate / SOFR** (± bps on the construction and perm rate) — vs. **rent** or **cost**.
- **Lease-up pace / absorption** (units/month, ± months to stabilization) — vs. concessions.
- **Exit cap** (± bps) standalone — usually the highest-impact single variable.

**Break-evens to report:** break-even rent (rent at which YoC = required), break-even cost ($/unit at which spread = required), break-even exit cap (cap at which profit/IRR hits the hurdle), break-even occupancy (§3.3), and break-even interest rate (rate at which DSCR/debt yield fails).

- **Source live:** Sensitivity ranges should bracket the **live** rate/cap/cost environment (FRED for rates, surveys for caps, indices for cost), with the base case sourced and dated.

---

## 6. The 5–7 assumptions deals are most sensitive to

Rank-order, stress every one, and own the downside:

1. **Exit / terminal cap rate** — highest-impact single input on value and IRR; never assume compression. *(Source: cap-rate surveys + broker BOVs, dated.)*
2. **Construction / hard cost per unit** — overruns and a moving cost market can erase the entire spread. *(GC/GMP bids, ENR/RSMeans.)*
3. **Achieved rents & rent growth (trended)** — the revenue ceiling; oversupply and concessions hit here first. *(Comp shop, Yardi/CoStar.)*
4. **Interest rate / cost of debt (SOFR + spread)** — drives construction carry, perm sizing (debt yield/DSCR), and refi risk. *(FRED SOFR/DGS10, lender term sheets.)*
5. **Property taxes at stabilization (reassessment step-up)** — the biggest OpEx surprise in development. *(Assessor + millage; model the step-up.)*
6. **Insurance cost & deductibles** — hardening SE market; top-three expense with real downside (named-storm). *(Broker indication.)*
7. **Lease-up pace / absorption & stabilized vacancy** — slow absorption extends carry and burns interest reserve. *(Submarket absorption + supply pipeline, Yardi/CoStar.)*

---

## 7. Capital Stack

Order of priority (lowest cost/lowest risk at the bottom of the stack, paid first): **Senior debt → Mezzanine/Preferred equity → LP common equity → GP/Sponsor common equity.**

### 7.1 Construction loan (the senior development debt)

| Term | Typical structure | Source live |
|---|---|---|
| **Sizing** | Capped at **LTC** (lesser of LTC and a stressed take-out test) | Lender term sheet |
| **Rate** | Floating: **SOFR + spread**, sometimes with a floor; rate cap often required | FRED `SOFR` / CME Term SOFR + lender spread |
| **Term** | Construction period + lease-up/stabilization, often with extension options (fees, tests) | Term sheet |
| **Interest reserve** | Funded line within the loan to pay interest until the property cash-flows | Sized in the budget (§4.1) |
| **Recourse** | Often **partial/full recourse** or completion guaranty for merchant builders; **non-recourse carve-outs** (bad-boy) always | Term sheet; sponsor balance sheet |
| **Funding** | Draws against costs incurred (with title/lien waivers, inspections) | Lender draw process |
| **Covenants** | Completion guaranty, balancing (loan must stay "in balance"), pre-leasing tests for extension/take-out | Term sheet |

### 7.2 Permanent / take-out financing (agency for multifamily)

- **Definition:** Long-term loan that refinances the construction loan once stabilized — for multifamily, frequently **Fannie Mae / Freddie Mac (agency)** or HUD/FHA, sometimes life-co or CMBS.
- **Sizing constraints:** Lesser of **LTV**, **minimum DSCR**, and **minimum debt yield** at the perm rate. Agency offers attractive rates, often interest-only periods, and non-recourse.
- **Why it matters:** The take-out validates the construction loan and crystallizes the refi-vs-sale decision; **refinance risk** (rates/caps at stabilization) is a core development risk.
- **Source live:** Agency/lender term sheets and current agency spreads; perm base rate off FRED (DGS10) + spread, dated.

### 7.3 Equity — LP / GP

- **LP (limited partner) equity:** Majority of the equity (institutional/fund/HNW); passive; receives a **preferred return** and the majority of cash flow until the promote tiers.
- **GP / Sponsor equity:** Co-invest ("skin in the game"); earns the **promote/carried interest** for performance, plus fees (acquisition/development/asset-management).
- **Source live:** JV/operating agreement; market co-invest and promote norms.

### 7.4 Preferred return & the promote/waterfall

- **Preferred return ("pref"):** A priority return on equity (e.g., a fixed annual %) paid before the sponsor shares in profits; may be **cumulative** and/or **compounding**.
- **Promote / carried interest:** Sponsor's outsized share of profits above hurdles — the incentive for performance.
- **Waterfall (illustrative tier structure — actual hurdles/splits per the JV doc):**
  1. **Return of capital** — 100% to investors until contributed equity is returned.
  2. **Preferred return** — to investors until the pref hurdle (an IRR) is met.
  3. **Promote tier 1** — split shifts to the sponsor (e.g., a larger sponsor share) up to a second IRR hurdle.
  4. **Promote tier 2+** — sponsor share increases at each higher IRR hurdle (a "promote crystallization"/catch-up may apply).
- **Why it matters:** Determines how value is split; aligns sponsor and LP. The hurdle structure massively affects sponsor economics and LP net returns.
- **Source live:** The deal's operating agreement governs; benchmark hurdle/split norms to market, dated.

### 7.5 Mezzanine debt / Preferred equity (gap capital)

- **Mezzanine debt:** Subordinate loan secured by a pledge of the equity interests; higher rate than senior; fills the gap between senior debt and common equity.
- **Preferred equity:** Sits between mezz/senior and common; fixed preferred return, often with redemption rights; can be "hard" (debt-like) or "soft."
- **Why it matters:** Boosts leverage and equity returns but increases risk, fixed obligations, and intercreditor complexity; in a high-rate environment, expensive gap capital can wipe out the spread.
- **Source live:** Capital-markets quotes; intercreditor/standstill terms from counsel.

---

## 8. Schedule (the timeline drives the carry)

Time is cost: every month of delay burns interest reserve, taxes, insurance, and overhead, and pushes the exit. Model the schedule explicitly and tie cash flows to it.

| Phase | What happens | Typical driver / source live |
|---|---|---|
| **Predevelopment** | Site control (option/PSA), feasibility, market study, preliminary design, financing structuring | Internal; market study (Yardi/CoStar/3rd-party) |
| **Entitlement** | Zoning/rezoning, site plan approval, variances, platting, permits, impact-fee determination, community/political process | **Municipal planning department & ordinance** — the biggest schedule wildcard; varies hugely by jurisdiction |
| **Construction** | Sitework → vertical → finishes → CO; garden/stick-built is faster, podium/wrap/high-rise (concrete/steel) longer | GC schedule (authoritative); construction type |
| **Lease-up / absorption** | Leasing from first units delivered (often phased) to stabilized occupancy | **Absorption pace = units leased/month**, from comp lease-ups + submarket demand (Yardi/CoStar) |
| **Stabilization** | Reaching and seasoning at stabilized occupancy (e.g., a sustained high-occupancy threshold for a few months) | Definition per lender/agency; drives perm take-out timing |

- **Absorption / lease-up pace:** `Months to stabilize ≈ (units to lease at stabilization) / (net absorption units per month)`. Net absorption = gross leases − move-outs; in a competitive lease-up, concessions are the lever to hit pace. **Stress this**: slow absorption is a top-7 risk (extends carry, burns reserve).
- **Source live:** Construction duration from the GC; absorption from comparable recent lease-ups in the submarket and submarket net absorption (Yardi/CoStar), dated.

---

## 9. Key risks & mitigants framework

For each deal, populate this matrix; every risk gets an owner, a mitigant, and a residual rating.

| Risk | Why it bites | Mitigants |
|---|---|---|
| **Cost overrun** | Erases spread/profit | GMP contract, robust contingency, value-engineering, subcontractor bonding, buy-out before close, owner's rep/cost review |
| **Schedule delay** | Burns carry, delays exit | Realistic schedule with float, liquidated damages, early procurement of long-lead items, weather/permitting buffer |
| **Entitlement risk** | No project without approvals | Close subject to entitlements where possible; experienced local counsel/consultants; community engagement; as-of-right where feasible |
| **Lease-up / absorption** | Slow lease-up = shortfall | Conservative pace, supply-pipeline analysis, concession budget, phased delivery, marketing reserve |
| **Interest-rate / refi** | Higher carry; perm may not size | Rate caps/hedges, conservative perm sizing on stressed rates, debt-yield cushion, extension options |
| **Cap-rate expansion** | Lowers exit value | Conservative (de-compressed) exit cap, build-to-spread discipline, refi-and-hold optionality |
| **Tax reassessment** | OpEx step-up at stabilization | Model the step-up explicitly, pursue abatement/PILOT, budget for appeal |
| **Insurance** | Hardening SE market, named-storm | Real broker indication, resilient construction, appropriate deductibles, ITV compliance |
| **Supply (oversupply)** | Concessions, soft rents | Submarket pipeline screen, sub-market selection, differentiated product |
| **Construction defect / quality** | Litigation, capital cost | Reputable GC, inspections, warranties, retainage, latent-defect coverage |
| **Capital partner / liquidity** | Equity or debt falls through | Committed capital, multiple lender relationships, balanced loan, sponsor liquidity |
| **Environmental / site** | Cost, delay, liability | Phase I (and II if triggered), geotech, wetlands delineation early (see data dictionary) |

---

## 10. Model tab structure (Excel underwriting model outline)

A disciplined underwriting model should contain these tabs/sections, in this order. Inputs flow left-to-right; nothing hardcoded downstream of an input cell.

1. **Cover / Summary (one-page IC output)** — deal name, location, unit count, key metrics dashboard (untrended & trended YoC, spread, levered/unlevered IRR, equity multiple, stabilized CoC, profit, $/unit cost), go/no-go, **and a sources-&-dates block** (citation standard).
2. **Assumptions / Control Panel** — every key driver in one place (rents, growth, vacancy, OpEx growth, exit cap, costs, rate, leverage, timing). Each assumption cell labeled with **source + date**. This is the only place to change inputs.
3. **Unit Mix & Rent Roll** — unit types, count, SF, in-place rent, market rent, LTL; $/unit and $/SF; lease-expiration schedule (acquisitions).
4. **Revenue Pro Forma** — GPR → EGI waterfall (§1), in-place vs. stabilized; other-income build; concession/lease-up burn-off.
5. **Operating Expenses** — line-item OpEx (§2), per-unit and % EGI, controllable/non-controllable; tax build (assessment × ratio × millage, with stabilization step-up); insurance build; reserves.
6. **NOI & Returns Summary** — NOI, expense ratio, breakeven occupancy; yield-on-cost (untrended/trended), spread, stabilized value, profit/margin.
7. **Development Budget (Uses)** — land/hard/soft with contingencies; $/unit, $/GSF, $/NRSF (§4).
8. **Sources & Capital Stack** — construction loan (LTC, SOFR+spread, interest reserve), perm/agency take-out (LTV/DSCR/debt-yield sizing), LP/GP equity, mezz/pref (§7).
9. **Development & Lease-up Schedule** — phase timeline, draw schedule, absorption (units/month), stabilization date; ties to cash-flow timing (§8).
10. **Construction Draw / Funding Schedule** — monthly cost curve, debt-vs-equity funding order, interest-reserve burn.
11. **Cash Flow (Monthly during construction/lease-up; annual at stabilization)** — unlevered and levered; through sale/refi.
12. **Debt Schedule** — construction interest accrual/reserve burn, perm amortization/IO, refi event, payoff.
13. **Equity Waterfall** — capital accounts, pref accrual, promote tiers, LP/GP distributions, IRR/multiple by partner (§7.4).
14. **Returns** — unlevered & levered IRR, equity multiple, cash-on-cash by year, profit; partner-level returns.
15. **Sensitivities** — 2-way data tables (rent×cap, cost×rent, rate×cost) and break-even outputs (§5.12).
16. **Comps** — rent comps ($/unit, $/SF, concessions), sale/cap comps, land comps — each with **source + date**.
17. **Sources / Citations log** — master list of every external data point: figure, value, source, as-of date, pull method (enforces the citation standard).

---

*End of underwriting-model.md. All ranges herein are illustrative and must be verified against live sources at run time; every figure in any deliverable must carry a source and date.*
