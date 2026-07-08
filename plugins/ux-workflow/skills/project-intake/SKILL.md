---
name: project-intake
description: >-
  Synthesize scattered project inputs — a live site to redesign, a sitemap or IA
  export, a written brief, stakeholder or workshop notes, meeting transcripts,
  competitor links — into a structured, durable set of project documents: a
  project brief, a sitemap that becomes the single source of truth, a numbered
  requirements list, per-screen layout specs, and a copy deck. This is the FIRST
  phase of any website or app (re)design project: run it before design or build
  work so every later step reads from stable, agreed docs instead of scattered
  inputs. Use it whenever the user has raw or messy project material (URLs, notes,
  exports, transcripts, a brief) and wants it organized, structured, synthesized,
  or "made sense of" — even if they don't say "intake", e.g. "help me structure
  this project", "turn these notes and this sitemap into specs", "set up the
  project docs", "organize everything we know about this redesign".
---

# Project intake — turn raw inputs into a structured doc set

## Why this exists

Design and build work goes sideways when the context lives in scattered places —
a URL here, a Slack thread there, a half-remembered workshop. This phase converts
all of that into a small set of **durable, agreed documents** that every later
step reads from. The sitemap becomes the single source of truth for *what* to
build; the specs say *how* each screen is structured; the requirements record the
*non-obvious constraints* that would otherwise be forgotten.

The payoff is leverage: once these docs exist, any teammate (or any future
session) can pick up the project cold, and the design/build phase never has to
re-derive decisions. Treat the output as the project's memory, not throwaway notes.

## The deliverable: a fixed doc set

Produce these files (adapt paths to the repo, but keep the roles). Everything is
**structure and content — no visual design** (colors/type/spacing are decided
later, in the design tool).

| File | Role | Notes |
|---|---|---|
| `CLAUDE.md` (or `docs/project-brief.md`) | **Orientation.** Anyone new reads this first: what we're doing, the company/product, commercial model, audience, the core user challenge, IA summary, current-state audit, goals, constraints, status. | The north star. Keep it current as decisions land. |
| `docs/sitemap.md` | **Source of truth for *what* to build.** Every page/screen, and the blocks/sections within each. | If there's a raw export (Octopus, FigJam, XML), keep it alongside and link it. |
| `docs/requirements.md` | **Numbered requirements R1…Rn** distilled from workshop/stakeholder notes. Each: the rule + *why* + *how to apply*. | These are the non-obvious constraints. Cite the source note. |
| `docs/layouts/` | **Per-screen layout specs** — one file per screen group. Structure, hierarchy, content, states, open questions. | Plus a `README.md` holding shared conventions (breakpoints, states, i18n, pricing, a11y) so they're **not repeated per screen**. |
| `docs/layouts/ui-copy-<lang>.md` | **Copy deck** — the actual strings, in the build language. | Real copy, not lorem. One deck per language if multilingual. |

Templates for each of these live in [`references/templates.md`](references/templates.md) —
read it before writing, and follow the shapes there so output is consistent across
projects and teammates.

## Process

1. **Gather every input.** Ask the user for: the live/reference site URL, any
   sitemap or IA export, the brief, and all notes/transcripts. List what you have
   and what's missing before starting — don't invent context you weren't given.
2. **Analyze the sources.** If there's a live site, study it (structure, content,
   commercial mechanics, current design system as *reference only*). Pull the
   business facts, the catalog/product model, the audience, and the core
   job-to-be-done. Use web search / fetch for company registry, reviews, etc.
   when it strengthens the brief.
3. **Draft the project brief** (`CLAUDE.md`). This is the synthesis step — resolve
   contradictions in the raw inputs, and surface what's genuinely uncertain rather
   than papering over it.
4. **Agree the sitemap.** Turn the IA into `docs/sitemap.md` with blocks per page.
   Flag new capabilities the redesign introduces vs. the current site. Get the
   user to confirm this — it's the source of truth everything else hangs off.
5. **Extract requirements.** Convert workshop/stakeholder notes into numbered
   `R1…Rn`, each with the rule, the reasoning, and how it affects the build.
   Keep the source notes so requirements are traceable.
6. **Write per-screen specs** in `docs/layouts/`, in the agreed build order
   (highest-leverage screens first). Put shared conventions in the `README.md`
   once; reference it instead of repeating. End each spec with an
   **"Open questions"** list for the stakeholder review.
7. **Build the copy deck** in the build language. This is where real strings live;
   specs stay in English (build instructions), the deck holds the actual UI text.

## Principles that make the docs durable

- **Sitemap is the single source of truth for *what*.** If a screen isn't in the
  sitemap, it isn't in scope. Update the sitemap first when scope changes.
- **Requirements are numbered and explained.** `R7: saved equipment works for
  guests via cookies — because most buyers don't have an account yet — so the
  finder and PDP must not gate saving behind login.` The *why* is what survives.
- **Specs are structure only.** No visual design. This keeps the intake phase fast
  and lets the design system (chosen later) own the look. Say so explicitly in the
  README so nobody styles prematurely.
- **Preserve existing content as an asset.** Long-form SEO/brand copy, deep product
  data, reviews — lay them out to be scannable, don't delete them.
- **Convert relative dates to absolute** ("next quarter" → the actual date) and
  record decisions with their rationale, so the docs stay readable months later.
- **Name the open questions.** Every unresolved decision goes in an explicit list,
  not into an assumption. Stakeholder review resolves them.

## Adapt to the project

The doc set is fixed; the *content* flexes. An e-commerce redesign leans on
catalog/commercial mechanics and a compatibility-finder flow; a SaaS app leans on
job-to-be-done flows and states; a marketing site leans on narrative and
conversion. Keep the five artifacts, scale each to what the project needs, and
drop sections that genuinely don't apply (note that you dropped them).

## Handoff

When the doc set is agreed, the next phase is building the screens. If that's in
Figma, hand off to the **`figma-ux-prototype`** skill — the sitemap drives the
screen list, the specs drive each screen's structure, and the copy deck supplies
the strings.
