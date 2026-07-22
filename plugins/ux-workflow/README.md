# ux-workflow

A workflow for UX (re)design projects: synthesize the inputs, then build the
screens in Figma. Two build skills share the same house rules but differ in the
**unit of composition** — pick by which library the project uses.

- **`project-intake`** — synthesize scattered project inputs into a structured,
  durable doc set (brief, sitemap-as-source-of-truth, numbered requirements,
  per-screen layout specs, copy deck) before any design/build work.
- **`figma-ux-prototype`** — build **app / product UI** in Figma by composing an
  **in-file atomic design system** (e.g. shadcn: Button, Input, Card…) under fixed
  house rules (design-system-in-file only, componentize everything, always wire a
  clickable prototype, extend don't rebuild).
- **`figma-relume-prototype`** — build **marketing / landing / content pages** in
  Figma by **assembling Relume section blocks** (Navbar, Header/hero,
  Layout/feature, CTA, pricing, FAQ, footer…) chosen by job then layout variant,
  under the same house rules adapted to section assembly.

**Which build skill?** Use `figma-relume-prototype` when the project builds on the
Relume section library or is a marketing/content site; use `figma-ux-prototype`
when composing app UI from an in-file atomic design system. Both assume the
library/design-system already exists in the file (visual/brand styling is a later
phase).

See the [repo README](../../README.md) for install and update instructions.
