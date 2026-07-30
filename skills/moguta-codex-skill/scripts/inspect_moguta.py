#!/usr/bin/env python3
"""Read-only structural and safety inspection for Moguta.CMS projects."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


PLUGIN_META_RE = re.compile(r"^\s*([A-Za-z][A-Za-z ]+):\s*(.*?)\s*$", re.MULTILINE)
VERSION_PATTERNS = (
    re.compile(
        r"""define\s*\(\s*['"]VER['"]\s*,\s*['"]([0-9][A-Za-z0-9._+-]{0,31})['"]""",
        re.IGNORECASE,
    ),
    re.compile(
        r"""\bconst\s+VER\s*=\s*['"]([0-9][A-Za-z0-9._+-]{0,31})['"]""",
        re.IGNORECASE,
    ),
)
EDITION_PATTERNS = (
    re.compile(
        r"""define\s*\(\s*['"]EDITION['"]\s*,\s*['"]([A-Za-z0-9._+-]{1,32})['"]""",
        re.IGNORECASE,
    ),
    re.compile(
        r"""\bconst\s+EDITION\s*=\s*['"]([A-Za-z0-9._+-]{1,32})['"]""",
        re.IGNORECASE,
    ),
)
SECRET_VALUE_RE = re.compile(
    r"(?i)\b(?:password|passwd|api[_-]?key|secret|token)\b\s*[:=]\s*\S+"
)
SUPERGLOBAL_RE = re.compile(r"\$_(?:GET|POST|REQUEST|COOKIE|FILES)\b")
DB_QUERY_RE = re.compile(r"\bDB\s*::\s*query\s*\(", re.IGNORECASE)
DB_QUOTE_RE = re.compile(
    r"\bDB\s*::\s*quote(?:Int|Float|IN)?\s*\(", re.IGNORECASE
)


@dataclass(frozen=True)
class Finding:
    severity: str
    code: str
    path: str
    message: str


def relative(path: Path, root: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return str(path)


def read_text_safe(path: Path, limit: int = 1_000_000) -> str:
    try:
        data = path.read_bytes()
    except OSError:
        return ""
    if len(data) > limit:
        data = data[:limit]
    return data.decode("utf-8-sig", errors="replace")


def iter_files(paths: Iterable[Path], suffix: str, limit: int) -> Iterable[Path]:
    count = 0
    for base in paths:
        if not base.exists():
            continue
        candidates = [base] if base.is_file() else base.rglob(f"*{suffix}")
        for path in candidates:
            if not path.is_file():
                continue
            yield path
            count += 1
            if count >= limit:
                return


def detect_version(root: Path, max_files: int) -> tuple[list[dict], list[dict]]:
    version_hits: list[dict] = []
    edition_hits: list[dict] = []
    candidates = [
        root / "index.php",
        root / "mg-core",
    ]
    for path in iter_files(candidates, ".php", max_files):
        text = read_text_safe(path)
        for pattern in VERSION_PATTERNS:
            match = pattern.search(text)
            if match:
                version_hits.append(
                    {"value": match.group(1), "path": relative(path, root)}
                )
                break
        for pattern in EDITION_PATTERNS:
            match = pattern.search(text)
            if match:
                edition_hits.append(
                    {"value": match.group(1), "path": relative(path, root)}
                )
                break
    return version_hits, edition_hits


def parse_plugin(plugin_dir: Path, root: Path) -> tuple[dict, list[Finding]]:
    findings: list[Finding] = []
    index = plugin_dir / "index.php"
    item = {
        "folder": relative(plugin_dir, root),
        "metadata": {},
        "has_pactioner": (plugin_dir / "Pactioner.php").is_file(),
        "has_admin_page": (plugin_dir / "pageplugin.php").is_file(),
        "has_readme": (plugin_dir / "readme.txt").is_file(),
        "has_locales": (plugin_dir / "locales").is_dir(),
    }
    if not index.is_file():
        findings.append(
            Finding(
                "error",
                "plugin-index-missing",
                relative(plugin_dir, root),
                "Plugin folder has no index.php.",
            )
        )
        return item, findings

    raw = index.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        findings.append(
            Finding(
                "error",
                "php-bom",
                relative(index, root),
                "index.php starts with a UTF-8 BOM; Moguta plugin guides require UTF-8 without BOM.",
            )
        )
    text = raw[:20_000].decode("utf-8-sig", errors="replace")
    comment = re.search(r"/\*(.*?)\*/", text, re.DOTALL)
    if comment:
        metadata = {
            key.strip(): value.strip()
            for key, value in PLUGIN_META_RE.findall(comment.group(1))
        }
        safe_metadata = {
            key: value
            for key, value in metadata.items()
            if not SECRET_VALUE_RE.search(f"{key}={value}")
            and key.lower() in {
                "plugin name",
                "description",
                "author",
                "version",
                "update",
                "edition",
                "edititon",
            }
        }
        item["metadata"] = safe_metadata
    required = {"Plugin Name", "Description", "Version"}
    missing = sorted(required - set(item["metadata"]))
    if missing:
        findings.append(
            Finding(
                "warning",
                "plugin-metadata-incomplete",
                relative(index, root),
                "Missing or unreadable metadata: " + ", ".join(missing) + ".",
            )
        )
    return item, findings


def parse_template(template_dir: Path, root: Path) -> tuple[dict, list[Finding]]:
    findings: list[Finding] = []
    required = [template_dir / "template.php", template_dir / "css" / "style.css"]
    missing = [relative(path, root) for path in required if not path.is_file()]
    item = {
        "folder": relative(template_dir, root),
        "has_template_php": required[0].is_file(),
        "has_style_css": required[1].is_file(),
        "has_config_ini": (template_dir / "config.ini").is_file(),
        "has_components": (template_dir / "components").is_dir(),
        "has_functions_php": (template_dir / "functions.php").is_file(),
        "has_ajaxuser_php": (template_dir / "ajaxuser.php").is_file(),
    }
    if missing:
        findings.append(
            Finding(
                "warning",
                "template-required-file-missing",
                relative(template_dir, root),
                "Template is missing recognized required file(s): "
                + ", ".join(missing)
                + ".",
            )
        )
    if item["has_components"] and not item["has_config_ini"]:
        findings.append(
            Finding(
                "warning",
                "component-config-missing",
                relative(template_dir, root),
                "Component-based templates documented for 8.15+ require config.ini.",
            )
        )
    return item, findings


def git_core_findings(root: Path) -> list[Finding]:
    if not (root / ".git").exists():
        return []
    try:
        result = subprocess.run(
            [
                "git",
                "-C",
                str(root),
                "status",
                "--porcelain",
                "--untracked-files=no",
                "--",
                "mg-core",
            ],
            check=False,
            capture_output=True,
            text=True,
            timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return []
    if not result.stdout.strip():
        return []
    return [
        Finding(
            "warning",
            "tracked-core-changes",
            "mg-core",
            "Git reports tracked changes under mg-core; verify that core edits are intentional and upgrade-safe.",
        )
    ]


def scan_extension_php(root: Path, max_files: int) -> list[Finding]:
    findings: list[Finding] = []
    extension_roots = [
        root / "mg-plugins",
        root / "mg-templates",
        root / "mg-pages",
    ]
    for path in iter_files(extension_roots, ".php", max_files):
        try:
            raw = path.read_bytes()
        except OSError:
            continue
        if raw.startswith(b"\xef\xbb\xbf"):
            findings.append(
                Finding(
                    "error",
                    "php-bom",
                    relative(path, root),
                    "PHP file starts with a UTF-8 BOM.",
                )
            )
        text = raw.decode("utf-8-sig", errors="replace")
        for number, line in enumerate(text.splitlines(), start=1):
            if (
                DB_QUERY_RE.search(line)
                and SUPERGLOBAL_RE.search(line)
                and not DB_QUOTE_RE.search(line)
            ):
                findings.append(
                    Finding(
                        "error",
                        "dynamic-sql-superglobal",
                        f"{relative(path, root)}:{number}",
                        "DB::query() and a request superglobal occur on the same line without a DB::quote* call.",
                    )
                )
    return findings


def discover(root: Path, max_files: int) -> dict:
    findings: list[Finding] = []
    markers = {
        name: (root / name).exists()
        for name in ("mg-core", "mg-admin", "mg-plugins", "mg-templates", "mg-pages")
    }
    standalone_plugin = (root / "index.php").is_file() and "Plugin Name:" in read_text_safe(
        root / "index.php", 20_000
    )
    standalone_template = (root / "template.php").is_file() or (
        root / "css" / "style.css"
    ).is_file()
    is_moguta = any(markers.values()) or standalone_plugin or standalone_template
    if not is_moguta:
        findings.append(
            Finding(
                "error",
                "moguta-root-not-detected",
                ".",
                "No Moguta.CMS root, standalone plugin, or standalone template markers were detected.",
            )
        )

    plugin_dirs: list[Path] = []
    if (root / "mg-plugins").is_dir():
        plugin_dirs.extend(
            path for path in sorted((root / "mg-plugins").iterdir()) if path.is_dir()
        )
    elif standalone_plugin:
        plugin_dirs.append(root)

    template_dirs: list[Path] = []
    if (root / "mg-templates").is_dir():
        template_dirs.extend(
            path for path in sorted((root / "mg-templates").iterdir()) if path.is_dir()
        )
    elif standalone_template:
        template_dirs.append(root)

    plugins = []
    for plugin_dir in plugin_dirs:
        item, item_findings = parse_plugin(plugin_dir, root)
        plugins.append(item)
        findings.extend(item_findings)

    templates = []
    for template_dir in template_dirs:
        item, item_findings = parse_template(template_dir, root)
        templates.append(item)
        findings.extend(item_findings)

    versions, editions = detect_version(root, max_files)
    findings.extend(git_core_findings(root))
    findings.extend(scan_extension_php(root, max_files))
    findings = list(dict.fromkeys(findings))

    return {
        "root": str(root),
        "is_moguta": is_moguta,
        "markers": markers,
        "version_candidates": versions,
        "edition_candidates": editions,
        "plugins": plugins,
        "templates": templates,
        "findings": [asdict(item) for item in findings],
        "summary": {
            "plugins": len(plugins),
            "templates": len(templates),
            "errors": sum(item.severity == "error" for item in findings),
            "warnings": sum(item.severity == "warning" for item in findings),
        },
    }


def print_text(report: dict) -> None:
    print(f"Moguta.CMS inspection: {report['root']}")
    print(f"Detected: {'yes' if report['is_moguta'] else 'no'}")
    present = [name for name, exists in report["markers"].items() if exists]
    print("Root markers: " + (", ".join(present) if present else "none"))
    versions = report["version_candidates"]
    if versions:
        print(
            "Version candidates: "
            + ", ".join(f"{item['value']} ({item['path']})" for item in versions)
        )
    else:
        print("Version candidates: not found; verify the installed source manually")
    editions = report["edition_candidates"]
    if editions:
        print(
            "Edition candidates: "
            + ", ".join(f"{item['value']} ({item['path']})" for item in editions)
        )
    else:
        print("Edition candidates: not found; verify license/admin settings manually")
    print(
        f"Extensions: {report['summary']['plugins']} plugin(s), "
        f"{report['summary']['templates']} template(s)"
    )
    for item in report["findings"]:
        print(
            f"{item['severity'].upper()} {item['code']} "
            f"{item['path']}: {item['message']}"
        )
    print(
        f"Result: {report['summary']['errors']} error(s), "
        f"{report['summary']['warnings']} warning(s)"
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Read-only structural and safety inspection for Moguta.CMS."
    )
    parser.add_argument("root", type=Path, help="Moguta.CMS, plugin, or template root")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="return non-zero when errors or warnings are found",
    )
    parser.add_argument(
        "--max-files",
        type=int,
        default=5000,
        help="maximum PHP files to scan per phase (default: 5000)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        print(f"error: not a directory: {root}", file=sys.stderr)
        return 2
    if args.max_files < 1:
        print("error: --max-files must be positive", file=sys.stderr)
        return 2
    report = discover(root, args.max_files)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_text(report)
    if args.strict and (
        report["summary"]["errors"] or report["summary"]["warnings"]
    ):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
