#!/usr/bin/env python3
"""
Validate the ux-workflow plugin marketplace before shipping.

Runs in CI (.github/workflows/validate.yml) and locally:

    python3 scripts/validate-plugin.py

The point is to catch the mistakes that only bite AFTER a change reaches
teammates — where you can't see the error and they just report "the plugin
stopped working". The headline check is for a **hard cross-marketplace
dependency**: declaring one in plugin.json disables the ENTIRE plugin on any
machine where the depended-on plugin isn't installed/authenticated. That's what
once took ux-workflow (both skills, including the Figma-free project-intake) down
behind Figma's OAuth. Everything else here is cheap manifest hygiene.

Stdlib only — no pip install — so it behaves identically on a laptop and in CI.
Exit code 0 = clean (warnings allowed), 1 = at least one error.
"""

from __future__ import annotations  # keep `X | None` hints working on Python 3.9

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)
    print(f"  ✗ {msg}")


def warn(msg: str) -> None:
    warnings.append(msg)
    print(f"  ⚠ {msg}")


def ok(msg: str) -> None:
    print(f"  ✓ {msg}")


def load_json(path: Path):
    """Parse JSON, recording an error (and returning None) on failure."""
    try:
        return json.loads(path.read_text())
    except FileNotFoundError:
        err(f"missing file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as e:
        err(f"invalid JSON in {path.relative_to(ROOT)}: {e}")
    return None


def frontmatter(md_path: Path) -> str | None:
    """Return the YAML frontmatter block of a Markdown file, or None."""
    text = md_path.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


def fm_has(fm: str, key: str) -> bool:
    return re.search(rf"^{re.escape(key)}:", fm, re.M) is not None


def fm_scalar(fm: str, key: str) -> str | None:
    m = re.search(rf"^{re.escape(key)}:[ \t]*(.+?)[ \t]*$", fm, re.M)
    return m.group(1).strip("\"'") if m else None


def plugin_dir_from_source(source) -> Path | None:
    """A marketplace plugin `source` is a repo-relative path (string) or a dict."""
    if isinstance(source, str):
        return (ROOT / source).resolve()
    if isinstance(source, dict) and isinstance(source.get("path"), str):
        return (ROOT / source["path"]).resolve()
    return None


def check_marketplace() -> tuple[str, list]:
    print("marketplace.json")
    path = ROOT / ".claude-plugin" / "marketplace.json"
    data = load_json(path)
    if data is None:
        return "", []
    name = data.get("name")
    if not isinstance(name, str) or not name:
        err("marketplace.json needs a non-empty string `name`")
        name = ""
    else:
        ok(f"marketplace name: {name}")
    plugins = data.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        err("marketplace.json needs a non-empty `plugins` array")
        plugins = []
    else:
        ok(f"lists {len(plugins)} plugin(s)")
    if "allowCrossMarketplaceDependenciesOn" in data:
        warn(
            "marketplace.json sets `allowCrossMarketplaceDependenciesOn` — this "
            "only exists to enable hard cross-marketplace dependencies, the exact "
            "footgun this repo chose to avoid. Remove it unless you mean to use it."
        )
    return name, plugins


def check_plugin(entry: dict, market_name: str) -> None:
    entry_name = entry.get("name", "<unnamed>")
    print(f"\nplugin: {entry_name}")
    pdir = plugin_dir_from_source(entry.get("source"))
    if pdir is None or not pdir.exists():
        err(f"could not resolve plugin source to a directory: {entry.get('source')!r}")
        return

    data = load_json(pdir / ".claude-plugin" / "plugin.json")
    if data is None:
        return

    name = data.get("name")
    if name != entry_name:
        err(f"plugin.json name {name!r} != marketplace entry name {entry_name!r}")
    else:
        ok(f"name matches marketplace entry: {name}")

    if not isinstance(data.get("description"), str) or not data["description"].strip():
        err("plugin.json needs a non-empty string `description`")
    else:
        ok("has a description")

    # ---- headline check: hard cross-marketplace dependency ----
    deps = data.get("dependencies")
    if deps is not None:
        external = [
            d for d in deps
            if isinstance(d, dict)
            and isinstance(d.get("marketplace"), str)
            and d["marketplace"] != market_name
        ]
        if external:
            names = ", ".join(
                f"{d.get('name')}@{d['marketplace']}" for d in external
            )
            err(
                f"plugin.json declares a HARD cross-marketplace dependency ({names}). "
                "This disables the whole plugin on any machine where that dependency "
                "isn't installed/authenticated — taking down every skill, not just the "
                "one that needs it. Document the dependency as a prerequisite in the "
                "README/skill instead of declaring it here."
            )
        else:
            warn("plugin.json has a `dependencies` field — confirm it's intentional")

    if "version" in data:
        warn(
            "plugin.json has a `version` field. With github-marketplace + commit-SHA "
            "versioning you normally omit it; if you keep it, you MUST bump it on every "
            "release or teammates silently keep the stale cached build."
        )
    else:
        ok("no pinned `version` (commit SHA drives updates)")

    check_skills(pdir)


def check_skills(pdir: Path) -> None:
    skills_dir = pdir / "skills"
    if not skills_dir.is_dir():
        warn(f"no skills/ directory under {pdir.relative_to(ROOT)}")
        return
    skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
    if not skill_dirs:
        warn("skills/ has no skill directories")
        return

    for sd in skill_dirs:
        skill_md = sd / "SKILL.md"
        if not skill_md.exists():
            err(f"skill {sd.name}: missing SKILL.md")
            continue
        fm = frontmatter(skill_md)
        if fm is None:
            err(f"skill {sd.name}: SKILL.md has no `---` frontmatter block")
            continue
        fm_name = fm_scalar(fm, "name")
        if fm_name != sd.name:
            err(f"skill {sd.name}: frontmatter name {fm_name!r} != directory name")
        if not fm_has(fm, "description"):
            err(f"skill {sd.name}: frontmatter has no `description`")
        if fm_name == sd.name and fm_has(fm, "description"):
            ok(f"skill {sd.name}: frontmatter OK")

        # referenced files resolve (references/... and evals/... links)
        body = skill_md.read_text()
        for rel in re.findall(r"\]\((references/[^)]+|evals/[^)]+)\)", body):
            rel = rel.split("#")[0]
            if not (sd / rel).exists():
                err(f"skill {sd.name}: SKILL.md links missing file {rel}")

        # eval JSON parses
        for ej in sorted(sd.glob("evals/*.json")):
            load_json(ej)


def main() -> int:
    print(f"Validating plugin marketplace at {ROOT}\n")
    market_name, plugins = check_marketplace()
    for entry in plugins:
        if isinstance(entry, dict):
            check_plugin(entry, market_name)

    print("\n" + "=" * 60)
    print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
    if errors:
        print("FAILED")
        return 1
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
