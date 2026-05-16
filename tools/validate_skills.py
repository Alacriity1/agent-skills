#!/usr/bin/env python3
"""Validate Codex skill folders in this repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
DEFAULT_SKILLS_DIR = Path(".agents/skills")


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []

    if not text.startswith("---\n"):
        return {}, ["missing YAML frontmatter opening '---'"]

    try:
        _, frontmatter, body = text.split("---\n", 2)
    except ValueError:
        return {}, ["missing YAML frontmatter closing '---'"]

    if not body.strip():
        errors.append("missing Markdown instruction body")

    data: dict[str, str] = {}
    for line_number, raw_line in enumerate(frontmatter.splitlines(), start=2):
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            errors.append(f"invalid frontmatter line {line_number}: {raw_line!r}")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        data[key] = value

    return data, errors


def iter_skill_dirs(root: Path) -> list[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.iterdir() if path.is_dir() and not path.name.startswith("."))


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        return [f"{skill_dir}: missing SKILL.md"]

    data, parse_errors = parse_frontmatter(skill_md)
    errors.extend(f"{skill_md}: {error}" for error in parse_errors)

    allowed_keys = {"name", "description"}
    extra_keys = sorted(set(data) - allowed_keys)
    if extra_keys:
        errors.append(f"{skill_md}: unsupported frontmatter keys: {', '.join(extra_keys)}")

    name = data.get("name", "")
    description = data.get("description", "")

    if not name:
        errors.append(f"{skill_md}: missing required 'name'")
    elif not NAME_RE.fullmatch(name):
        errors.append(f"{skill_md}: name must use lowercase letters, digits, and single hyphens")
    elif name != skill_dir.name:
        errors.append(f"{skill_md}: name {name!r} must match folder {skill_dir.name!r}")

    if not description:
        errors.append(f"{skill_md}: missing required 'description'")
    elif len(description) > 1024:
        errors.append(f"{skill_md}: description must be 1024 characters or fewer")

    line_count = len(skill_md.read_text(encoding="utf-8").splitlines())
    if line_count > 500:
        errors.append(f"{skill_md}: keep SKILL.md under 500 lines; move details to references/")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Codex skill folders.")
    parser.add_argument(
        "skills_dir",
        nargs="?",
        default=str(DEFAULT_SKILLS_DIR),
        help="Directory containing skill folders, default: .agents/skills",
    )
    args = parser.parse_args()

    skills_root = Path(args.skills_dir)
    skill_dirs = iter_skill_dirs(skills_root)
    if not skill_dirs:
        print(f"No skills found in {skills_root}.")
        return 0

    errors: list[str] = []
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))

    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(skill_dirs)} skill(s) in {skills_root}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
