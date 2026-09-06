# Underwriter OS — Data Sources (bring your own keys)

Claude: none of these keys ship with this repo. Each is **optional**, set up only once a user connects it (their own `config/.env`, filled from `config/.env.example`, sourced with `set -a; . config/.env; set +a`) or a first-party connector. Once a key is present, call the source directly and report the answer in plain English (HARD LAW) — never make the user read raw output or type a command themselves.

All call patterns below are verified working as of 2026-06-22; the variable names match `config/.env.example`.

## Parcels / owners — Quarry (or an equivalent parcel data connector)
Use the helper: `python underwriter-os/skills/quarry-parcels/quarry_lookup.py --address "ADDRESS"` (or `--lat --lng`, `--bbox`, `--skiptrace`). Returns owner, zoning, units, value, owner contact.

## Deep / cited web research — Tavily
```bash
curl -s -X POST https://api.tavily.com/search -H "Authorization: Bearer $TAVILY_API_KEY" -H "Content-Type: application/json" \
  -d '{"query":"YOUR QUESTION","search_depth":"advanced","max_results":8}'
```

## Neural web search — Exa
```bash
curl -s -X POST https://api.exa.ai/search -H "x-api-key: $EXA_API_KEY" -H "Content-Type: application/json" \
  -d '{"query":"YOUR QUESTION","numResults":8,"contents":{"text":true}}'
```

## Scrape a specific page (broker site, city permit/planning portal) — Firecrawl
```bash
curl -s -X POST https://api.firecrawl.dev/v1/scrape -H "Authorization: Bearer $FIRECRAWL_API_KEY" -H "Content-Type: application/json" \
  -d '{"url":"https://PAGE","formats":["markdown"]}'
```

## Macro / rates / housing — FRED (latest value of a series)
```bash
curl -s "https://api.stlouisfed.org/fred/series/observations?series_id=MORTGAGE30US&api_key=$FRED_API_KEY&file_type=json&sort_order=desc&limit=1"
```
Useful series: `MORTGAGE30US` (30-yr mortgage), `DGS10` (10-yr Treasury), `CPIAUCSL` (CPI), `HOUST` (housing starts), `CSUSHPINSA` (Case-Shiller HPI).

## Demographics / incomes / rents — Census ACS (market sizing)
```bash
curl -s "https://api.census.gov/data/2022/acs/acs5?get=NAME,B19013_001E,B25064_001E&for=place:*&in=state:47&key=$CENSUS_API_KEY"
```
Vars: `B19013_001E` median household income · `B25064_001E` median gross rent · `B25003` tenure · `B01003` population. (State 47 = TN; change as needed.)

## Markets / equities — Alpha Vantage (free tier: ~25 calls/day, use sparingly)
```bash
curl -s "https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=TICKER&apikey=$ALPHAVANTAGE_API_KEY"
```

## Speak — ElevenLabs (use the voice-onboarding helper)
`python underwriter-os/skills/voice-onboarding/generate_voice.py --text "..." --out underwriter-os/audio/x.mp3`

## Notes
- Read JSON back in plain English; cite the source + date; never invent figures.
- If a free-tier source is momentarily rate-limited (e.g., Alpha Vantage), fall back to web search / Tavily and say so.
