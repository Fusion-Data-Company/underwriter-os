# Underwriter OS — Power Layer Config Guide (for a technical helper)

This sets up the **community MCP servers** (real estate, finance, research, maps) that go beyond Claude's one-click connectors. Basic office users do **not** do this — it's for the power rig. Every run command below was verified from each project's own README (June 2026).

## TL;DR (3 commands)
```bash
cp config/.env.example config/.env     # then edit config/.env, paste your keys
bash config/setup.sh                   # installs only what your keys + runtimes allow
# Fully quit Claude Desktop (Cmd+Q) and reopen
```
`setup.sh` backs up your existing config, only wires up servers whose key+runtime are present, and never overwrites an unreadable config.

---

## Prerequisites (install once)
| Runtime | Needed for | Install |
|---|---|---|
| **Node.js 20+** (`npx`) | Tavily, Exa, Firecrawl, Google Maps | https://nodejs.org |
| **uv** (`uvx`) | OpenStreetMap, Alpha Vantage | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| **Docker Desktop** | SEC EDGAR, FRED | https://www.docker.com/products/docker-desktop |

You don't need all three — install what matches the servers you want. `npx` + `uv` alone (no Docker) already gives you OSM, Tavily, Exa, Firecrawl, Maps, Alpha Vantage.

---

## The servers, configured (what each gives your firm + nuance)

### Free, no key
- **osm** (OpenStreetMap, `uvx osm-mcp-server`) — geocode site addresses, find nearby amenities, walkability/commute. Zero config. **Best free default.**
- **sec-edgar** (`docker … stefanoamorelli/sec-edgar-mcp`) — SEC filings, XBRL financials, insider data. Pull public REIT/competitor/lender financials and do **entity/ownership research**. *Nuance:* SEC requires a real identity — set `SEC_EDGAR_USER_AGENT="Name (email)"` in `.env`. The `-i` flag is mandatory (stdio); `setup.sh` handles it.

### Free key
- **fred** (`docker … stefanoamorelli/fred-mcp-server`) — Federal Reserve data: 30-yr mortgage rate, 10-yr Treasury, CPI, housing starts, home-price index — the macro inputs for underwriting. Key: https://fred.stlouisfed.org/docs/api/api_key.html
- **alphavantage** (`uvx marketdata-mcp-server <KEY>`) — markets/rates/economic indicators. *Nuance:* the package is `marketdata-mcp-server` (not the repo name) and the **key is a positional argument**, not an env var — `setup.sh` places it correctly. Key: https://www.alphavantage.co/support/#api-key

### Free tier (sign up; paid only for heavy use)
- **tavily** (`npx -y tavily-mcp@latest`) — deep, cited web research. *Nuance:* pre-tuned with `DEFAULT_PARAMETERS={"search_depth":"advanced","max_results":10}` for thorough research. Key: https://app.tavily.com/home
- **exa** (`npx -y exa-mcp-server`) — neural search for niche sources/competitors. (Exa also has a one-click Claude connector if you prefer that over the config.) Key: https://dashboard.exa.ai/api-keys
- **firecrawl** (`npx -y firecrawl-mcp`) — scrape/crawl broker sites, **city permit & planning portals**, comps pages. *Nuance:* pre-set retry (5 attempts) and a 2000-credit warning so you don't burn credits silently. Key: https://www.firecrawl.dev/app/api-keys

### Paid (Google Cloud; free monthly credit)
- **google-maps** (`npx -y @cablate/mcp-google-map --stdio`) — geocode, drive-times, nearby places for site analysis. *Nuance:* limited to `maps_geocode,maps_directions,maps_search_places` to keep it lean (edit `GOOGLE_MAPS_ENABLED_TOOLS` to add more). **Before use, enable "Places API (New)" + "Routes API"** in Google Cloud Console.

---

## Two servers that need a manual clone+build (advanced)
These have no drop-in registry runner — set up only if you want them.

### Census (official US Census MCP) — the best free demographics/rent/income data
```bash
git clone https://github.com/uscensusbureau/us-census-bureau-data-api-mcp
cd us-census-bureau-data-api-mcp
# requires Docker; one-time data seed:
docker compose --profile prod run --rm census-mcp-db-init sh -c "npm run migrate:up && npm run seed"
```
Then add to your Claude config (edit the path):
```json
"mcp-census-api": {
  "command": "bash",
  "args": ["/FULL/PATH/us-census-bureau-data-api-mcp/scripts/mcp-connect.sh"],
  "env": { "CENSUS_API_KEY": "YOUR_CENSUS_API_KEY" }
}
```
Census key (free): https://api.census.gov/data/key_signup.html

### Omnisearch (one server fronting Tavily/Brave/Kagi/Exa/Firecrawl)
```bash
git clone https://github.com/spences10/mcp-omnisearch
cd mcp-omnisearch && pnpm install && pnpm run build
```
```json
"omnisearch": {
  "command": "node",
  "args": ["/FULL/PATH/mcp-omnisearch/dist/index.js"],
  "env": { "TAVILY_API_KEY":"…", "EXA_API_KEY":"…", "FIRECRAWL_API_KEY":"…" }
}
```
Providers without keys are skipped automatically. Use this *instead of* separate Tavily/Exa/Firecrawl entries if you want a single search tool.

---

## Verify it worked
1. Fully quit Claude Desktop (Cmd+Q) and reopen.
2. Ask Claude: **"what tools do you have now?"** — the new servers should appear.
3. Test one: *"Use OpenStreetMap to geocode [an address you care about]."*

## Troubleshooting
- **Server not showing:** you must fully quit (Cmd+Q), not just close the window.
- **"npx/uvx/docker not found":** install the runtime (table above), reopen Terminal, re-run `setup.sh`.
- **Docker servers fail:** make sure Docker Desktop is actually running.
- **Key rejected:** re-check the key in `config/.env`, re-run `setup.sh` (it re-merges), restart Claude.
- **Want to undo:** your previous config was saved as `claude_desktop_config.json.backup.<timestamp>` in `~/Library/Application Support/Claude/` — rename it back.
- **Config location:** `~/Library/Application Support/Claude/claude_desktop_config.json`

*All run commands verified from upstream READMEs June 2026. Open-source projects change — re-check if a server stops working.*
