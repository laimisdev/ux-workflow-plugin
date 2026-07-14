# `use_figma` scripting gotchas

Hard-won failure modes when driving Figma via the plugin API (`use_figma`).
Read before a substantial build — each of these causes silent or confusing
breakage. `/figma-use` is mandatory before any `use_figma` call; this list is
supplementary.

## Auto-layout sizing

- **New auto-layout frames default to `counterAxisSizingMode: FIXED` (100px).**
  Always set sizing explicitly (`AUTO` / hug) or your frames silently come out
  100px wide/tall.
- **Set `layoutSizingHorizontal = 'FILL'` only *after* appending** the node to its
  parent. Setting it before the node has an auto-layout parent throws or is ignored.
- **Short frames** (content shorter than the viewport) need an explicit fixed
  height with the content set to `layoutGrow`, or footers won't pin to the bottom
  of the viewport.

## Node manipulation

- **`appendChild()` returns `void`** — don't chain off it (`frame.appendChild(x).y`
  fails). Append, then operate on the child by its own reference.
- **`findAll(...).find(f => f.findOne(...))` can match an ancestor frame**, not the
  node you meant. This has silently wiped screen bodies (the finder matched the
  page-level body frame instead of a card). Scope your queries tightly and verify
  the matched node before mutating/deleting it.
- **Hyperlink text to a frame** with `setRangeHyperlink` of type `NODE`.

## Variants

- **Variant names are exact:** `Prop=Value, Prop=Value` (comma-space separated,
  exact casing). A checkbox is `Checked=Off, State=Default`. A typo creates a new
  variant instead of matching.

## Reactions / prototype

- **Setting reactions on an instance replaces inherited ones.** See the
  hover-merge rule in `house-rules.md`: on nav targets (buttons, links, cards)
  clone the inherited `ON_HOVER` and set it alongside your `ON_CLICK`. Form
  controls own their `ON_CLICK` state toggle and are never nav sources, so you
  never override them.
- **Wire nav on mains, on the same page as the screens.** Cross-page inherited
  reactions are ignored by Figma at runtime.
- **`overlayPositionType` / `overlayBackground` are read-only** via the plugin
  API — so wire the `OVERLAY` reaction directly to the natural-size dialog/drawer
  frame and leave position/background at their defaults for a human to set in the
  Figma UI. Do **not** wrap the overlay in a full-viewport frame with the modal
  nested inside; it points the prototype link at the wrapper and makes
  re-prototyping harder (see the overlay pattern in `house-rules.md`).

## Design-system conventions

- If the file's DS uses a manifest/self-documenting convention (e.g. shared
  plugin data with a `manifest` and a `run_id`), **read it first** and **tag new
  nodes** per that convention with the current run id. It's how the DS stays
  navigable and how the next session finds your work.
- Compose from DS components/tokens/styles only. Missing piece? Note it as an open
  question — don't invent a style (visual design is a later phase).
- **Search the DS by intent, not by name, before creating any component.** The
  file's name for a thing rarely matches yours ("tabs" → `Segmented Control`,
  "link" → `Button` `Link` variant), so a name-only look comes up empty and tempts
  you to build your own. Use `search_design_system` by *purpose* and check the
  inventory. Reuse the match, or flag the gap — see the reuse gate in
  `house-rules.md`.

## Verify

After building, click through the main flows and take a screenshot
(`get_screenshot`) to confirm: instances are instances (not detached), components
are consistent, links work, and nothing got wiped by an over-broad query. Also
**sweep for invented components** — any locally-created component or raw element
that duplicates something in the inventory (hand-built tabs, bare-text links,
custom accordions) gets swapped back to the DS instance; anything with no DS match
goes on the open-questions list, not into the file.
