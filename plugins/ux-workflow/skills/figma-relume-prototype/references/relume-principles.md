# Figma Relume build — the principles in full

These expand the four rules in SKILL.md. They exist so that a Relume file
assembled by many people, over many sessions, stays coherent and maintainable —
and so future sessions **extend** rather than rebuild. The unit of composition
here is the **section block**, not the atom: you assemble pages from Relume
sections, you don't compose sections from primitives.

## Reuse first, edit before you create — the section ladder

Relume is a **customizable starting kit, not a locked catalogue**: you may edit,
restyle, and extend its sections, and create new ones when the library genuinely
lacks something. What rots a file is not editing — it's a *needless* off-library
one-off: a hand-rolled hero built when a Relume `Header` would have fit, or a
detached scrap left behind that won't match the type scale or get library updates.
So keep a strict order of preference and **stop at the first rung that works**.

**The section ladder — run it before you place, edit, or build any section:**

1. **Reuse.** Name the section's *job* on the page, find the Relume *category* for
   it, then pick the *variant* whose layout fits — and instance it. This is the
   default and covers most sections.
   - **Job → category:** opening the page (→ Header), explaining a feature/benefit
     (→ Layout), showing proof (→ Logo / Testimonial / Stats), prompting an action
     (→ CTA)? Search with `search_design_system` by that purpose and cross-check
     the category map from your inventory (SKILL.md step 2) — Relume's names differ
     from yours.
   - **Category → variant:** within the category, Relume ships many numbered
     variants (`Layout 1…N`) differing by arrangement — image-left/right, centered,
     grid, alternating rows, tabbed, carousel. Pick the closest and fill it with
     the spec's content. Needing more/fewer items is an instance-level content
     edit, not grounds for anything new.
2. **Edit.** If a section is *close but not right*, adapt it rather than starting
   over. Change content through the instance; change layout or styling by **editing
   the main component** (so every instance updates with it) or by **adding a
   variant** for a repeating state. Editing and restyling are in scope — a
   customized Relume section is still a first-class, reusable component.
   **Prefer this over creating whenever an existing section can be bent to fit.**
3. **Create — last resort.** Only when nothing can be reused or edited to fit,
   create a new section, and make it a **proper reusable component**: full-width,
   auto-layout, built from the Relume style-guide tokens (type scale, colors,
   spacing) so it matches the file, and clearly named. The best starting point is
   to **duplicate the nearest Relume section into a new component and rework it**,
   not to build from a blank frame. Record any new section in the build-state and
   flag it for the library owner — it may belong in the shared library.

**Detaching an instance is not a rung on this ladder** — it produces an off-library
scrap. Edit the main component or create a new component instead; detach only for a
true one-off you accept won't be reusable.

**Page need → Relume section category to reach for** (always search the library
for the file's *actual* names and variant numbers — reuse the match, edit it to
fit, or create only as a last resort):

| The page needs… | Reach for the Relume category… | Don't hand-roll (reuse/edit instead)… |
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

If the library genuinely lacks one of these, edit the nearest fit to cover it, or
(last resort) create it as a proper component from the Relume tokens — and flag it
for the library owner.

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
- **To change a section, edit — don't detach.** Match the tool to the scope:
  **content** → instance overrides (text, nested image/logo/avatar swaps, item
  count via the section's own controls); **a different layout among existing
  options** → swap the instance to another Relume variant (a variant-property
  change or a swap to a different Relume component, depending on how the library is
  structured — see gotchas); **layout or styling that should apply everywhere** →
  edit the **main component** (it propagates to every instance); **a new repeating
  state** → add a **variant**. Detaching severs the library link — the section
  stops matching the type scale and never receives updates — so reserve it for a
  genuine one-off, and prefer a new component over a detached frame.
- **Use Relume's built-in variants for states**, not duplicate frames: mobile /
  tablet section variants, `Navbar = LoggedOut/LoggedIn`, a list section's
  empty/populated states. One section instance switched by variant beats two
  near-identical hand-placed copies.
- **Keep the names of placed Relume instances — name what you create.** A placed,
  unedited `Header 5` instance stays named `Header 5`; a `Layout 4` stays `Layout
  4`. Do **not** rename them to `hero`, `features-grid`, or the like — a rename
  hides that the node is a Relume instance, breaks traceability back to the library,
  and makes the needless-one-off sweep unreliable. Give clear names to what you
  **create**: new components (and ones you fork/customize into your own component),
  page frames, and canvas/section groupings. **Rule of thumb: placed as-is → leave
  the name; created or forked into your own component → name it.**

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

- **Best practices inform section choice, order, content, and states.** They shape
  which sections, in what order, with what copy and what states
  (empty/loading/error/success on any interactive section). They follow the same
  ladder: a best practice justifies *reusing or editing* a section, not a
  **needless** new one, and any styling it motivates uses the Relume style-guide
  tokens, not invented values. A truly missing section is the *create-as-last-
  resort* path (see *the section ladder*), done as a proper component.
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
