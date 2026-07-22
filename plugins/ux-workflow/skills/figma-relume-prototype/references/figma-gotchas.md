# `use_figma` scripting gotchas (Relume assembly)

Hard-won failure modes when driving Figma via the plugin API (`use_figma`) to
assemble Relume pages. Read before a substantial build — each of these causes
silent or confusing breakage. `/figma-use` is mandatory before any `use_figma`
call; this list is supplementary.

## Assembling section stacks & auto-layout sizing

- **Build each page as a vertical auto-layout frame** and append section instances
  top-to-bottom. New auto-layout frames default to `counterAxisSizingMode: FIXED`
  (100px) — set sizing explicitly (vertical HUG on the page frame's height) or it
  silently comes out 100px.
- **Set `layoutSizingHorizontal = 'FILL'` on a section only *after* appending it**
  to the page frame. Set before the section has an auto-layout parent, it throws or
  is ignored — and the full-width Relume section collapses to its intrinsic width.
- **Set the page frame's width to the target breakpoint** (e.g. 1440 desktop) and
  let sections FILL it; don't resize individual sections by hand.

## Editing sections: instance overrides, main-component edits, and swaps

Editing sections is expected — match the mechanism to the scope of the change (and
prefer any of these over detaching).

- **One page's content → instance overrides.** Set text on nested text nodes
  (`node.characters = …` after `figma.loadFontAsync(node.fontName)` — unloaded fonts
  throw), swap nested image/logo/avatar **instance** slots, use the section's
  exposed instance properties (`componentProperties`) for text/boolean/instance
  swaps, and add or remove repeated items via the section's own controls where the
  variant supports it.
- **Layout or styling for *every* instance → edit the main component.** Reach the
  main via `instance.mainComponent` and edit it there; the change propagates to all
  instances. Do this deliberately — it changes every page the section appears on.
- **A different layout among existing options → a swap, structured two ways.** Some
  libraries model layouts as **variant properties** of one component (switch with
  `instance.setProperties({...})` using exact variant names); others ship each
  layout as a **separate component** (`Header 1`, `Header 5` are distinct mains —
  switch with `instance.swapComponent(otherMainComponent)`). Inspect the instance's
  `mainComponent` and the component's `variantProperties` /
  `componentPropertyDefinitions` (or `get_metadata`) to see which applies before
  scripting the swap.
- **A genuinely new section (last resort) → fork, don't blank-slate.** Duplicate
  the nearest Relume section's main component, rework it, keep it as a reusable
  component bound to the Relume style-guide tokens, then place instances. This stays
  consistent and updatable, unlike a hand-built frame.
- **`detachInstance()` is the last resort, not a default.** It severs the library
  link, so the section stops matching the type scale and never gets updates. Prefer
  a main-component edit, a variant, or a new component; detach only for a genuine
  one-off you accept won't be reusable.

## Node manipulation

- **`appendChild()` returns `void`** — don't chain off it (`frame.appendChild(x).y`
  fails). Append, then operate on the child by its own reference.
- **`findAll(...).find(f => f.findOne(...))` can match an ancestor frame**, not the
  node you meant — it has silently matched a whole page frame instead of a section.
  Scope queries tightly and verify the matched node before mutating/deleting it.
- **Hyperlink text to a frame** with `setRangeHyperlink` of type `NODE`.

## Variants

- **Variant names are exact:** `Prop=Value, Prop=Value` (comma-space separated,
  exact casing) — e.g. a Relume responsive variant might be `Breakpoint=Mobile` or
  a nav state `State=Logged In`. A typo creates a new variant instead of matching.
  Read the component's actual `variantProperties` before setting them.

## Reactions / prototype

- **Setting reactions on an instance replaces inherited ones.** See the hover-merge
  rule in `relume-principles.md`: on nav targets (buttons, links, cards) that carry
  an `ON_HOVER`, clone the inherited hover and set it alongside your `ON_CLICK`.
  Form controls own their `ON_CLICK` state toggle and are never nav sources, so you
  never override them.
- **Wire nav on the global Navbar/Footer mains, on the same page as the screens.**
  Cross-page inherited reactions are ignored by Figma at runtime — keep the globals
  and the pages on one page.
- **`overlayPositionType` / `overlayBackground` are read-only** via the plugin API —
  so wire the `OVERLAY` reaction directly to the natural-size dialog/menu frame and
  leave position/background at their defaults for a human to set in the Figma UI. Do
  **not** wrap the overlay in a full-viewport frame with the modal nested inside; it
  points the prototype link at the wrapper and makes re-prototyping harder (see the
  overlay pattern in `relume-principles.md`).

## Library / style-guide conventions

- Relume publishes its sections and style guide from a **library**. Confirm the
  library is enabled for the target file and place **instances** of the published
  sections; don't copy raw section frames between files (that can detach them from
  the source).
- Build from Relume sections and the Relume style-guide tokens. Need a section the
  library lacks? Edit the nearest fit, or (last resort) create a new component from
  the tokens — and flag it for the library owner. Don't leave hand-built frames that
  ignore the tokens.
- **Search Relume by the section's job, then narrow by layout — not by name.** The
  library's name for a thing rarely matches yours ("hero" → `Header`, "features" →
  `Layout`, "logo cloud" → `Logo`), so a name-only look comes up empty and tempts
  you to build your own. Use `search_design_system` by *purpose* and check the
  category map from your inventory. Reuse the match, edit it, or (last resort)
  create — see the section ladder in `relume-principles.md`.

## Verify

After building, click through the flows and take a screenshot (`get_screenshot`)
to confirm: sections are components/instances (not stray detached frames), the same
section is reused consistently for the same job, links work, hover affordances are
present on clickables, and nothing got wiped by an over-broad query. Also **sweep
for needless one-offs** — any hand-built or detached section that duplicates a
Relume section a reuse or an edit would have covered gets folded back onto the
library (reuse the instance, or make it a proper component). A genuinely **new**
section is fine — confirm it's a reusable component bound to the style-guide
tokens, not a detached scrap, and recorded in the build-state. In the same sweep,
confirm **placed (unedited) instances kept their Relume names** — a `Layout 4`
renamed `features-grid` should be restored (see the naming rule in
`relume-principles.md`).
