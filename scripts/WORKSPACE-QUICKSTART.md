# Start with your own firm and deal

Create a new workspace from a committed source checkout:

```sh
python3 scripts/create_workspace.py --firm "Your firm name" --output /absolute/path/new-workspace
```

Open that workspace in Codex or Claude and read AGENTS.md. The provider list starts empty. No research account, payment, message or live data request is created by installation.

Within the delivered workspace, create a deal using its actual name:

```sh
python3 scripts/deal_workspace.py --workspace . create --name "Actual deal name" --slug actual-deal-name
```

Retain an actual source document, with its real provenance and publication date (or `unknown`):

```sh
python3 scripts/deal_workspace.py --workspace . source --slug actual-deal-name --file /absolute/path/document.pdf --title "Document title" --origin "Original URL or document provider" --as-of unknown
python3 scripts/deal_workspace.py --workspace . list
```

The source command stores a copy and a hash in the deal's research folder. The source registry distinguishes retention time from publication time. Capturing a document does not verify its claims. Duplicate bytes reuse the existing source record. Reusing a deal slug fails without overwriting the deal. A concurrent source import fails rather than interleaving registry writes.

Unfilled templates are marked as such. Populate them with sourced research and explicit assumptions before using them in a decision. The package contains no customer data or completed underwriting analysis.

## Continue a browser research workspace

Export workspace JSON from the browser, then import it into a new deal folder:

```sh
python3 scripts/import_browser.py --workspace . --file /absolute/path/deal-export.json --slug imported-deal
```

The import retains the exact JSON, its hash, notes and source metadata. It never overwrites an existing deal. Browser fingerprints are not original documents: imported source records are kept separately from the retained-file registry. Use the existing source command to copy each original document. Matching SHA-256 and byte count attach its browser source IDs to the retained record. Nothing is uploaded, and neither import nor hashing verifies a document's claims.
