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

To enable it automatically for everyone working in a given project, commit a
`.claude/settings.json` to **that project's** repo (not this one). Pointing the
`ref` at the `stable` branch and setting `"autoUpdate": true` is what keeps the
whole team on the latest *validated* build without anyone running update commands
by hand (see [Updating](#updating) for why both matter):

```json
{
  "extraKnownMarketplaces": {
    "rimti": {
      "source": { "source": "github", "repo": "laimisdev/ux-workflow-plugin", "ref": "stable" },
      "autoUpdate": true
    }
  },
  "enabledPlugins": { "ux-workflow@rimti": true }
}
```

Because the plugin source is remote, committed settings aren't quite zero-touch on
first run: each teammate, once, trusts the repo folder when prompted and runs
`/plugin install ux-workflow@rimti`. After that, `autoUpdate` carries them — no
more manual installs or refreshes.

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

### How updates reach the team

Versions aren't pinned by a `version` field, so Claude Code identifies each release
by its **git commit SHA** — every commit on the tracked branch is a new version.
But a push doesn't reach anyone on its own: third-party marketplaces like `rimti`
**don't auto-update by default** (only official Anthropic ones do). Two settings do
the work, and both matter:

- **`"autoUpdate": true`** — at each Claude Code **startup**, the `rimti`
  marketplace is refreshed and the installed plugin is advanced to the newest
  commit on its branch; Claude Code then prompts `/reload-plugins` to activate it.
  This is what stops teammates silently sitting on a stale cached build.
- **`"ref": "stable"`** — the marketplace tracks the `stable` branch, not `main`.
  You push to `main`; CI validates the manifests and only then fast-forwards
  `stable`, so a manifest-breaking commit can't reach the team the moment it's
  pushed — which is exactly the failure this channel exists to prevent.

Updates run at startup only, so a teammate mid-session picks up a new release on
their next restart (or after the `/reload-plugins` prompt).

### Releasing a change (maintainers)

Just push to `main` — that's the whole release. CI validates the manifests and, if
they pass, automatically fast-forwards `stable` (the branch teammates track), who
then auto-update on their next startup. If validation fails, `stable` is left
untouched, so a broken manifest never reaches anyone — you just fix and push again.

```bash
git push origin main                 # ship it; CI promotes to stable on green
python3 scripts/validate-plugin.py   # optional: run the same check locally first
```

Keep **no `version` field** in `plugins/ux-workflow/.claude-plugin/plugin.json`.
With it absent, the commit SHA drives updates and every push is seen as new. If you
ever add a `version`, you must bump it on *every* release — otherwise Claude Code
sees an unchanged version string and keeps the stale cached copy for everyone. (CI
warns if a `version` field appears.)

> **One-time repo setting:** auto-promotion needs Actions to be allowed to push. In
> GitHub → **Settings → Actions → General → Workflow permissions**, select **Read
> and write permissions**. Without it the `promote` job can't advance `stable`, and
> you'd fall back to promoting by hand (`git push origin main:stable`).

### When something still looks stale

If a teammate isn't on the version you expect after a promote + restart:

```bash
/plugin marketplace update rimti   # force-refresh the marketplace
/plugin update ux-workflow@rimti   # advance the install
/reload-plugins                    # activate in the current session
```

If it's genuinely stuck, clear the cache (there's no official command for this —
it's a workaround) and let it reinstall:

```bash
rm -rf ~/.claude/plugins/cache/rimti/ux-workflow
```

### Desktop app note

The Claude desktop app runs plugins in **local and SSH sessions only — not cloud
sessions**. Behaviour is otherwise identical to the CLI. If a teammate uses a cloud
session in the desktop app, the plugin won't be present there.

## Layout

```
ux-workflow-plugin/                     ← git repo = marketplace
├── .claude-plugin/marketplace.json     ← lists the plugin(s)
├── .github/workflows/validate.yml      ← CI: validates the manifests on push/PR
├── scripts/validate-plugin.py          ← the same check, runnable locally
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
