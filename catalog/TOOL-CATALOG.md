# Underwriter OS — Tool Catalog (connectors, configured)

The complete, prioritized set of tools that power Underwriter OS. Everything here is real and verified as of June 2026. Two kinds of tools:

- **First-party Claude connectors** — added in the desktop app under **Settings → Connectors**, log in once, done. Safe for any user at your firm.
- **Community MCP servers** — open-source tools from GitHub (see `GITHUB-PACK.md`). More powerful for real estate, but they need a technical person (an IT teammate, or a helper) to set up once. NOT for first-time basic users.

> **The golden rule for basic users (non-technical staff):** you only ever need **Tier 0** and the one-click connectors in **Tier 1**. Everything below that is optional power you can add later.

---

## TIER 0 — Works instantly, nothing to set up
| Tool | What it does | Used by |
|---|---|---|
| **Claude web search** (built in) | Live web research, no account | every play, esp. deep-research |
| **Anthropic document skills** (docx/xlsx/pptx/pdf) | Produce real Word/Excel/PowerPoint/PDF deliverables | deal-memo, market study |

This alone runs all seven Underwriter OS plays. Start here.

---

## TIER 1 — Free / free-tier, one-click, high impact (recommended for everyone)
| Connector | What it does for your firm | Cost | Powers |
|---|---|---|---|
| **Tavily** | Deep, source-cited web research built for AI | Free tier | deep-research, market-comp, underwriting |
| **Exa** | Neural web search — finds niche sources, competitors, submarket intel | Free tier | deep-research, site-selection, investor-sourcing |
| **Google Drive** | Read/write where your firm's docs live; save deliverables | Free w/ Google | deal-memo, all |
| **Gmail** | Pull/draft deal correspondence, investor outreach context | Free w/ Google | investor-sourcing, pipeline |
| **Google Calendar** | Deadlines, IC meetings, site-visit scheduling | Free w/ Google | deal-pipeline |
| **Slack** | Team updates, pipeline summaries posted to channels | Free tier | deal-pipeline |
| **Notion** | If your firm keeps notes/wikis there — read/write deal knowledge | Free tier | all |

**How to connect any of these:** Claude desktop → **Settings → Connectors** → find it → **Connect** → sign in once.

---

## TIER 2 — Paid power-ups (connect the ones your firm already pays for)

### Real estate data (the big one)
| Connector | What it does | Notes |
|---|---|---|
| **Yardi Matrix** | Multifamily market intelligence: property search, rents, supply pipeline, **owner lookup** (`search_by_owner`) | First-party Claude connector. THE pick if your firm subscribes. Powers site-selection, market-comp, investor/owner sourcing |
| *(community MCPs: Census, Zillow, ATTOM, RentCast, Maps — see `GITHUB-PACK.md` §real-estate)* | Demographics, comps, parcel/AVM, geocoding | Need technical setup; great free/low-cost data |

### Finance & market data
| Connector | What it does | Notes |
|---|---|---|
| **Morningstar** | Investment & market insights | First-party |
| **Financial Modeling Prep (FMP)** | Broad market/company financial data | First-party |
| **S&P Global** | S&P datasets (capital, ratings, company info) | First-party |
| **FactSet** | Institutional financial data & analytics | First-party, enterprise |
| **Fitch Solutions** | Credit intelligence, ratings, research | First-party, enterprise |
| **Bigdata.com** | Real-time financial data & company tearsheets | First-party |
| **Quartr** | Company research, events, filings | First-party |
| *(community: SEC EDGAR, FRED, Alpha Vantage — see `GITHUB-PACK.md` §finance)* | Filings, Treasury/CPI/mortgage rates, markets | Free, technical setup |

### Investor / capital-partner / company & owner research
| Connector | What it does | Use |
|---|---|---|
| **CB Insights** | Private-company & investor intelligence | Who's active, who funds deals |
| **Harmonic** | Enrich companies and people | Capital-partner profiles |
| **Apollo** | B2B contact & company database | Investor contact (business data) |
| **ZoomInfo** | B2B company & contact intelligence | Investor sourcing |
| **Clay** | Data enrichment/orchestration across sources | Building target lists |
| **Lusha** | B2B contact enrichment | Contact for a firm |
| **Sumble** | Deep research on accounts, people, tech | Background on a partner |
| **Phoenix by HG Insights** | B2B firmographic/technographic data | Company intel |

> These cover capital-partner, company, owner, and contact research. For property-owner lookup and contact, Underwriter OS also uses its own Quarry engine (`quarry-parcels`).

### Documents, CRM, ops (connect what your firm uses)
| Connector | What it does | Category |
|---|---|---|
| **HubSpot** | CRM — investors, deals, contacts | CRM |
| **DocuSign** | E-signature for LOIs, agreements | Docs |
| **QuickBooks** / **Xero** | Accounting/financials | Finance ops |
| **Canva** | Investor decks, marketing visuals | Design |
| **Asana** / **ClickUp** / **Monday** / **Linear** | Project & development task management | PM |
| **Airtable** | Deal trackers / structured databases | PM/data |
| **Box** / **Dropbox** / **OneDrive** | Document storage (confirm availability in Settings) | Storage |
| **Salesforce** | CRM (confirm availability in Settings) | CRM |
| **CoCounsel Legal** / **Midpage** | Legal deep research (title/contract questions) | Legal |

*(Items marked "confirm availability" are common connectors I did not directly verify in the registry this session — check Settings → Connectors; if absent, a community MCP exists.)*

---

## Which connector powers which play
| Play | Tier 0 (always) | Best upgrades |
|---|---|---|
| **deep-research** | web search | Tavily, Exa |
| **site-selection** | web search | Yardi Matrix, Census MCP, Maps MCP, Exa |
| **market-comp-analysis** | web search | Yardi Matrix, RentCast/Zillow MCP, Census MCP |
| **investor-sourcing** | web search | CB Insights, Harmonic, Apollo, ZoomInfo, Clay; Yardi `search_by_owner` + SEC EDGAR for entity/owner |
| **underwriting-research** | web search | FRED (rates), Census (incomes/rents), Yardi, Morningstar/FMP |
| **deal-memo** | doc skills | Google Drive, Canva, DocuSign |
| **deal-pipeline** | local file | HubSpot, Airtable, Slack, Google Calendar |

---

## Setup priority (do in this order)
1. **Tier 0** — already on. Confirm web search works.
2. **Tavily + Exa** — 5 minutes, free, biggest research jump.
3. **Google Drive + Gmail + Calendar** — if your firm is on Google Workspace.
4. **Yardi Matrix** — if your firm subscribes (huge for RE).
5. **One investor-research tool** (Apollo or CB Insights) when a raise is active.
6. **Community MCP servers** (Census/SEC/FRED/Maps) — have a technical teammate set these up from `GITHUB-PACK.md`; they're free and powerful but not a basic-user task.

*All connector availability/names current as of June 2026. Verify in Settings → Connectors, which is the live source of truth.*
