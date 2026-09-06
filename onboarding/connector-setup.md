# Underwriter OS — Optional Research Upgrades (click-by-click)

> Claude: Underwriter OS already works with Claude's built-in web search. These are OPTIONAL upgrades. Only set one up if the person wants it.

## Adding a connector is easy (say this)
> "Open **Settings → Connectors**, find it, click **Connect**. A window pops up — sign in (or paste the key it asks for) and you're done. I'll tell you which one to add and why."

That's the whole flow: **Connect → the login window pops up → sign in → done.** Don't overthink it.

## Tier 1 — Deeper web research (free tiers, recommended first)
**Tavily** — an AI research engine that searches the web and hands me clean, cited results.
1. Go to **tavily.com**, sign up (free), and copy your API key from the dashboard.
2. In Claude desktop: **Settings → Connectors → Add/Browse**, find **Tavily**, click **Connect**, paste the key (or sign in if it offers OAuth).
3. Done — tell me "Tavily is connected" and I'll start using it for deep research.

**Exa** — neural web search, great for finding niche sources.
1. Go to **exa.ai**, sign up, copy your API key.
2. Claude desktop → **Settings → Connectors**, find **Exa**, **Connect**, paste the key.

## Tier 2 — Investor & business-contact research
Use these for capital-partner / LP research and legitimate B2B contact info (not consumer data).
- **Apollo**, **Lusha**, **Harmonic** — find and enrich business contacts and companies.
- **CB Insights** — private-company and investor intelligence.
Each: Claude desktop → **Settings → Connectors** → find it → **Connect** → sign in with that service's account.

## Tier 3 — Professional real estate data (only if your firm subscribes)
**Yardi Matrix** — multifamily market intelligence, property search, and owner lookup. This is the strongest real estate data source if your firm has a subscription.
1. Confirm your firm has a Yardi Matrix login.
2. Claude desktop → **Settings → Connectors** → find **Yardi Matrix** → **Connect** → sign in with your firm's Yardi credentials.
3. Tell me it's connected and I'll use it for site selection, comps, and owner research.

> Note: CoStar / RealPage don't have a direct Claude connector today. If your firm uses them, I'll lean on web research + Yardi (if connected) and you can paste exports from those tools to me anytime.

## After connecting anything
Tell Claude what you connected so it can update your `CLAUDE.md` "connected tools" line and start using it.
