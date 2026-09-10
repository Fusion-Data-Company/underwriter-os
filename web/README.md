# Underwriter public product page

Standalone static HTML/CSS. No runtime dependencies, analytics, provider requests or checkout.

Preview from the repository root:

```sh
python3 -m http.server 8796 --directory web
```

Rebuild the public download from a clean committed source checkout:

```sh
python3 web/build_download.py
```

This invokes the canonical `scripts/create_workspace.py` in a temporary directory, using the explicitly unconfigured identity `Your firm - unconfigured starter`. Its tracked-source allowlist governs the package; no customer deal is created. The resulting ZIP, SHA-256 and source revision are written to `web/downloads/`. Commit changed source before rebuilding, as required by the canonical creator. The public package is MIT licensed, with optional configuration services kept separate. No standalone subscription or exclusivity claims are made.

The source repository's service section is the service inquiry destination. The page does not create payment links or reproduce unverified pricing.

## Generated assets

Built-in image generation, inspected visually:

- `assets/hero.png`: cinematic architectural scale model, dark graphite research desk, brass survey lines, warm sunlight, dark space for HTML headline; imaginary buildings, no metrics or map claims.
- `assets/evidence-flow.png`: four illustrated stages, workspace / deal / evidence / review; firm instructions, separate folders, original file plus SHA-256, human decision. Full meaning is repeated in accessible HTML and alt text.

Preview verification: desktop Chrome rendered hero, process illustration and readable page content. This is a bounded visual check, not mobile, accessibility or comprehensive release QA. No deployment performed.
