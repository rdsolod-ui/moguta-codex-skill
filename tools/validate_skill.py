#!/usr/bin/env python3
"""Validate the public Moguta.CMS skill package and repository hygiene."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
SECRET_PATTERNS = [
    re.compile(
        r"(?i)(access[_-]?token|api[_-]?key|password|secret)\s*[:=]\s*[A-Za-z0-9_./+-]{20,}"
    ),
    re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
]
FORBIDDEN_PARTS = {
    ".moguta-research",
    "__pycache__",
    "backups",
    "browser-profile",
    "cookies",
    "private",
    "production-data",
    "runtime",
    "uploads",
}
ALLOWED_TEXT_SUFFIXES = {
    ".gitignore",
    ".json",
    ".md",
    ".py",
    ".txt",
    ".yaml",
    ".yml",
}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("SKILL.md frontmatter is not closed")
    result: dict[str, str] = {}
    for raw_line in text[4:end].splitlines():
        if not raw_line.strip() or raw_line.startswith((" ", "\t")):
            continue
        if ":" not in raw_line:
            raise ValueError(f"invalid frontmatter line: {raw_line}")
        key, value = raw_line.split(":", 1)
        result[key.strip()] = value.strip().strip("\"'")
    return result


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"missing {skill_file}"]
    text = skill_file.read_text(encoding="utf-8")
    try:
        metadata = parse_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    if set(metadata) != {"name", "description"}:
        errors.append("SKILL.md frontmatter may contain only name and description")
    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not NAME_RE.fullmatch(name):
        errors.append("name must be 1-64 lowercase letters, digits, or hyphens")
    if name != skill_dir.name:
        errors.append("frontmatter name must match the skill directory")
    if not description or len(description) > 1024:
        errors.append("description is required and must be at most 1024 characters")
    if len(text.splitlines()) > 500:
        errors.append("SKILL.md must stay under 500 lines")

    required_terms = {
        "moguta",
        "moguta.cms",
        "plugins",
        "templates",
        "hooks",
        "api",
        "payment",
        "delivery",
    }
    lower_description = description.lower()
    missing_terms = sorted(term for term in required_terms if term not in lower_description)
    if missing_terms:
        errors.append(f"description missing discovery terms: {', '.join(missing_terms)}")

    required_resources = {
        "references/core-development.md",
        "references/templates.md",
        "references/plugins.md",
        "references/api-and-engine.md",
        "references/documentation-map.md",
        "references/engine-symbol-index.md",
        "scripts/inspect_moguta.py",
        "agents/openai.yaml",
    }
    for item in sorted(required_resources):
        if not (skill_dir / item).is_file():
            errors.append(f"missing skill resource: {item}")

    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)
    for link in links:
        if "://" in link or link.startswith("#"):
            continue
        target = (skill_dir / link).resolve()
        try:
            target.relative_to(skill_dir.resolve())
        except ValueError:
            errors.append(f"reference escapes skill directory: {link}")
            continue
        if not target.exists():
            errors.append(f"missing referenced file: {link}")

    openai_yaml = skill_dir / "agents" / "openai.yaml"
    if openai_yaml.is_file():
        yaml_text = openai_yaml.read_text(encoding="utf-8")
        if "$moguta-codex-skill" not in yaml_text:
            errors.append("agents/openai.yaml default prompt must name $moguta-codex-skill")

    map_path = skill_dir / "references" / "documentation-map.md"
    if map_path.is_file():
        map_text = map_path.read_text(encoding="utf-8")
        if "Coverage: 116 reachable pages" not in map_text:
            errors.append("documentation map coverage marker is missing")
        if "https://wiki.moguta.ru/devhelp" not in map_text:
            errors.append("documentation map must link to the official entry point")

    symbols_path = skill_dir / "references" / "engine-symbol-index.md"
    if symbols_path.is_file():
        symbols_text = symbols_path.read_text(encoding="utf-8")
        if "Indexed symbols: 795" not in symbols_text:
            errors.append("engine symbol count marker is missing")
        if "112 hook names" not in symbols_text:
            errors.append("hook count marker is missing")

    for path in skill_dir.rglob("*"):
        if path.is_dir():
            continue
        relative = path.relative_to(skill_dir)
        if path.name.lower() == "readme.md":
            errors.append("README.md must not be placed inside the skill directory")
        if any(part.lower() in FORBIDDEN_PARTS for part in relative.parts):
            errors.append(f"forbidden runtime path in skill: {relative}")
    return errors


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    config_path = root / "skills.sh.json"
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid skills.sh.json: {exc}")
    else:
        groups = config.get("groupings")
        if not isinstance(groups, list) or not groups:
            errors.append("skills.sh.json must contain at least one grouping")
        elif "moguta-codex-skill" not in groups[0].get("skills", []):
            errors.append("skills.sh.json must list moguta-codex-skill")

    for required in (
        "README.md",
        "LICENSE",
        "SECURITY.md",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        ".github/workflows/validate.yml",
    ):
        if not (root / required).is_file():
            errors.append(f"missing repository file: {required}")

    for path in root.rglob("*"):
        if path.is_dir() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        relative = path.relative_to(root)
        if any(part.lower() in FORBIDDEN_PARTS for part in relative.parts):
            errors.append(f"forbidden public path: {relative}")
        suffix = path.suffix.lower() or path.name.lower()
        if suffix not in ALLOWED_TEXT_SUFFIXES:
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"non-UTF-8 text file: {relative}")
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                errors.append(f"possible secret in {relative}")
                break
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_skill.py PATH_TO_SKILL", file=sys.stderr)
        return 2
    skill_dir = Path(argv[1]).resolve()
    root = skill_dir.parents[1]
    errors = validate_skill(skill_dir) + validate_repository(root)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Skill and repository are valid: {skill_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
