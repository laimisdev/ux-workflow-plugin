---
name: figma-relume-prototype
description: >-
  Build or extend website/landing-page SCREENS in Figma by ASSEMBLING Relume
  library section blocks (Navbar, Header/hero, Layout/feature, CTA, testimonial,
  logo, stats, pricing, FAQ, contact, footer, …), under a fixed set of house
  rules: assemble from the Relume sections already in the file (never hand-build
  or restyle a section — this is the wireframe/structure phase), build each page
  as a vertical stack of section instances chosen by JOB then by LAYOUT variant,
  place the global Navbar/Footer once and reuse them, always wire a clickable
  prototype (nav on the global sections, page CTAs on the instances), and extend
  rather than rebuild. Reach for it whenever the project builds on the Relume
  section library, or the user mentions Relume, or it's a marketing / landing /
  content website assembled from prebuilt sections — e.g. "build the landing page
  in Figma with Relume", "assemble the home and pricing pages from Relume
  sections", "wire the marketing-site prototype", "add these pages using our
  Relume file", "stack a hero, features and CTA for the product page". It is the
  section-library sibling of figma-ux-prototype: use THIS when composing pages
  from Relume section blocks, and use figma-ux-prototype when composing
  app/product UI and flows from an in-file atomic design system (e.g. shadcn)
  instead. It complements the Figma MCP's /figma-use and /figma-generate-design
  skills (they do the Figma operations; this adds the Relume section-assembly
  process and house rules). It assumes the Relume library already exists in the
  file, so do NOT use it for: visual or brand design like choosing colors/fonts
  or restyling sections (a later phase); building a design system or component
  library from scratch (use /figma-generate-library); converting a Figma design
  INTO code (design-to-code); merely inspecting or reading an existing file;
  FigJam diagrams; or Figma Slides decks.
---

# Figma Relume prototype — assemble pages from section blocks, under house rules

## Why this exists

Relume works differently from an atomic design system. You don't compose a page
from buttons and inputs — you **assemble it from prebuilt section blocks** (a
Navbar, a Header/hero, a stack of Layout/feature sections, a CTA, a Footer), each
shipped in many numbered layout variants. Built well, a Relume file lets a whole
team stand up coherent marketing pages fast; built carelessly — one hand-rolled
hero here, a detached footer there — it rots into a pile of off-library one-offs
that nobody can update. These house rules keep the assembly disciplined: the file
speaks one visual language (Relume's, untouched — this is the wireframe phase),
pages are stacks of reusable section instances, the prototype clicks through like
a real site, and future sessions **extend** the file instead of rebuilding it.
Follow them even when hand-building "just this one section" is faster — that
shortcut is exactly what breaks the next person's work.

This is the section-library counterpart to `figma-ux-prototype`. Same spirit,
different unit of composition: there you compose app UI from an in-file atomic DS
(e.g. shadcn); here you assemble marketing/content pages from Relume sections. If
the project is really a complex **app** (deep checkout, dashboards, data-dense
product UI) rather than a marketing/content **site**, the atomic-DS sibling is the
better fit — say so and route there.

## Before you build

**This skill operates on the Figma file entirely through the Figma MCP.** Every
read and write — opening the file, inspecting the Relume library, placing
sections, wiring the prototype — goes through the Figma MCP's skills and tools
(`/figma-use`, `/figma-generate-design`, `use_figma`). There is no other way to
see or change the file, so set this up **first**:

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
  governs *what* and *how* to assemble; those govern the mechanics.

Then:

1. **Get the target Figma file link, confirm it, and open it through the Figma
   MCP** so you actually load its contents. Never guess the file, and never assume
   what's in it. If the Relume library lives in a **separate library file** that's
   enabled for this file, confirm that too — you place instances of sections
   published from that library.
2. **Take a section inventory — but inventory Relume the way it's organized: by
   category, not by enumerating hundreds of variants.** Relume is large, so the
   goal is a map of *what section categories exist and how you reach a specific
   one*, not a list of every block. Use the MCP (`get_metadata`,
   `search_design_system`, `get_libraries`) to record: which **categories** are
   present (Navbar, Header, Layout, CTA, Logo, Stats, Testimonial, Pricing, FAQ,
   Contact, Team, Blog, Gallery, Banner, Footer, …), the naming convention for
   variants (e.g. `Header 1…N`, `Layout 1…N`), whether layout variants are
   **separate components** or **variant properties** of one (this changes how you
   swap them — see gotchas), and the Relume **style guide / tokens** (type scale,
   colors, spacing) that all sections already use. Also note the **global**
   sections you'll place once: the Navbar and the Footer. Write this down and
   record it in the build-state so the next session reuses it. If the file has no
   Relume library, stop and raise it — assembling on an empty file is a different
   task.
3. **Have the specs in hand.** Ideally the doc set from the `project-intake`
   skill: the **sitemap** (the page list + build order), the **layout specs**
   (per-page section list and content), and the **copy deck** (the strings). If
   they don't exist yet, get at least a sitemap before building.

## The four house rules

1. **Relume sections only — assemble, don't build or restyle.** Compose every
   page from the Relume section blocks already in the file. **Never hand-build a
   section** — a hero, a feature row, a pricing table, a footer — out of frames and
   text; that off-library block is exactly what these rules exist to prevent. And
   do **not** introduce new colors, type, or spacing: this is the
   wireframe/structure phase and Relume owns the look (restyling to brand is a
   later phase). If a section type you need genuinely isn't in the library, note it
   as an open question rather than inventing it (see the selection gate in
   `relume-principles.md`).

2. **A page is a stack of section instances — pick by JOB, then by LAYOUT; never
   detach.** Build each page as a vertical auto-layout **stack of section
   instances**. Select each one in two steps: (a) choose the section **category**
   by the section's *job* on the page (open the page? explain a feature? show
   proof? convert?), then (b) choose the specific Relume **variant** by which
   *layout* fits the content in the spec (image-left, centered, grid, alternating,
   tabbed, …). Customize a section only through its instance — edit text, swap
   image/logo/avatar slots, add or remove repeated items — **never by detaching**
   (detaching severs the library link and breaks updates; to change layout, swap
   the instance to a different Relume variant). Place the **global Navbar and
   Footer once** and reuse those instances on every page. Don't rename the Relume
   instances you place (a `Header 5` stays `Header 5`); name only containers you
   author, like the page frames and canvas sections.

3. **Always wire a clickable prototype.** Pages connect into real flows. Wire
   navigation reactions on the **global Navbar and Footer mains** (on the pages'
   page), so every page inherits them — don't wire the same nav on every page.
   Page-specific CTAs (hero → sign-up, pricing → checkout/contact, blog card →
   article) are wired at the instance level. The result should click through like
   a real site. **Anything clickable is also hoverable:** Relume sections carry
   hover affordances on their buttons/links — preserve them (see the hover-merge
   rule); any clickable you author yourself needs a hover state added.

4. **Extend, don't rebuild.** Before adding a page, reuse the Navbar/Footer and any
   section variants already placed. New pages get the global nav "for free" by
   reusing the existing mains. Record which Relume sections and variants each page
   uses (see *Record the build state*) so the next session continues instead of
   re-choosing from scratch.

## Compose pages with landing-page best practices

The four rules keep the file coherent; this keeps the pages *effective*. Relume's
home turf is marketing and content pages, where the **choice and order of
sections** is what makes or breaks the page. Don't just transcribe the spec
box-by-box — ground each page's section stack in the established pattern for that
page type, and **research current conventions when you're genuinely unsure**
rather than guessing. Two boundaries hold: best practices shape **section choice,
order, content, and states** but stay **inside the Relume-only, no-restyle rule**
(they never justify new styling or a hand-built section); and they **don't
silently add scope** — where a best practice isn't covered by the spec, apply the
well-established pattern if it's clearly structural and **flag the deviation as an
open question**. The per-page-type section recipes (home/landing, product/feature,
pricing, about, contact, blog) live in
[`references/relume-principles.md`](references/relume-principles.md).

## Process

1. **Plan the page list** from the sitemap, in the agreed build order
   (highest-leverage first — typically Home/landing → primary product/feature page
   → pricing → about → contact → blog/resources → secondary pages).
2. **Place the global sections first** — instance the Relume **Navbar** and
   **Footer** once, on the pages' page (e.g. above the pages in negative-Y space,
   or a labeled "Global" section), so prototype nav wired on them is inherited by
   every page.
3. **Assemble each page as a stack of section instances**, following its layout
   spec for which sections and in what order. Ground the stack in the best-practice
   recipe for that page type first, then select each section by **job → variant by
   layout**, instance it into the page's vertical auto-layout frame, and fill
   content from the copy deck (text, image/logo slots, item counts). Reuse the
   global Navbar/Footer at top and bottom.
4. **Wire the prototype**: nav on the Navbar/Footer mains (rule 3), page CTAs on
   the section instances, overlays (mobile nav menu, cookie banner) via Figma's
   native overlay actions — wired to the natural-size frame, position/scrim left
   default and flagged for the human. Apply the agreed transition rules. Ensure
   every clickable element has a hover affordance.
5. **Add the states and variants** the specs call for — mobile/tablet section
   variants, logged-in vs guest Navbar, empty vs populated lists — using Relume's
   **built-in section variants**, not one-off duplicated frames, wherever they
   repeat.
6. **Verify** by clicking through the flows and checking a screenshot; confirm
   sections are **instances** (not detached), the same section variant is reused
   consistently, links work, and every clickable has a hover affordance. Then
   **sweep for hand-built sections**: scan the pages for any section assembled by
   hand that duplicates a Relume section (a hand-rolled hero, a bespoke pricing
   grid, a custom footer) and swap each back to the Relume instance. Anything with
   genuinely no Relume match goes on the open-questions list, not into the file. In
   the same pass, **confirm section instances kept their Relume names** (a `Layout
   4` shouldn't be renamed `features-grid`).

## Build in the project's target language

All visible text goes in the project's build language (from the copy deck), not
English placeholder, unless the user says otherwise. Localization to other
languages is a later pass.

## Record the build state

After a build session, write down — in the project's notes or your persistent
memory — the file key, the **Navbar/Footer main node IDs**, the **section map per
page** (each page → the ordered list of Relume sections + the variant used, e.g.
*Home → Navbar / Header 5 / Logo 1 / Layout 4 / Layout 10 / Testimonial 6 /
Pricing 2 / CTA 1 / Footer 4*), the naming/section-layout conventions, and any
overlays left at default position/scrim for a human to finish. This section map is
what lets the next session *extend, don't rebuild* — reusing the same section
choices instead of re-deriving them, and finding the Navbar to instance without
re-reading the whole file.

## The principles and the Figma gotchas

The rules above are the *what*. Two reference files hold the detail — read them
before a substantial build:

- [`references/relume-principles.md`](references/relume-principles.md) — the full
  regulations: the section-selection gate (job → category → variant), the
  page-need → Relume-category table, section-instance discipline (stack, swap
  don't detach, global sections, keep Relume names), prototype wiring
  (nav-on-globals, hover-merge, transition rules), the overlay pattern, the
  per-page-type section recipes, and extend-don't-rebuild.
- [`references/figma-gotchas.md`](references/figma-gotchas.md) — hard-won
  `use_figma` scripting gotchas (vertical page stacks and auto-layout sizing,
  swapping section variants vs. variant properties, editing nested section content
  without detaching, `appendChild` behavior, exact variant naming, the
  hover-reaction merge, transition/overlay API limitations). These will save you
  from subtle, silent breakage.
