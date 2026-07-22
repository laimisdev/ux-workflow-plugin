---
name: figma-ux-prototype
description: >-
  Build or extend UX wireframe/prototype SCREENS in Figma from structured layout
  specs, under a fixed set of house rules: use ONLY the design system already in
  the Figma file (no new visual styling), turn every repeated element into a
  component and place instances (never copy-paste), always wire a clickable
  prototype (navigation on the MAIN components, hover reactions merged not
  overwritten, agreed transition rules), and extend rather than rebuild. Reach for
  it whenever the user wants to create, build, assemble, lay out, or extend UX
  screens, wireframes, or a clickable prototype in Figma — especially the
  structure/IA/wireframe phase before visual design — e.g. "build the screens in
  Figma", "make the prototype", "add these pages to the file", "wire the flow",
  "lay out the PDP using our design system". It complements the Figma MCP's
  /figma-use and /figma-generate-design skills (they do the Figma operations; this
  adds the spec-driven process and house rules). Its sibling figma-relume-prototype
  does the same for pages ASSEMBLED from the Relume section-block library
  (marketing/landing/content sites); use that one when the project builds on Relume
  rather than on an in-file atomic design system such as shadcn. It assumes the
  design system already exists in the file, so do NOT use it for: visual or brand
  design like
  choosing colors/fonts or restyling (a later phase); building a design system or
  component library from scratch (use /figma-generate-library); converting a Figma
  design INTO code (design-to-code); merely inspecting or reading an existing
  file; FigJam diagrams; Figma Slides decks; or building screens in real code
  (React/Next) rather than in Figma.
---

# Figma UX prototype — build screens from specs, under house rules

## Why this exists

A prototype built by many people, across many screens and projects, only stays
coherent and maintainable if everyone follows the same discipline. These house
rules exist so that: the file has one visual language (the design system already
in it), repeated things change in one place (components), the prototype behaves
like a real website (wired flows), and future sessions **extend** the file instead
of rebuilding it. Follow them even when a shortcut is tempting — the shortcut is
what makes the next person's work harder.

## Before you build

**This skill operates on the Figma file entirely through the Figma MCP.** Every
read and write — opening the file, inspecting the design system, creating frames,
wiring the prototype — goes through the Figma MCP's skills and tools (`/figma-use`,
`/figma-generate-design`, `use_figma`). There is no other way to see or change the
file, so set this up **first**:

- **Confirm the Figma MCP is connected, and use it.** If its tools aren't
  available, stop and ask the user to enable the Figma MCP. Do **not** try to open
  the file link with a web fetch, and do **not** proceed as if the file can't be
  seen — Claude only "sees" the file through the MCP. (A file link alone is not
  access; you must read it via the MCP.) The MCP ships in Figma's official
  `figma@claude-plugins-official` plugin — install it if it's missing
  (`/plugin install figma@claude-plugins-official`) and authenticate once via
  `/mcp`.
- **Load `/figma-use` before any `use_figma` call** (mandatory), and use
  `/figma-generate-design` when translating a spec/layout into Figma. This skill
  governs *what* and *how* to build; those govern the mechanics.

Then:

1. **Get the target Figma file link, confirm it, and open it through the Figma
   MCP** so you actually load its contents. Never guess the file, and never assume
   what's in it without reading it via the MCP.
2. **Take a component inventory — the single most important step for avoiding
   invented components.** Don't just glance at the DS; enumerate it. Use the MCP
   (`get_metadata`, `search_design_system`, `get_libraries`) to list every
   component the file offers, and write it down: for each, `name → what it's for →
   key variants`, plus the tokens and styles. This written inventory is what you
   compose *from* and what you check *against* before creating anything (see the
   reuse gate in `house-rules.md`), and you record it in the build-state so the
   next session reuses it instead of re-deriving it. If a DS is large, still list
   what you can and search by intent for the rest — the goal is that "does the DS
   already have this?" is always answered from a list, never from a guess. If the
   file has no DS, stop and raise it; building UX on an empty file is a different
   task.
3. **Have the specs in hand.** Ideally the doc set from the `project-intake`
   skill: the **sitemap** (the screen list + build order), the **layout specs**
   (per-screen structure), and the **copy deck** (the strings). If they don't
   exist yet, get at least a sitemap before building.

## The four house rules

1. **Design system in the file only.** Compose screens from the existing DS
   components/tokens/styles. Do **not** introduce new colors, type, or spacing —
   visual design is a later phase and the DS owns the look. **This applies to
   components as much as styles:** never build your own tabs, link, accordion, or
   chip when the DS has one — search the DS by what the element *does* (its name
   there may differ), instance the match, or flag the gap. Creating a new
   component is the exception that must be justified, not the default. If
   something's missing from the DS, note it as an open question rather than
   inventing it (see the reuse gate in `house-rules.md`).

2. **Componentize everything repeated.** Any element that appears more than once —
   header, footer, product card, list row, review card, stat tile, step item —
   is a **component**, and every occurrence is an **instance**. Never copy-paste a
   block. When you notice a second occurrence of something, promote it to a
   component and swap the occurrences to instances. This is what makes a
   1,000-SKU-scale catalog maintainable from templates. **Don't rename the DS
   instances you place** — a `Button` instance stays named `Button`, not
   `btn-secondary`; name only the nodes you create (see *Keep the names of DS
   instances* in `house-rules.md`).

3. **Always wire a clickable prototype.** Screens connect into real flows. Wire
   navigation reactions on the **main components** (on the same page as the
   screens), so every instance inherits them — don't wire the same nav 50 times on
   50 instances. Screen-specific CTAs get wired at the instance level. The result
   should click through like a real site. **Anything clickable is also hoverable:**
   if an element navigates or opens an overlay, it must have a hover affordance
   too. DS components already carry one; authored clickables (cards, tiles, rows)
   need a `Hover` variant added — see *Clickable ⇒ hoverable* in `house-rules.md`.

4. **Extend, don't rebuild.** Before adding anything, check what already exists and
   instance it. New screens should get header/footer/card navigation "for free" by
   reusing the existing mains. Record what you built (see *Record the build
   state*) so the next session continues instead of starting over.

## Design the complex flows with best practices

The four rules keep the file coherent; this keeps it *good*. For the parts where
UX quality makes or breaks the experience — **checkout, account, product detail,
search/filtering, forms, sign-up/onboarding** — don't just transcribe the spec
box-by-box. Ground the structure in the established best practices for that
pattern, and **research current conventions when you're genuinely unsure** rather
than guessing. Two boundaries hold: best practices shape IA, step/field order,
states, and flow but stay **inside the DS-only rule** (they never justify new
styling or an invented component); and they **don't silently add scope** — where a
best practice isn't covered by the spec, apply the well-established pattern if it's
clearly structural and **flag the deviation as an open question**. The per-pattern
checklists (what "good" looks like for checkout, PDP, account, search, forms) live
in [`references/house-rules.md`](references/house-rules.md).

## Process

1. **Plan the screen list** from the sitemap, in the agreed build order
   (highest-leverage first — typically Home → primary task flow → listing → detail
   → cart/checkout → account/secondary).
2. **Build shared components first** — header, footer, and the repeated molecules
   (cards, rows, tiles, steps). Place the **main components on the screens' page**
   (e.g. above the screens in negative-Y space, or a labeled components section),
   so prototype reactions wired on the mains are inherited by all instances.
3. **Build each screen as a composition of instances**, following its layout spec
   for structure/hierarchy/content/states. Use the copy deck for all text. For
   high-stakes flows (checkout, PDP, account, search, forms), ground the structure
   in best practices for that pattern first (see *Design the complex flows*).
4. **Wire the prototype**: nav on mains (rule 3), screen-specific CTAs on instances,
   overlays via Figma's native overlay actions — wired to the natural-size frame,
   position/scrim left default and flagged for the human. Apply the agreed
   transition rules. Ensure every clickable element has a hover affordance — add a
   `Hover` variant to any authored clickable (cards, tiles, rows) that lacks one.
5. **Add states and variants** the specs call for (empty/loading/error, logged-in
   vs guest, made-to-order vs in-stock, etc.) as component variants, not one-off
   frames, wherever they repeat.
6. **Verify** by clicking through the main flows and checking a screenshot; confirm
   instances (not detached copies), consistent components, working links, and that
   every clickable element has a hover affordance (no click-without-hover). Then
   **sweep for invented components**: scan the screens for any locally-created
   component or raw element that duplicates something in the inventory (a
   hand-built tab bar, a bare-text link, a custom accordion), and swap each back
   to the DS instance. Anything with genuinely no DS match goes on the open-questions
   list, not into the file. In the same pass, **check DS instances kept their
   names** — a `Button` renamed to `btn-secondary` is a red flag; restore the
   inherited name and express the intent as a variant, not a rename.

## Build in the project's target language

All visible text goes in the project's build language (from the copy deck), not
English placeholder, unless the user says otherwise. Localization to other
languages is a later pass.

## Record the build state

After a build session, write down — in the project's notes or your persistent
memory — the file key, the key component node IDs, what screens exist, the
conventions used, and any overlays left at default position/scrim for a human to
finish. This is what lets the next session *extend, don't rebuild*. The
next person should be able to find the header component and instance it without
re-reading the whole file.

## The regulations and the Figma gotchas

The rules above are the *what*. Two reference files hold the detail — read them
before a substantial build:

- [`references/house-rules.md`](references/house-rules.md) — the full regulations:
  component/instance discipline, prototype wiring (nav-on-mains, hover-merge,
  transition rules), the overlay pattern, button standardization, variant/persona
  axes, and extend-don't-rebuild.
- [`references/figma-gotchas.md`](references/figma-gotchas.md) — hard-won
  `use_figma` scripting gotchas (auto-layout sizing, `appendChild` behavior,
  exact variant naming, the hover-reaction merge, transition/overlay API
  limitations). These will save you from subtle, silent breakage.
