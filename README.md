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
/plugin marketplace add laimisdev/ux-workflow-plugin
/plugin install ux-workflow@rimti
```

- The repo is **public**, so this works with no GitHub account and no auth — the
  marketplace clones anonymously. A full `https://` git URL or a local clone path
  also work as the source.
- `rimti` is the **marketplace name** (set in `.claude-plugin/marketplace.json`) —
  the install target is always `<plugin>@<marketplace>`.

Verify with `/plugin list`. Non-interactive equivalent:

```bash
claude plugin marketplace add laimisdev/ux-workflow-plugin
claude plugin install ux-workflow@rimti
```

To enable it automatically for everyone in a given project, add to that project's
`.claude/settings.json`. Include `"autoUpdate": true` so pushes are picked up at
startup — without it a third-party marketplace is never refreshed automatically
(see [Updating](#updating)):

```json
{
  "extraKnownMarketplaces": {
    "rimti": {
      "source": { "source": "github", "repo": "laimisdev/ux-workflow-plugin" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": { "ux-workflow@rimti": true }
}
```

## Figma MCP (required for the build phase)

The `figma-ux-prototype` skill builds in Figma through Figma's **official MCP
server**, which ships in the `figma@claude-plugins-official` plugin. Install it
once — it's in Anthropic's built-in marketplace, so there's nothing extra to add:

```
/plugin install figma@claude-plugins-official
```

Then connect it via OAuth: run `/mcp` and approve in the browser. Until it's
connected, `figma-ux-prototype` cannot read a Figma file — a file link alone is
not access. (The `project-intake` skill needs none of this; it has no Figma step.)

## Updating

No version is pinned, so **every push to this repo becomes the latest release** —
but a push doesn't reach anyone on its own. Third-party marketplaces like `rimti`
**don't auto-update by default** (only official Anthropic marketplaces do), so each
teammate's Claude Code picks up a change only when its marketplace is refreshed.
Two ways to get there:

- **Refresh manually:** run `/plugin marketplace update rimti`, then
  `/reload-plugins` (or restart Claude Code) to activate the new version.
- **Turn on auto-update once:** `/plugin` → **Marketplaces** → `rimti` → **Enable
  auto-update**, or set `"autoUpdate": true` on the `rimti` entry in project
  settings (as above). Claude Code then refreshes at startup and prompts a reload
  when something changed.

If a change still doesn't appear after refreshing, clear the plugin cache with
`rm -rf ~/.claude/plugins/cache`, restart Claude Code, and reinstall.

## Layout

```
ux-workflow-plugin/                     ← git repo = marketplace
├── .claude-plugin/marketplace.json     ← lists the plugin(s)
├── plugins/
│   └── ux-workflow/
│       ├── .claude-plugin/plugin.json
│       ├── DEVELOPING.md               ← how to re-optimize skill descriptions
│       └── skills/
│           ├── project-intake/
│           │   ├── SKILL.md
│           │   ├── evals/trigger-eval.json
│           │   └── references/templates.md
│           └── figma-ux-prototype/
│               ├── SKILL.md
│               ├── evals/trigger-eval.json
│               └── references/{house-rules,figma-gotchas}.md
└── README.md
```

## Renaming

Names are easy to change *before* teammates install:
- **Marketplace name** (`rimti`) → `.claude-plugin/marketplace.json` → `name`.
- **Plugin name** (`ux-workflow`, and the `/ux-workflow:` skill prefix) →
  `plugins/ux-workflow/.claude-plugin/plugin.json` → `name`, plus the directory
  name and the `source` path in `marketplace.json`.
