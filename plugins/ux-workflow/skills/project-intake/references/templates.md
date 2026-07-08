# Doc-set templates

Templates for the five intake artifacts. Copy the shape, fill with the project's
content. Keep the roles; adapt the sections. All of this is **structure and
content — no visual design**.

## Table of contents
1. Project brief (`CLAUDE.md`)
2. Sitemap (`docs/sitemap.md`)
3. Requirements (`docs/requirements.md`)
4. Layout specs (`docs/layouts/*.md`) + shared conventions README
5. Copy deck (`docs/layouts/ui-copy-<lang>.md`)

---

## 1. Project brief — `CLAUDE.md`

The orientation doc. A new session or teammate reads this first and understands
the whole project. Lead with a short "read this first" note stating the current
phase and what's in/out of scope right now.

```markdown
# <Project> — <what we're doing> Project Context

> Read this first. Current phase = <phase>. In scope now: <...>. Out of scope
> now (later phase): <...>.

## 1. What we are doing
<1–2 paragraphs: the goal, for whom, and the deliverable of THIS phase.>

## 2. Company / product snapshot
<table: brand, entity, location, scale, positioning, reputation, mission.>

## 3. What they sell / do
<product families or feature set; the data/attributes that matter to users.>

## 4. Commercial model & offers  (if applicable)
<pricing, discounts, loyalty, delivery/returns, B2B — mechanics that must survive.>

## 5. Target audience
<primary / secondary / tertiary; languages; regions.>

## 6. THE core UX challenge
<the central job-to-be-done, stated plainly. This is the north star.>

## 7. Information architecture — agreed sitemap
<pointer to docs/sitemap.md as source of truth + a one-paragraph summary +
 any NEW capabilities the redesign introduces.>

## 8. Current-state audit  (reference only)
<what to keep (strengths) and what to fix (weaknesses). If a live site, note its
 current design tokens as REFERENCE ONLY — not what we'll use.>

## 9. Goals / opportunities
<numbered; mark which are this-phase vs later.>

## 10. Constraints & considerations
<platform, scale/SKU count, commercial mechanics to preserve, workshop rules.>

## 11. Quick reference
<URLs, contacts, entity, key tokens — the at-a-glance facts.>

## 12. Status & next steps
<checklist of what's done and what's next. Keep current.>
```

---

## 2. Sitemap — `docs/sitemap.md`

The **source of truth for what to build**. Lists every page/screen and the
blocks within each. If a page isn't here, it isn't in scope.

```markdown
# <Project> — Agreed Sitemap (source of truth)

> Raw export: <link to Octopus/FigJam/XML if any>.

## Top-level structure
Home · <Category> · <core flow> · … · Auth → Profile · 404 · …

## Pages
### Home
- Block: hero / <primary CTA>
- Block: <…>
### <Page>
- Block: <…>
  - <sub-elements / states>

## New capabilities this sitemap introduces
- <capability> — <why it's new vs. the current site; which screens it touches>

## Template inventory
<list the reusable page templates: Home, Listing, Detail, Cart, Checkout,
 Account, Content, Auth, Overlay, Error…>
```

---

## 3. Requirements — `docs/requirements.md`

Numbered constraints distilled from workshop/stakeholder notes. Each carries its
**reasoning** and **how it affects the build** — that's what survives.

```markdown
# <Project> — Requirements (R1–Rn)

> Source notes: <link/folder>. Each requirement is traceable to a note.

- **R1 — <short rule>.** <One sentence.> *Why:* <reason.> *How to apply:*
  <what changes in the design/build.>
- **R2 — <short rule>.** …
```

**Example:**
`R7 — Saved equipment works for guests via cookies. Why: most buyers don't have
an account when they first need a filter. How to apply: the finder and product
page must let users save/match their unit without a login wall.`

---

## 4. Layout specs — `docs/layouts/`

One file per screen group (`01-home.md`, `02-<flow>.md`, …). **Structure and
content only.** Shared conventions live once in `docs/layouts/README.md` and are
**not repeated** per screen.

### `docs/layouts/README.md` (shared conventions — write once)
```markdown
# Layout specs — conventions
- Breakpoints: <mobile / desktop widths>
- States every screen may need: default / empty / loading / error / logged-in vs guest
- i18n: build language = <lang>; multilingual-ready (<langs>)
- Pricing/VAT rules (if commerce): <incl./excl., discounts display>
- Accessibility: <focus order, labels, contrast owned by DS>
- These specs are STRUCTURE ONLY — no colors/type/spacing (the design system owns look).
```

### Per-screen spec template
```markdown
# <NN> — <Screen name>

**Purpose:** <the one job this screen does.>
**Route / entry points:** <where it lives; how users arrive.>

## Structure (top → bottom)
1. <Section / block> — <what it contains, hierarchy, key content.>
2. <Section> — <…>
   - <component> (reused: yes/no)

## States
- Empty / loading / error / <variant> — <what changes.>

## Content
<the real content blocks; point to the copy deck for exact strings.>

## Open questions
- <unresolved decision for stakeholder review — do NOT bake in an assumption.>
```

---

## 5. Copy deck — `docs/layouts/ui-copy-<lang>.md`

The actual UI strings in the build language. Specs stay in English (build
instructions); this deck holds the real text so the build is copy-accurate.

```markdown
# UI copy — <language>

## Global
- Nav: <…>
- Buttons: <Add to cart / Subscribe / …>
- Footer: <…>

## <Screen>
- Heading: "<…>"
- Body: "<…>"
- CTA: "<…>"
- Empty state: "<…>"
```
