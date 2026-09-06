#!/usr/bin/env bash
# ============================================================
# Underwriter OS — Power Layer setup for Claude Desktop (macOS)
# Wires the verified MCP servers into your Claude Desktop config.
# Only installs servers whose runtime + API key are present.
# Safe: backs up your existing config and refuses to overwrite
# an unreadable one.
#   Usage:  cp config/.env.example config/.env && edit it
#           bash config/setup.sh
# ============================================================
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ENV_FILE="$SCRIPT_DIR/.env"

echo "=== Underwriter OS — Power Layer setup ==="

# 1) Load keys from .env (if present)
if [ -f "$ENV_FILE" ]; then
  set -a; . "$ENV_FILE"; set +a
  echo "Loaded keys from config/.env"
else
  echo "No config/.env found — copy config/.env.example to config/.env and fill it in."
  echo "Continuing with current shell environment only."
fi

# 2) Claude Desktop config path (macOS)
CONFIG_DIR="$HOME/Library/Application Support/Claude"
CONFIG_PATH="$CONFIG_DIR/claude_desktop_config.json"
mkdir -p "$CONFIG_DIR"

# 3) Detect runtimes
have(){ command -v "$1" >/dev/null 2>&1; }
HAS_NPX=0;    have npx    && HAS_NPX=1    || true
HAS_UVX=0;    have uvx    && HAS_UVX=1    || true
HAS_DOCKER=0; have docker && HAS_DOCKER=1 || true
echo "Runtimes detected -> npx:$HAS_NPX  uvx:$HAS_UVX  docker:$HAS_DOCKER"
[ "$HAS_NPX" = 1 ]    || echo "  (npx missing: install Node.js 20+ from https://nodejs.org to enable Tavily/Exa/Firecrawl/Maps)"
[ "$HAS_UVX" = 1 ]    || echo "  (uvx missing: install uv -> curl -LsSf https://astral.sh/uv/install.sh | sh  — enables OSM/AlphaVantage)"
[ "$HAS_DOCKER" = 1 ] || echo "  (docker missing: install Docker Desktop — enables SEC EDGAR/FRED)"

# 4) Back up existing config
if [ -f "$CONFIG_PATH" ]; then
  BK="$CONFIG_PATH.backup.$(date +%Y%m%d%H%M%S)"
  cp "$CONFIG_PATH" "$BK"
  echo "Backed up existing config -> $BK"
fi

# 5) Merge servers into config (only what runtime+key allow)
HAS_NPX="$HAS_NPX" HAS_UVX="$HAS_UVX" HAS_DOCKER="$HAS_DOCKER" CONFIG_PATH="$CONFIG_PATH" python3 <<'PY'
import json, os
cfg_path = os.environ["CONFIG_PATH"]
on   = lambda k: os.environ.get(k) == "1"
val  = lambda k: (os.environ.get(k) or "").strip()

servers, skipped = {}, []

if on("HAS_UVX"):
    servers["osm"] = {"command":"uvx","args":["osm-mcp-server"]}
else: skipped.append("osm (needs uv/uvx)")

if on("HAS_DOCKER"):
    ua = val("SEC_EDGAR_USER_AGENT") or "Your Firm Name (compliance@yourfirm.com)"
    servers["sec-edgar"] = {"command":"docker","args":["run","-i","--rm","-e",f"SEC_EDGAR_USER_AGENT={ua}","stefanoamorelli/sec-edgar-mcp:latest"]}
else: skipped.append("sec-edgar (needs Docker)")

if on("HAS_DOCKER") and val("FRED_API_KEY"):
    servers["fred"] = {"command":"docker","args":["run","-i","--rm","-e",f"FRED_API_KEY={val('FRED_API_KEY')}","stefanoamorelli/fred-mcp-server:latest"]}
else: skipped.append("fred (needs Docker + FRED_API_KEY)")

if on("HAS_NPX") and val("TAVILY_API_KEY"):
    servers["tavily"] = {"command":"npx","args":["-y","tavily-mcp@latest"],
        "env":{"TAVILY_API_KEY":val("TAVILY_API_KEY"),"DEFAULT_PARAMETERS":'{"search_depth":"advanced","max_results":10}'}}
else: skipped.append("tavily (needs npx + TAVILY_API_KEY)")

if on("HAS_NPX") and val("EXA_API_KEY"):
    servers["exa"] = {"command":"npx","args":["-y","exa-mcp-server"],"env":{"EXA_API_KEY":val("EXA_API_KEY")}}
else: skipped.append("exa (needs npx + EXA_API_KEY)")

if on("HAS_NPX") and val("FIRECRAWL_API_KEY"):
    servers["firecrawl"] = {"command":"npx","args":["-y","firecrawl-mcp"],
        "env":{"FIRECRAWL_API_KEY":val("FIRECRAWL_API_KEY"),"FIRECRAWL_RETRY_MAX_ATTEMPTS":"5","FIRECRAWL_CREDIT_WARNING_THRESHOLD":"2000"}}
else: skipped.append("firecrawl (needs npx + FIRECRAWL_API_KEY)")

if on("HAS_NPX") and val("GOOGLE_MAPS_API_KEY"):
    servers["google-maps"] = {"command":"npx","args":["-y","@cablate/mcp-google-map","--stdio"],
        "env":{"GOOGLE_MAPS_API_KEY":val("GOOGLE_MAPS_API_KEY"),"GOOGLE_MAPS_ENABLED_TOOLS":"maps_geocode,maps_directions,maps_search_places"}}
else: skipped.append("google-maps (needs npx + GOOGLE_MAPS_API_KEY)")

if on("HAS_UVX") and val("ALPHAVANTAGE_API_KEY"):
    servers["alphavantage"] = {"command":"uvx","args":["marketdata-mcp-server",val("ALPHAVANTAGE_API_KEY")]}
else: skipped.append("alphavantage (needs uvx + ALPHAVANTAGE_API_KEY)")

# Load existing config safely
if os.path.exists(cfg_path):
    try:
        with open(cfg_path) as f: cfg = json.load(f)
    except Exception as e:
        raise SystemExit(f"ERROR: existing {cfg_path} is not valid JSON ({e}). "
                         f"A backup was made; fix or remove the file and re-run. Refusing to overwrite.")
else:
    cfg = {}

cfg.setdefault("mcpServers", {})
cfg["mcpServers"].update(servers)
with open(cfg_path, "w") as f: json.dump(cfg, f, indent=2)

print("\nWired up: " + (", ".join(servers) if servers else "(none — add keys/runtimes and re-run)"))
if skipped:
    print("Skipped:")
    for s in skipped: print("  - " + s)
PY

# 6) Pre-pull Docker images that will be used
if [ "$HAS_DOCKER" = 1 ]; then
  echo "Pulling Docker images..."
  docker pull stefanoamorelli/sec-edgar-mcp:latest >/dev/null 2>&1 && echo "  sec-edgar image ready" || echo "  (sec-edgar pull failed — is Docker running?)"
  if [ -n "${FRED_API_KEY:-}" ]; then
    docker pull stefanoamorelli/fred-mcp-server:latest >/dev/null 2>&1 && echo "  fred image ready" || echo "  (fred pull failed — is Docker running?)"
  fi
fi

echo
echo "✅ Done. Fully QUIT Claude Desktop (Cmd+Q) and reopen it to load the servers."
echo "   Config written to: $CONFIG_PATH"
echo "   In Claude, you can then say: \"what tools do you have now?\""
