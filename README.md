# ux-workflow — Claude Code plugin + marketplace

A two-phase workflow for UX (re)design projects, packaged as a [Claude Code
plugin](https://code.claude.com/docs/en/plugins) so the whole team runs the same
method on any machine. This repo is **both** the plugin and the marketplace that
serves it.

## What's in it

Two skills that fire automatically when your task matches, or that you can invoke
explicitly:

| Skill | Phase | What it does |
|---|---|---|
| **`/ux-workflow:project-intake`** | 1 — synthesize | Turn scattered inputs (live site, sitemap, brief, workshop/stakeholder notes) into a structured, durable doc set: project brief, sitemap (source of truth), numbered requirements, per-screen layout specs, copy deck. |
| **`/ux-workflow:figma-ux-prototype`** | 2 — build | Build the screens in Figma from those specs under fixed house rules: use only the design system already in the file, componentize everything, always wire a clickable prototype, extend don't rebuild. |

The intended flow is **intake → Figma build**, but each skill stands alone (a
non-Figma project can use just the intake phase).

## Install (each teammate, once)

Inside Claude Code:

```
/plugin marketplace add <your-org>/ux-workflow-plugin
/plugin install ux-workflow@rimti
```

- Replace `<your-org>/ux-workflow-plugin` with this repo's GitHub `owner/repo`
  once it's pushed (a full `https://…​.git` URL or a local path also work).
- `rimti` is the **marketplace name** (set in `.claude-plugin/marketplace.json`) —
  the install target is always `<plugin>@<marketplace>`.

Verify with `/plugin list`. Non-interactive equivalent:

```bash
claude plugin marketplace add <your-org>/ux-workflow-plugin
claude plugin install ux-workflow@rimti
```

To enable it automatically for everyone in a given project, add to that project's
`.claude/settings.json`:

```json
{
  "extraKnownMarketplaces": {
    "rimti": { "source": { "source": "github", "repo": "<your-org>/ux-workflow-plugin" } }
  },
  "enabledPlugins": { "ux-workflow@rimti": true }
}
```

## Updating

No version is pinned, so **every push to this repo is treated as the latest
release** — improve a skill, push, and teammates pick it up. To refresh:

```
/plugin marketplace update rimti
```

## Layout

```
ux-workflow-plugin/                     ← git repo = marketplace
├── .claude-plugin/marketplace.json     ← lists the plugin(s)
├── plugins/
│   └── ux-workflow/
│       ├── .claude-plugin/plugin.json
│       └── skills/
│           ├── project-intake/
│           │   ├── SKILL.md
│           │   └── references/templates.md
│           └── figma-ux-prototype/
│               ├── SKILL.md
│               └── references/{house-rules,figma-gotchas}.md
└── README.md
```

## Renaming

Names are easy to change *before* teammates install:
- **Marketplace name** (`rimti`) → `.claude-plugin/marketplace.json` → `name`.
- **Plugin name** (`ux-workflow`, and the `/ux-workflow:` skill prefix) →
  `plugins/ux-workflow/.claude-plugin/plugin.json` → `name`, plus the directory
  name and the `source` path in `marketplace.json`.
