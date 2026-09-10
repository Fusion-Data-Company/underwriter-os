# Underwriter public product page

Static public product page plus the optional authenticated configuration engagement service. See CONFIGURATION-SERVICE.md for its Node API, database, payment and private delivery setup. The free MIT download remains public.

Preview from the repository root:

```sh
python3 -m http.server 8796 --directory web
```

Rebuild the public download from a clean committed source checkout:

```sh
python3 web/build_download.py
```

This invokes the canonical `scripts/create_workspace.py` in a temporary directory, using the explicitly unconfigured identity `Your firm - unconfigured starter`. Its tracked-source allowlist governs the package; no customer deal is created. The resulting ZIP, SHA-256 and source revision are written to `web/downloads/`. Commit changed source before rebuilding, as required by the canonical creator. The public package is MIT licensed, with optional configuration services kept separate. No standalone subscription or exclusivity claims are made.

The service inquiry destination is configuration.html. It accepts no public price: operators must publish actual scoped quotes before customers can accept and pay.

## Generated assets

Built-in image generation, inspected visually:

- `assets/hero.png`: cinematic architectural scale model, dark graphite research desk, brass survey lines, warm sunlight, dark space for HTML headline; imaginary buildings, no metrics or map claims.
- `assets/evidence-flow.png`: four illustrated stages, workspace / deal / evidence / review; firm instructions, separate folders, original file plus SHA-256, human decision. Full meaning is repeated in accessible HTML and alt text.

Preview verification: desktop Chrome rendered hero, process illustration and readable page content. This is a bounded visual check, not mobile, accessibility or comprehensive release QA. No deployment performed.
