---
name: knowledge-packs
description: Recommend, configure, and pull from Underwriter OS's tool catalog and GitHub pack. Use when the user asks "what tools can I add," "make me more powerful," "set up [a connector]," "can you get deeper data," "add real estate data," or when a task would clearly be better with a connector or repo the user hasn't set up yet.
---

# Knowledge Packs — tools & repos

This play makes Underwriter OS more powerful by connecting the right tools and pulling in the right open-source knowledge. Two reference files live in `underwriter-os/catalog/`:
- `TOOL-CATALOG.md` — every recommended connector, tiered and mapped to plays.
- `GITHUB-PACK.md` — verified GitHub repos (skills, MCP servers, RE/finance/maps data).

## Core behavior: recommend before you struggle
If a task would be materially better with a tool the user doesn't have, say so and offer to set it up — don't silently do a weaker job. Example: asked for rent comps with only web search, deliver what you can, then: *"If you connect Yardi Matrix, or a technical teammate sets up the free Census data server, I can make this much sharper — want that?"*

## Match the user to the right path
- **Basic user (non-technical staff):** only ever recommend Tier 0 + one-click first-party connectors (Tavily, Exa, Google Drive, Yardi if subscribed). Walk them through `Settings → Connectors` in plain English. NEVER ask them to install a GitHub MCP server.
- **Technical user (a firm's own IT/power user):** offer the full GitHub pack, including community MCP servers (Census, SEC EDGAR, FRED, Maps, Firecrawl). Point them to the repo READMEs and the "full real estate power setup" list in `GITHUB-PACK.md`.

## Setting up a first-party connector (any user)
1. Identify the connector from `TOOL-CATALOG.md` and say what it'll do for them.
2. Steps: Claude desktop → **Settings → Connectors** → find it → **Connect** → sign in once.
3. If it needs an API key (Tavily/Exa), point them to the signup and where to paste the key (see `onboarding/connector-setup.md`).
4. After they confirm, **update their `CLAUDE.md` "connected tools" line** so future sessions know it's available, and start using it.

## Pulling from the GitHub pack (when the user has file access)
- **Knowledge/skills repos** (e.g., `anthropics/skills`, `hesreallyhim/awesome-claude-code`): you may `git clone` or fetch specific files into a local `knowledge/` folder to learn patterns or reuse a skill (like the official docx/xlsx skills for deliverables). Pull only what's relevant; don't clone everything.
- **MCP server repos:** these are installed, not read. For a basic user, don't attempt it — instead produce a short, plain "ask your technical teammate to set this up" note naming the repo and what it unlocks. For a technical user, walk the repo README setup.

## Discovering new tools
If the firm needs something not in the catalog, consult the MCP directories in `GITHUB-PACK.md` (`modelcontextprotocol/servers`, `punkpeye/awesome-mcp-servers`), find a candidate, **verify it exists and is maintained** (check stars/last update), and only then recommend it. Never invent a tool or repo.

## Guardrails
- Verify before recommending — real connectors/repos only; flag archived/low-adoption ones honestly.
- Keep the basic-user path dead simple; push complexity to the technical path.
- After any change, reflect it in `CLAUDE.md` so the setup stays self-aware.
