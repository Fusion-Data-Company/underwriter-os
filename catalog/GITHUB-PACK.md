# Underwriter OS — GitHub Pack (repos Claude pulls from)

Curated, **verified** public GitHub repos that extend Claude for institutional real-estate teams. Every repo below was confirmed to exist via the GitHub API on **2026-06-22** (HTTP 200), with live star counts and last-push dates. Archived repos are flagged.

## Two ways Claude uses these
1. **Knowledge / skills repos** — Claude can read or `git clone` these into a local `knowledge/` folder to learn patterns, reuse skills (e.g., Anthropic's document skills), and discover new connectors. No service account needed.
2. **MCP servers** — installable tools. A technical person (an IT teammate or a helper) runs/adds them once; then they appear to Claude like any connector. Many target real estate data Claude can't otherwise reach.

> **Who sets these up:** Knowledge repos = safe for anyone (Claude just reads them). MCP servers = technical setup; queue these for a technical teammate, not for first-time basic users.

---

## 1. MCP directories & official servers — *knowledge repos*
| Repo | ⭐ | Updated | What you get |
|---|--:|---|---|
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | 87,554 | 2026-06-17 | Official + community MCP index — the trust anchor for sourcing any connector |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | 89,596 | 2026-06-19 | Largest, freshest MCP directory — discover any future tool |
| [appcypher/awesome-mcp-servers](https://github.com/appcypher/awesome-mcp-servers) | 5,622 | 2026-05-06 | Well-categorized cross-reference list |
| [wong2/awesome-mcp-servers](https://github.com/wong2/awesome-mcp-servers) | 4,179 | 2026-06-13 | Cleaner opinionated shortlist |

## 2. Claude skills & CLAUDE.md patterns — *knowledge/skills repos*
| Repo | ⭐ | Updated | What you get |
|---|--:|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | 153,848 | 2026-06-09 | **Anthropic's official Agent Skills** incl. reference docx/xlsx/pptx/pdf skills — the cleanest path to polished memos/models |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 65,521 | 2026-05-22 | Huge curated skills/workflow collection |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 47,045 | 2026-04-27 | Canonical list of skills, hooks, slash-commands, CLAUDE.md patterns |
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 13,644 | 2026-04-28 | Curated Claude Skills directory with install guidance |
| [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | 2,145 | 2026-05-12 | Toolkit + a SKILL.md linter for authoring your firm's own skills |

## 3. Real estate / property / demographics — *MCP servers (technical setup)*
| Repo | ⭐ | Updated | Notes |
|---|--:|---|---|
| [uscensusbureau/us-census-bureau-data-api-mcp](https://github.com/uscensusbureau/us-census-bureau-data-api-mcp) | 80 | 2026-03-13 | **OFFICIAL U.S. Census MCP** — ACS demographics, income, rent, housing by tract/ZIP. Free (Census key). Core site-selection data. |
| [agentic-ops/real-estate-mcp](https://github.com/agentic-ops/real-estate-mcp) | 41 | 2025-10-13 | Reference RE MCP (listings, market analysis) — good self-host base; sample data |
| [sap156/zillow-mcp-server](https://github.com/sap156/zillow-mcp-server) | 45 | 2025-05-08 | Property search + Zestimates (RapidAPI key). Quick comps. Mind Zillow ToS |
| [nkbud/mcp-server-attom](https://github.com/nkbud/mcp-server-attom) | 2 | 2025-07-20 | ATTOM property data (parcels, AVM, sales hist). Low adoption — fork & self-host if your firm licenses ATTOM |
| [robcerda/rentcast-mcp-server](https://github.com/robcerda/rentcast-mcp-server) | 1 | 2025-07-01 | RentCast AVMs/rent comps. Near-zero stars — vet before relying |

> **Honest read:** the property/parcel MCP space is still early. The **official Census server** is the only high-confidence pick; the Zillow/ATTOM/RentCast wrappers are low-star and best treated as fork-and-self-host reference code. For licensed pro data, **Yardi Matrix (first-party connector)** beats all of these.

## 4. Web research / scraping — *MCP servers*
| Repo | ⭐ | Updated | Notes |
|---|--:|---|---|
| [firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server) | 6,651 | 2026-06-22 | Best-in-class scrape/crawl/extract — broker sites, city permit/planning portals, comps. Paid key |
| [exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server) | 4,605 | 2026-06-22 | Official Exa neural search (also a first-party connector). Paid key, free tier |
| [tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp) | 2,130 | 2026-06-21 | Official Tavily search+extract (also first-party). Paid key, free tier |
| [spences10/mcp-omnisearch](https://github.com/spences10/mcp-omnisearch) | 328 | 2026-06-21 | One server unifying Tavily/Brave/Kagi/Exa/Firecrawl — use whichever keys you have |

## 5. Finance / macro data — *MCP servers (mostly free)*
| Repo | ⭐ | Updated | Notes |
|---|--:|---|---|
| [stefanoamorelli/sec-edgar-mcp](https://github.com/stefanoamorelli/sec-edgar-mcp) | 321 | 2026-06-22 | SEC filings, XBRL financials, insider data — public REIT/competitor/lender financials + **entity research**. Free |
| [stefanoamorelli/fred-mcp-server](https://github.com/stefanoamorelli/fred-mcp-server) | 103 | 2026-05-16 | FRED — Treasury yields, CPI, housing starts, mortgage rates for underwriting. Free key |
| [lzinga/us-gov-open-data-mcp](https://github.com/lzinga/us-gov-open-data-mcp) | 103 | 2026-06-11 | 40+ US gov data APIs / 250+ tools (Treasury, FRED, BLS, Congress). Free |
| [alphavantage/alpha_vantage_mcp](https://github.com/alphavantage/alpha_vantage_mcp) | 175 | 2026-06-22 | Equities/FX/rates/economic indicators. Free tier key |

## 6. Document generation (memos / models / decks)
| Repo | ⭐ | Updated | Notes |
|---|--:|---|---|
| [anthropics/skills](https://github.com/anthropics/skills) | 153,848 | 2026-06-09 | **Use this first** for docx/xlsx/pptx/pdf — no API key, maintained |
| [haris-musa/excel-mcp-server](https://github.com/haris-musa/excel-mcp-server) | 3,949 | 2026-04-12 | Create/edit .xlsx (formulas, charts) — underwriting models, rent rolls. MCP server |
| [GongRzhe/Office-Word-MCP-Server](https://github.com/GongRzhe/Office-Word-MCP-Server) | 2,062 | 2025-12-31 | ⚠️ **ARCHIVED** (read-only). Word .docx generation — usable but unmaintained; prefer anthropics/skills |
| [GongRzhe/Office-PowerPoint-MCP-Server](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server) | 1,805 | 2025-12-31 | ⚠️ **ARCHIVED**. .pptx decks — usable but unmaintained; prefer anthropics/skills |

## 7. Maps / geocoding — *MCP servers*
| Repo | ⭐ | Updated | Notes |
|---|--:|---|---|
| [google/mcp](https://github.com/google/mcp) | 4,225 | 2026-06-19 | Google's official MCP hub. Paid key |
| [cablate/mcp-google-map](https://github.com/cablate/mcp-google-map) | 356 | 2026-04-21 | Geocode (batch 50), places, directions, drive-times — site address → coords/commute. Paid key |
| [jagan-shanmugam/open-streetmap-mcp](https://github.com/jagan-shanmugam/open-streetmap-mcp) | 202 | 2025-07-12 | **Free, no key** OSM geocoding/nearby — good default |
| [googlemaps/platform-ai](https://github.com/googlemaps/platform-ai) | 102 | 2026-06-05 | Official Google Maps Platform MCP (docs-grounded). Paid key |
| [NERVsystems/osmmcp](https://github.com/NERVsystems/osmmcp) | 24 | 2026-03-20 | Precision OSM routing/walkability near sites. Free |

## 8. Legitimate entity / business-data (OSINT-adjacent) — *index*
| Repo | ⭐ | Updated | Notes |
|---|--:|---|---|
| [soxoj/awesome-osint-mcp-servers](https://github.com/soxoj/awesome-osint-mcp-servers) | 257 | 2026-06-15 | Vetting catalog of OSINT/business-intel MCPs (OpenCorporates/SEC/RDAP-based). Use for **entity/LLC ownership** research from public sources. |

> For owner/entity research: SEC EDGAR (§5), Yardi `search_by_owner`, county records, the public-records servers indexed above, and your firm's own connected parcel data source (e.g. Quarry).

---

## The "full real estate power setup" (for a technical helper)
Install these MCP servers to max out Underwriter OS beyond first-party connectors:
1. **Census MCP** (free) — demographics/rents/incomes for every market.
2. **SEC EDGAR MCP** (free) — REIT/competitor/lender financials + entity research.
3. **FRED MCP** (free) — interest rates, CPI, housing starts for underwriting.
4. **OpenStreetMap MCP** (free) — geocoding/commute/walkability, no key.
5. **Firecrawl MCP** (paid key) — scrape broker & city-planning sites for comps and pipeline.
6. **Omnisearch MCP** (paid keys) — one front door to Tavily/Exa/Brave/Firecrawl.

Each repo's README has setup steps. Underwriter OS's `knowledge-packs` skill walks Claude through recommending and (where the user has the access) installing these.

*Every repo verified 2026-06-22. Re-check before install; open-source projects change.*
