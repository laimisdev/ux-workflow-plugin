# Developing the ux-workflow skills

## Trigger eval sets

Each skill ships a trigger eval set at `skills/<skill>/evals/trigger-eval.json` — a
flat list of realistic prompts labelled `should_trigger: true/false`. The positives
cover different phrasings of the intent; the negatives are deliberate **near-misses**
(prompts that share keywords but should route elsewhere — the other skill, a code
build, FigJam, Figma Slides, visual design, etc.). They're the guide for tuning each
skill's `description`, which is the primary mechanism that decides whether Claude
reaches for the skill.

## Re-optimizing a description

The `description` frontmatter is what to tune. The skill-creator skill has an
optimization loop that scores a description against the eval set (running each
prompt several times), proposes an improved description, and keeps the best on a
held-out split.

**Easiest path:** in a terminal, start `claude`, load the **skill-creator** skill,
and ask it to optimize this skill's description using the eval set at
`skills/<skill>/evals/trigger-eval.json`.

**Raw command** (from the skill-creator skill directory; needs Python 3.10+ and
PyYAML — `uv` supplies both):

```bash
uv run --no-project --python 3.12 --with pyyaml python -m scripts.run_loop \
  --eval-set  <repo>/plugins/ux-workflow/skills/<skill>/evals/trigger-eval.json \
  --skill-path <repo>/plugins/ux-workflow/skills/<skill> \
  --model <your-model-id> --max-iterations 5 --report none \
  --results-dir /tmp/ux-workflow-opt/<skill> --verbose
```

Take `best_description` from the resulting `results.json` and paste it into the
skill's `SKILL.md` frontmatter.

> ⚠️ **Auth caveat.** The loop spawns `claude -p` subprocesses. Run it from a
> normal terminal session where the CLI is logged in locally (keychain / creds
> file). In host-managed / Agent-SDK sessions (e.g. `ANTHROPIC_BASE_URL` set, no
> local credentials) those subprocesses fail with `401 Invalid authentication
> credentials` and every prompt scores 0 — the harness runs but tells you nothing.

The descriptions currently in the skills were tuned by reasoning against these eval
sets (added explicit scope boundaries + cross-skill disambiguation), not by the
scored loop — so an empirical pass is still worth running when you're in a terminal
session that can authenticate subprocesses.
