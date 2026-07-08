# Figma UX build — the house rules in full

These expand the four rules in SKILL.md. They exist so that a file built by many
people, over many sessions, stays coherent and maintainable — and so future
sessions **extend** rather than rebuild.

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

## Prototype wiring

- **Wire navigation on the MAIN components**, not on each instance. The header's
  logo→Home, cart→Cart, nav items→their pages get wired once on the header main
  and every screen inherits them. Screen-specific CTAs (hero→finder, add→cart) are
  wired at the instance level.
- **Hover-merge rule (critical):** adding a reaction to a DS-derived instance
  *overrides* the reactions it inherited from its main — including the
  `ON_HOVER` → hover-state change that makes buttons feel alive. So when you add a
  nav reaction to such an instance, **merge**: clone the main component's
  hover-family reactions (`ON_HOVER`, `WHILE_PRESSING`, etc. — skip its `ON_CLICK`
  state toggle) and prepend them:
  `setReactionsAsync([...mainHoverClones, navReaction])`. Always do this on
  DS-derived instances.
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

**API limitation:** `overlayPositionType` and `overlayBackground` are **read-only**
via the plugin API. Work around it: make the overlay frame the **full viewport
size with transparent fill** (`fills = []`), and position the actual scrim /
drawer / modal *inside* it. The default CENTER position then covers the viewport
exactly and the underlying page shows through the transparent areas. (A
non-blocking banner, like cookie consent, can be scrim-less.)

## Button standardization

Everything clickable maps to a DS component — no raw icons or bare text with an
onclick:
- Filled / outline / ghost CTA → **Button**.
- Icon-only tap target → **Icon Button**.
- Standalone "see all" / action link → **Button** `Link` variant.
- Footer column links, nav items, inline-sentence anchors → **text links**
  (this is correct convention — they are not buttons).

## Extend, don't rebuild — and record the state

- Before building anything, check what exists and **instance it**. A new screen
  should inherit header/footer/card navigation for free.
- After a session, **record the build state** (project notes or persistent
  memory): the file key, key component node IDs, what screens exist, the naming
  and section layout, and any DS-specific tagging convention. The next session
  should be able to find and instance the header without re-reading the file.
- Organize the canvas into **labeled sections** (e.g. "Components", "Primary
  flow", "Account", "Overlays") and set named `flowStartingPoints` so the
  prototype opens on the right entry points.

## Show flows as progression

When a flow has steps (a finder, a checkout), build the steps as **distinct
frames that show progression** — later steps shown locked/dimmed with an unlock
hint on earlier steps — rather than collapsing everything into one screen. Users
and stakeholders need to see "what comes next".
