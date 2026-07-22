# Figma Relume build — the principles in full

These expand the four rules in SKILL.md. They exist so that a Relume file
assembled by many people, over many sessions, stays coherent and maintainable —
and so future sessions **extend** rather than rebuild. The unit of composition
here is the **section block**, not the atom: you assemble pages from Relume
sections, you don't compose sections from primitives.

## Never hand-build a section — search Relume first

The most common way a Relume build goes wrong: the page needs a section (a hero, a
feature explainer, a pricing table), the agent doesn't spot an exact match, and
quietly builds its own out of frames and text. That one hand-rolled, off-library
section is exactly what these rules exist to prevent — it won't match the type
scale, won't update with the library, and reads as bespoke to the next person. So
treat **hand-building a section as the exception that must be justified**, never
the default.

**The selection gate — run it before you place or build any section:**

1. **Name the section's *job* on the page, then find the Relume *category* for
   it.** Is it opening the page (→ Header), explaining a feature/benefit (→
   Layout), showing proof (→ Logo / Testimonial / Stats), prompting an action (→
   CTA)? Search the library by that purpose with `search_design_system`, and
   cross-check the category map from your inventory (SKILL.md step 2) — Relume's
   own name may differ from yours.
2. **Then pick the *variant* by which layout fits the content.** Within the
   category, Relume ships many numbered variants (`Layout 1…N`) differing by
   arrangement — image-left/right, centered, two/three/four-column grid,
   alternating rows, tabbed, carousel. Choose the one whose structure matches the
   spec's content shape. A close layout you fill with the right copy beats a
   hand-built section every time. If you need more/fewer items, that's an
   instance-level content edit, not grounds for a new section.
3. **Genuinely no match → flag it as an open question and stop.** A missing
   section type is a gap for the library owner — record it in the build-state and
   the end-of-build summary. Do **not** paper over it by hand-building one.

**Page need → Relume section category to reach for** (always search the library
for the file's *actual* names and variant numbers):

| The page needs… | Reach for the Relume category… | Never… |
|---|---|---|
| Top navigation bar | `Navbar` | build a nav row from frames |
| Page opener / hero | `Header` | hand-build a hero |
| Feature / benefit / how-it-works | `Layout` | compose feature columns by hand |
| Social proof — client logos | `Logo` (logo cloud) | drop raw logos in a row |
| Social proof — quotes/ratings | `Testimonial` | build a quote card by hand |
| Numbers / metrics | `Stats` | lay out stat tiles by hand |
| Plans / tiers | `Pricing` | hand-build pricing cards |
| Common questions | `FAQ` | build an accordion from scratch |
| Conversion prompt / banner | `CTA` / `Banner` | build a custom CTA band |
| Contact / lead form | `Contact` | assemble a form by hand |
| People | `Team` | build member cards by hand |
| Article/resource list | `Blog` / `Content` | grid out cards by hand |
| Site footer | `Footer` | build a footer from scratch |

If the library genuinely lacks one of these, that's the **flag-it** path — not the
build-it path.

## Section-assembly & instance discipline

- **Every page is a vertical auto-layout stack of section instances.** Create a
  page frame with vertical auto-layout, append section instances top-to-bottom,
  and set each section to fill the frame width (`layoutSizingHorizontal = 'FILL'`
  *after* appending — see gotchas). The stack order *is* the page's information
  architecture.
- **Place the global Navbar and Footer once, on the same page as the screens.**
  Instance the Relume Navbar and Footer a single time as the **global mains**, in a
  labeled "Global" area (e.g. negative-Y space above the pages), and reuse those
  instances at the top and bottom of every page. This matters because prototype nav
  wired on a main is inherited by every instance *on that page* — Figma ignores an
  inherited reaction that points to a frame on a **different** page, so keep the
  globals and the pages together.
- **Swap the instance to change layout — never detach.** Detaching a section
  severs its link to the Relume library, so it stops matching the type scale and
  never receives library updates; it also defeats the hand-built-section sweep
  (a detached section reads as bespoke). If a section's layout doesn't fit, **swap
  the instance to a different Relume variant** — either a variant-property change or
  a swap to a different Relume component, depending on how the library is
  structured (see gotchas). Customize only content through the instance: edit text,
  swap nested image/logo/avatar instances, add/remove repeated items via the
  section's own controls.
- **Use Relume's built-in variants for states**, not duplicate frames: mobile /
  tablet section variants, `Navbar = LoggedOut/LoggedIn`, a list section's
  empty/populated states. One section instance switched by variant beats two
  near-identical hand-placed copies.
- **Keep the names of Relume instances — only rename what you author.** A placed
  `Header 5` instance stays named `Header 5`; a `Layout 4` stays `Layout 4`. Do
  **not** rename them to `hero`, `features-grid`, or the like — a rename hides that
  the node is a Relume instance, breaks traceability back to the library, and makes
  the hand-built-section sweep unreliable. Reserve meaningful names for containers
  you actually author: the page frames and the canvas/section groupings. **Rule of
  thumb: did you create this node, or instance it? Created → name it. Instanced →
  leave it.**

## Prototype wiring

- **Wire navigation on the global Navbar and Footer mains**, not on each page. The
  logo→Home, nav items→their pages, footer links→their pages get wired once on the
  Navbar/Footer mains and every page inherits them. Page-specific CTAs (hero
  button→sign-up, pricing button→checkout/contact, blog card→article) are wired at
  the instance level, on that page.
- **Clickable ⇒ hoverable.** Anything that navigates or opens an overlay must also
  have a hover affordance — it's how a user can tell the element is interactive.
  Relume sections carry hover states on their buttons/links already, so **preserve
  them** (see the hover-merge rule below). For any clickable you author yourself
  (rare — prefer a Relume section), add a hover state with a subtle treatment using
  Relume tokens only, and wire `ON_HOVER → CHANGE_TO Hover` (`SMART_ANIMATE`) on the
  main so instances inherit it. A clickable with an `ON_CLICK` but no hover is not
  finished.
- **Hover-merge rule (critical):** setting a reaction on an instance *replaces*
  everything it inherited from its main — including the `ON_HOVER` state change that
  makes buttons feel alive. You hit this whenever you add an `ON_CLICK` to a Relume
  button/link/card that already carries an `ON_HOVER`. So the merge is always the
  same: clone the inherited `ON_HOVER` and set it alongside your new `ON_CLICK`:
  `setReactionsAsync([...hoverClones, navReaction])`. **Form controls** (inputs,
  radios, checkboxes) own a baked-in `ON_CLICK` state toggle and are never a nav
  source, so you never override them — leave them inheriting untouched. *(General
  fallback if the library ever puts other triggers on a nav target: re-clone every
  inherited reaction on a trigger other than the `ON_CLICK` you're adding.)*
- **Transition rules (keep consistent across the whole file):**
  - Page→page `NAVIGATE`: `transition: null` (static, like a real page load).
  - Section/component state `CHANGE_TO`: `SMART_ANIMATE` (usually inherited from
    Relume).
  - Overlay open: `MOVE_IN`, `0.25s`, `EASE_OUT`, direction per overlay
    (mobile nav from TOP or RIGHT, most dialogs from BOTTOM).
  - `SWAP` (e.g. cookie banner → settings): `DISSOLVE`, `0.15s`.

## Overlay pattern

Relume marketing pages mostly need a couple of overlays: the **mobile nav menu**
and a **cookie/consent banner**; occasionally a newsletter or video dialog. Use
Figma's native overlay actions: triggers with `navigation: 'OVERLAY'`, closers
with `{type: 'CLOSE'}` (X, scrim tap, "Cancel"), banner→settings with
`navigation: 'SWAP'`.

**Keep the overlay frame at its natural size** and wire the `OVERLAY` reaction
**directly to that frame** — a mobile menu stays menu-width, a dialog stays
dialog-sized. Leave the overlay's **position and background at Figma's defaults**;
don't try to place or style them.

**Why leave them default:** `overlayPositionType` and `overlayBackground` are
**read-only** via Figma's Plugin API (not an MCP gap — Figma itself exposes no
setter), so they can only be set by hand in the Figma UI. Do **not** work around
this by wrapping the overlay in a full-viewport transparent frame with the modal
nested inside. That makes the *generated* prototype look right, but it points the
prototype link at the wrapper instead of the real frame — so any human who later
re-prototypes has to dig in and re-link to the nested frame. Ship the
default-positioned overlay and flag it: setting position (e.g. mobile menu pinned
TOP) and scrim is a few seconds of UI work for a human, and the link already points
at the real frame. Optimize for the handoff, not the first render. (A non-blocking
banner, like cookie consent, can be scrim-less.)

**Flag each overlay for the human.** Because position and scrim are left default,
leave a checklist so none ship un-styled: drop a short text note in an `Overlays`
canvas section — one line per overlay, `frame name → intended position + scrim`
(e.g. *Mobile nav → pin TOP, dim scrim*; *Cookie banner → bottom, no scrim*) — and
repeat that list in the build-state record and the end-of-build summary.

## Extend, don't rebuild — and record the section map

- Before assembling anything, check what exists and **reuse it**: instance the
  existing Navbar/Footer, and reuse a section variant you've already placed rather
  than picking a new one for the same job.
- After a session, **record the build state** (project notes or persistent
  memory): the **section inventory** (category map + variant naming convention) so
  the next session reuses it, the file key, the **Navbar/Footer main node IDs**,
  the **section map per page** (page → ordered Relume sections + variant used), the
  naming and canvas-section layout, and any overlays still at default position/scrim
  awaiting manual setup. The next session should be able to find and instance the
  Navbar, and re-use the same `Pricing 2` you already chose, without re-reading the
  file.
- Organize the canvas into **labeled sections** (e.g. "Global", "Marketing pages",
  "Pricing", "Overlays") and set named `flowStartingPoints` so the prototype opens
  on the right entry points (usually Home).

## Compose pages with landing-page best practices — and research when unsure

The reuse and wiring rules keep the file coherent; this keeps the pages
*effective*. For marketing and content pages — where the choice and order of
sections is the design — don't just transcribe the layout spec section-by-section.
Build on the established pattern for that page type, and **research current
conventions when you're genuinely unsure** rather than guessing.

**Two hard boundaries:**

- **Best practices inform section choice, order, content, and states — not
  styling.** They shape which sections, in what order, with what copy and what
  states (empty/loading/error/success on any interactive section), all within the
  Relume-only, no-restyle rule. A best practice never justifies inventing a color,
  a type ramp, or a hand-built section; a missing section is still the flag-it path
  (see *Never hand-build a section*).
- **Respect the spec; don't silently add scope.** Where a best practice isn't
  covered by — or contradicts — the layout spec/sitemap, apply the well-established
  pattern if it's clearly structural, but **flag the deviation or gap as an open
  question** in the build-state and end-of-build summary. Don't invent pages or
  sections the project didn't ask for.

**Page type → section recipe** (structural expectations — search the library for
the sections that realize them, and adapt to the spec):

- **Home / landing** — `Navbar` → `Header` (clear value proposition + one primary
  CTA above the fold) → `Logo` (social proof / "trusted by") → problem→solution or
  benefit `Layout`s (lead with the user's outcome, alternate image side) →
  how-it-works `Layout` → `Testimonial` → `Pricing` or feature highlight →
  `FAQ` → final `CTA` → `Footer`.
- **Product / feature** — `Header` framing the one feature → benefit `Layout`s
  (what it does → why it matters) → proof (`Stats`/`Testimonial`) → a focused `CTA`
  → `Footer`.
- **Pricing** — `Header` (short) → `Pricing` table → feature `Comparison`/`Layout`
  → `FAQ` (billing/plan questions) → `CTA` → `Footer`.
- **About** — `Header` (mission/story) → `Stats` → values `Layout`s → `Team` →
  `CTA` (careers or contact) → `Footer`.
- **Contact** — `Contact` (form + details) → `Locations`/map if relevant → `FAQ` →
  `Footer`.
- **Blog / resources** — `Header` → article list/grid (`Blog`/`Content`) with
  category filter → newsletter `CTA` → `Footer`.

When a page type isn't in this list but is clearly important or unfamiliar, treat
it the same way: establish the best-practice section pattern first (research if
needed), then assemble.

## Show flows as progression

When a page is part of a multi-step flow (a multi-step sign-up, a lead funnel,
onboarding), build the steps as **distinct frames that show progression** — later
steps shown locked/dimmed with an unlock hint on earlier steps — rather than
collapsing everything into one screen. Stakeholders need to see "what comes next".
