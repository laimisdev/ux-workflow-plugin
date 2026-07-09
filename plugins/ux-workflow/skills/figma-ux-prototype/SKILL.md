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
  adds the spec-driven process and house rules). It assumes the design system
  already exists in the file, so do NOT use it for: visual or brand design like
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

1. **Get the target Figma file link** and confirm it. Never guess the file.
2. **Confirm a design system already exists in the file.** This skill assumes it
   does — components, tokens, styles. If the file has no DS, stop and raise it;
   building UX on an empty file is a different task.
3. **Have the specs in hand.** Ideally the doc set from the `project-intake`
   skill: the **sitemap** (the screen list + build order), the **layout specs**
   (per-screen structure), and the **copy deck** (the strings). If they don't
   exist yet, get at least a sitemap before building.
4. **Load the Figma MCP skills.** `/figma-use` is **mandatory before any
   `use_figma` call**; use `/figma-generate-design` for translating a spec/layout
   into Figma. This skill governs *what* and *how* to build; those govern the
   mechanics.

## The four house rules

1. **Design system in the file only.** Compose screens from the existing DS
   components/tokens/styles. Do **not** introduce new colors, type, or spacing —
   visual design is a later phase and the DS owns the look. If something's missing
   from the DS, note it as an open question rather than inventing a style.

2. **Componentize everything repeated.** Any element that appears more than once —
   header, footer, product card, list row, review card, stat tile, step item —
   is a **component**, and every occurrence is an **instance**. Never copy-paste a
   block. When you notice a second occurrence of something, promote it to a
   component and swap the occurrences to instances. This is what makes a
   1,000-SKU-scale catalog maintainable from templates.

3. **Always wire a clickable prototype.** Screens connect into real flows. Wire
   navigation reactions on the **main components** (on the same page as the
   screens), so every instance inherits them — don't wire the same nav 50 times on
   50 instances. Screen-specific CTAs get wired at the instance level. The result
   should click through like a real site.

4. **Extend, don't rebuild.** Before adding anything, check what already exists and
   instance it. New screens should get header/footer/card navigation "for free" by
   reusing the existing mains. Record what you built (see *Record the build
   state*) so the next session continues instead of starting over.

## Process

1. **Plan the screen list** from the sitemap, in the agreed build order
   (highest-leverage first — typically Home → primary task flow → listing → detail
   → cart/checkout → account/secondary).
2. **Build shared components first** — header, footer, and the repeated molecules
   (cards, rows, tiles, steps). Place the **main components on the screens' page**
   (e.g. above the screens in negative-Y space, or a labeled components section),
   so prototype reactions wired on the mains are inherited by all instances.
3. **Build each screen as a composition of instances**, following its layout spec
   for structure/hierarchy/content/states. Use the copy deck for all text.
4. **Wire the prototype**: nav on mains (rule 3), screen-specific CTAs on instances,
   overlays via Figma's native overlay actions — wired to the natural-size frame,
   position/scrim left default and flagged for the human. Apply the agreed
   transition rules.
5. **Add states and variants** the specs call for (empty/loading/error, logged-in
   vs guest, made-to-order vs in-stock, etc.) as component variants, not one-off
   frames, wherever they repeat.
6. **Verify** by clicking through the main flows and checking a screenshot; confirm
   instances (not detached copies), consistent components, and working links.

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
