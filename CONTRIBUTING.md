# Contributing

Thank you for improving Moguta Codex Skill.

## Principles

- Keep `SKILL.md` concise and route detail to a directly linked reference.
- Prefer the installed Moguta.CMS source over a version-ambiguous wiki example.
- Do not add proprietary engine/plugin code or mirror the official wiki.
- Preserve upgrade-safe plugin, hook, component, and view extension points.
- Keep the inspector dependency-free and read-only.
- Add tests for deterministic script changes.
- Never commit production data, uploads, config values, credentials, logs, or
  license information.

## Local checks

```bash
python3 tools/validate_skill.py skills/moguta-codex-skill
python3 -m unittest discover -s tests -v
python3 -m py_compile \
  skills/moguta-codex-skill/scripts/inspect_moguta.py \
  tools/validate_skill.py
python3 /path/to/skill-creator/scripts/quick_validate.py \
  skills/moguta-codex-skill
npx --yes skills add . --list
```

## Documentation updates

Record the snapshot date and exact official URLs. Update coverage and symbol
counts only after a complete crawl of the official developer entry point and
generated reference. Summarize; do not copy full pages.

## Pull requests

Explain the user problem, compatibility impact, source evidence, behavior
change, and checks executed. Keep unrelated refactors out of the same pull
request.
