# Deal folder structure (how Claude organizes a deal)

When you start working a deal, Claude creates a folder for it inside your workspace so everything lives together:

```
<your workspace>/
├── CLAUDE.md                      ← your permanent brief (don't move)
├── underwriter-os/                    ← the system (skills, templates, docs)
├── pipeline.md                    ← your deal tracker
└── deals/
    └── <deal-name>/
        ├── 00-summary.md          ← the running snapshot of the deal
        ├── site-one-pager.md
        ├── market-study.md
        ├── comps.md
        ├── assumptions-memo.md
        ├── investor-targets.md  (or owner-brief.md)
        ├── ic-memo.md
        └── research/              ← raw sourced research briefings
```

You don't have to make any of this — Claude does it. Just say "start a deal folder for [name]" or start asking about a deal and Claude sets it up. Everything is sourced, dated, and saved so you can hand it to the committee, a lender, or a partner.
