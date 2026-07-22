---
name: figma-relume-prototype
description: >-
  Build or extend website/landing-page SCREENS in Figma by ASSEMBLING Relume
  library section blocks (Navbar, Header/hero, Layout/feature, CTA, testimonial,
  logo, stats, pricing, FAQ, contact, footer, …), under a fixed set of house
  rules: compose from the Relume sections already in the file on a strict
  preference ladder — REUSE a section that fits, EDIT/restyle one that's close, and
  CREATE a new section only when nothing fits (always edit before you create) —
  build each page as a vertical stack of section instances chosen by JOB then by
  LAYOUT variant, place the global Navbar/Footer once and reuse them, always wire a
  clickable prototype (nav on the global sections, page CTAs on the instances), and
  extend
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
  file, so do NOT use it for: defining the brand's color palette or type system
  from scratch (the upstream design-token work); building a design system or
  component library from scratch (use /figma-generate-library); converting a Figma
  design INTO code (design-to-code); merely inspecting or reading an existing file;
  FigJam diagrams; or Figma Slides decks.
---

# Figma Relume prototype — assemble pages from section blocks, under house rules

## Why this exists

Relume works differently from an atomic design system. You don't compose a page
from buttons and inputs — you **assemble it from prebuilt section blocks** (a
Navbar, a Header/hero, a stack of Layout/feature sections, a CTA, a Footer), each
shipped in many numbered layout variants. Relume is a **customizable starting
kit**, not a locked catalogue — you may edit its sections, restyle them to the
brand, and create new ones when the library genuinely lacks something. Built well,
a Relume file lets a whole team stand up coherent marketing pages fast; built
carelessly — a *needless* hand-rolled hero here, a detached footer there — it rots
into a pile of off-library one-offs that nobody can update. So these house rules
keep the work disciplined without making it rigid: **reuse** a section when one
fits, **edit** a section when it's close, and **create** a new one only when
nothing fits — and whatever you edit or create stays a proper reusable component.
Pages stay stacks of section instances, the prototype clicks through like a real
site, and future sessions **extend** the file instead of rebuilding it. The
discipline isn't "never touch a section" — it's "don't create what you could have
reused or edited," because that needless one-off is what breaks the next person's
work.

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

1. **Reuse first, edit before you create.** Compose every page from the Relume
   section blocks in the file, in that strict order of preference: **(a) reuse** a
   section whose job and layout already fit; **(b) edit** an existing section — its
   content, layout, or styling — when one is close but not quite right; **(c)
   create** a new section only when nothing in the library can be reused or edited
   to fit. Editing and restyling sections *is* allowed and expected — Relume is a
   starting kit you shape. What's not allowed is **needlessly** hand-rolling a
   one-off when a Relume section would have worked, or leaving detached scraps
   behind. Whatever you edit or create stays a **proper reusable component** (edit
   the main component, add a variant, or build a new component from the Relume
   tokens — never a loose off-library frame). When both are viable, **prefer
   editing an existing section over creating a new one** every time. See the full
   section ladder in `relume-principles.md`.

2. **A page is a stack of section instances — pick by JOB, then by LAYOUT; edit,
   don't detach.** Build each page as a vertical auto-layout **stack of section
   instances**. Select each one in two steps: (a) choose the section **category**
   by the section's *job* on the page (open the page? explain a feature? show
   proof? convert?), then (b) choose the specific Relume **variant** by which
   *layout* fits the content in the spec (image-left, centered, grid, alternating,
   tabbed, …). Then match the edit to its scope: **one page's content** → instance
   overrides (text, image/logo/avatar swaps, item count); **a different layout
   among existing options** → swap the instance to another Relume variant; **layout
   or styling you want everywhere** → edit the **main component** (it propagates to
   every instance); **a repeating state** → add a **variant**. Reach for
   **detaching only as a last resort** for a genuine one-off — it severs the library
   link and should be rare; prefer a new component instead. Place the **global
   Navbar and Footer once** and reuse those instances on every page. Don't rename
   placed Relume instances (a `Header 5` stays `Header 5`); name the components and
   containers you author or create.

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
order, content, and states**, and they follow the same ladder — they justify
*reusing or editing* a section, not a **needless** new one, and any styling you add
uses the Relume style-guide tokens, not invented values; and they **don't silently
add scope** — where a best practice isn't covered by the spec, apply the
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
   content from the copy deck (text, image/logo slots, item counts). Where a
   section is close but not right, **edit it** (main component or variant) to fit;
   where nothing fits, **create a new section as a component** — but only after
   confirming reuse and editing won't do (the section ladder). Reuse the global
   Navbar/Footer at top and bottom.
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
   sections are components/instances (not stray detached frames), the same section
   is reused consistently, links work, and every clickable has a hover affordance.
   Then **sweep for needless one-offs**: scan for any hand-built or detached section
   that duplicates a Relume section a reuse or an edit would have covered, and fold
   it back onto the library (reuse the instance, or turn it into a proper
   component). A **new** section is fine when nothing fit — just confirm it's a real
   reusable component bound to the Relume tokens, not a detached scrap, and note it
   in the build-state. In the same pass, **confirm placed (unedited) Relume
   instances kept their names** (a `Layout 4` shouldn't be renamed `features-grid`).

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
  regulations: the section ladder (reuse → edit → create), the page-need →
  Relume-category table, section-instance discipline (stack, edit don't detach,
  global sections, keep Relume names), prototype wiring (nav-on-globals,
  hover-merge, transition rules), the overlay pattern, the per-page-type section
  recipes, and extend-don't-rebuild.
- [`references/figma-gotchas.md`](references/figma-gotchas.md) — hard-won
  `use_figma` scripting gotchas (vertical page stacks and auto-layout sizing,
  editing sections via instance overrides / main-component edits / variant swaps,
  forking a new section component, `appendChild` behavior, exact variant naming,
  the hover-reaction merge, transition/overlay API limitations). These will save
  you from subtle, silent breakage.
