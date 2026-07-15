# Figma UX build — the house rules in full

These expand the four rules in SKILL.md. They exist so that a file built by many
people, over many sessions, stays coherent and maintainable — and so future
sessions **extend** rather than rebuild.

## Never invent a component — search the DS first

The most common way a build goes wrong: the agent needs a UI element (tabs, a
link, an accordion), doesn't see an obvious match, and quietly builds its own.
That one detached, off-system component is exactly what these rules exist to
prevent. So treat **creating a new component as the exception that must be
justified**, never the default.

**The gate — run it before you create anything repeated or clickable:**

1. **Search the DS by what the element *does*, not by what you'd call it.** The DS
   often names things differently: "tabs" might be `Segmented Control`, a "link"
   might be a `Button` `Link` variant. Use `search_design_system` with the
   element's *purpose* and cross-check the inventory you took (see SKILL.md step 2).
2. **Match found → instance it.** A rough match beats a new component. If you need
   a state the component lacks, that's a *variant request on the existing
   component*, not grounds for a new one.
3. **Genuinely no match → flag it as an open question and stop.** A missing DS
   component is a gap for the design-system owner — record it in the build-state
   and the end-of-build summary. Do **not** paper over it by inventing one.

**Common UI pattern → DS component to reach for** (generalizes button
standardization below; always search the DS for the file's *actual* name):

| You need… | Reach for the DS… | Never… |
|---|---|---|
| Filled / outline / ghost CTA | `Button` | build a bare frame with an onclick |
| Icon-only tap target | `Icon Button` | drop a raw icon with a reaction |
| "See all" / standalone action link | `Button` `Link` variant | style text blue by hand |
| Footer / nav / inline-sentence anchor | text link | make it a Button |
| Tabs / segmented switcher | `Tabs` / `Segmented Control` | hand-build tab headers |
| Expand/collapse section | `Accordion` / `Disclosure` | build a custom toggle row |
| Removable filter / selection tag | `Chip` / `Tag` | style a pill by hand |
| Trail like Home / Shop / PDP | `Breadcrumbs` | lay out text with "/" separators |
| Inline notice / status message | `Banner` / `Alert` / `Callout` | build a colored box by hand |

If the DS genuinely lacks one of these, that's the **flag-it** path — not the
build-it path.

## Component & instance discipline

- **Every repeated element is a component; every occurrence is an instance.**
  Header, footer, cards, list rows, review cards, stat tiles, step items, class
  options — all components. When you see a second occurrence of anything, promote
  it and swap occurrences to instances. Never copy-paste a block.
- **Place main components on the same page as the screens** — e.g. above the
  screens in negative-Y space, or in a clearly labeled "Components" section. This
  matters because prototype reactions wired on a main are inherited by every
  instance *on that page*. (Figma ignores an instance's inherited reaction when it
  points to a frame on a **different** page — keep mains and screens together.)
- **Molecules over one-offs.** If three screens each hand-build the same
  "product row", extract one `Product Row` component and instance it everywhere.
- **Use variants for states**, not duplicate frames: `State=Empty/Saved/Due`,
  `User=Guest/LoggedIn`, `Delivery=Fast/MadeToOrder`, `Fit=Fits/None`. One
  component with variant axes beats ten near-identical frames.
- **Keep the names of DS instances — only rename what you create.** When you place
  an instance of a design-system component (a `Button`, an `Icon Button`, a
  `Chip`), leave its layer name as inherited from the main. Do **not** rename a
  `Button` instance to `btn-secondary`, `cta-primary`, or the like. A rename hides
  that the node is a DS instance, breaks traceability back to the DS, and makes the
  invented-component sweep unreliable — a renamed instance reads like a bespoke,
  off-system element. If you want a "secondary" button, that's a **variant** of
  `Button` (`Type=Secondary`), selected via variant props — never a rename. Reserve
  meaningful names for nodes you actually author: new components you create
  (`Product Row`), screen frames, and section/layout containers. **Rule of thumb:
  did you create this node, or instance it? Created → name it. Instanced → leave it.**

## Prototype wiring

- **Wire navigation on the MAIN components**, not on each instance. The header's
  logo→Home, cart→Cart, nav items→their pages get wired once on the header main
  and every screen inherits them. Screen-specific CTAs (hero→finder, add→cart) are
  wired at the instance level.
- **Clickable ⇒ hoverable.** Anything that navigates or opens an overlay must also
  have a hover affordance — it's how a user can tell the element is interactive and
  what makes the prototype feel real. DS components (buttons, links, cards) already
  carry an `ON_HOVER`, so preserve it (see the hover-merge rule below). But for
  components you **author** — a custom card, tile, list row, or any bespoke
  clickable — hover does **not** come for free: give the component a
  `State=Default/Hover` variant with a subtle hover treatment (elevation, border,
  or background shift, using DS tokens only) and wire `ON_HOVER → CHANGE_TO Hover`
  (`SMART_ANIMATE`, per the transition rules) on the **main**, so every instance
  inherits it. A card with an `ON_CLICK` but no hover is not finished — add the
  hover before you consider it wired.
- **Hover-merge rule (critical):** setting a reaction on a DS-derived instance
  *replaces* everything it inherited from its main — including the `ON_HOVER`
  state change that makes buttons feel alive. You only hit this on the components
  you wire nav/overlays onto — **buttons, links, cards** — which carry an
  `ON_HOVER` and leave the click open. So the merge is always the same: clone the
  inherited `ON_HOVER` and set it alongside your new `ON_CLICK`:
  `setReactionsAsync([...hoverClones, navReaction])`. **Form controls** (inputs,
  radios, checkboxes) are what own a baked-in `ON_CLICK`, but that's their own
  state toggle and they're never a nav source, so you never override them — leave
  them inheriting untouched. *(General fallback if a DS ever puts other triggers
  on a nav target: re-clone every inherited reaction on a trigger other than the
  `ON_CLICK` you're adding.)*
- **Transition rules (keep consistent across the whole file):**
  - Screen→screen `NAVIGATE`: `transition: null` (static, like a real page load).
  - Component state `CHANGE_TO`: `SMART_ANIMATE` (usually inherited from the DS).
  - Overlay open: `MOVE_IN`, `0.25s`, `EASE_OUT`, direction per overlay
    (mini-cart from RIGHT, mega-menu from TOP, most others from BOTTOM).
  - `SWAP` (e.g. banner→settings): `DISSOLVE`, `0.15s`.

## Overlay pattern

Use Figma's native overlay actions: triggers with `navigation: 'OVERLAY'`,
closers with `{type: 'CLOSE'}` (X button, scrim tap, "Cancel"), banner→settings
with `navigation: 'SWAP'`.

**Keep the overlay frame at its natural size** and wire the `OVERLAY` reaction
**directly to that frame** — a small dialog stays a small dialog, a drawer stays
drawer-width. Leave the overlay's **position and background at Figma's defaults**;
don't try to place or style them.

**Why leave them default:** `overlayPositionType` and `overlayBackground` are
**read-only** via Figma's Plugin API (not an MCP gap — Figma itself exposes no
setter), so they can only be set by hand in the Figma UI. Do **not** work around
this by wrapping the overlay in a full-viewport transparent frame with the modal
nested inside. That makes the *generated* prototype look right, but it points the
prototype link at the wrapper instead of the real dialog — so any human who later
re-prototypes has to dig in and re-link to the nested frame. Ship the
default-positioned overlay instead and flag it: setting position (e.g. drawer
pinned RIGHT) and scrim is a few seconds of UI work for a human, and the link
already points at the real dialog. Optimize for the handoff, not the first render.
(A non-blocking banner, like cookie consent, can be scrim-less.)

**Flag each overlay for the human.** Because position and scrim are left default,
leave a checklist so none ship un-styled: drop a short text note in the `Overlays`
canvas section — one line per overlay, `frame name → intended position + scrim`
(e.g. *Mini-cart → pin RIGHT, dim scrim*; *Cookie banner → bottom, no scrim*) —
and repeat that same list in the build-state record and the end-of-build summary.
That list is the checklist a human works through in the Figma UI.

## Button standardization

Everything clickable maps to a DS component — no raw icons or bare text with an
onclick. The mapping lives in the *Common UI pattern → DS component* table above
(the button/icon-button/link rows). The one convention worth restating: footer
column links, nav items, and inline-sentence anchors are **text links**, not
Buttons — that's correct, they are not buttons.

## Extend, don't rebuild — and record the state

- Before building anything, check what exists and **instance it**. A new screen
  should inherit header/footer/card navigation for free.
- After a session, **record the build state** (project notes or persistent
  memory): the **component inventory** (name → purpose → key variants) so the next
  session reuses it instead of re-deriving it and re-risking invented components,
  the file key, key component node IDs, what screens exist, the naming and section
  layout, and any DS-specific tagging convention, plus any overlays still at
  default position/scrim awaiting manual setup. The next session should be able to
  find and instance the header without re-reading the file.
- Organize the canvas into **labeled sections** (e.g. "Components", "Primary
  flow", "Account", "Overlays") and set named `flowStartingPoints` so the
  prototype opens on the right entry points.

## Show flows as progression

When a flow has steps (a finder, a checkout), build the steps as **distinct
frames that show progression** — later steps shown locked/dimmed with an unlock
hint on earlier steps — rather than collapsing everything into one screen. Users
and stakeholders need to see "what comes next".
