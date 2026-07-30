# Moguta Codex Skill

[![Validate](https://github.com/rdsolod-ui/moguta-codex-skill/actions/workflows/validate.yml/badge.svg)](https://github.com/rdsolod-ui/moguta-codex-skill/actions/workflows/validate.yml)
[![skills.sh](https://skills.sh/b/rdsolod-ui/moguta-codex-skill)](https://skills.sh/rdsolod-ui/moguta-codex-skill)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e.svg)](LICENSE)

An installable Agent Skill for Codex and other compatible agents that develop,
inspect, debug, modernize, and review Moguta.CMS projects.

It covers plugins, templates, hooks, shortcodes, AJAX handlers, the external
API, payment and delivery extensions, MVC overrides, database access, caching,
and version-aware upgrade safety.

## Install

### Codex

```bash
npx --yes skills add rdsolod-ui/moguta-codex-skill \
  --skill moguta-codex-skill \
  --agent codex \
  --global \
  --copy \
  --yes
```

Invoke it with:

```text
Use $moguta-codex-skill to inspect this Moguta.CMS project and add the
requested feature without modifying mg-core.
```

### Claude Code

```bash
npx --yes skills add rdsolod-ui/moguta-codex-skill \
  --skill moguta-codex-skill \
  --agent claude-code \
  --global \
  --copy \
  --yes
```

Invoke it with:

```text
/moguta-codex-skill
```

## Кратко на русском

Skill помогает Codex безопасно работать с Moguta.CMS:

- сначала определяет структуру, версию и редакцию проекта;
- выбирает расширение через плагин, hook, компонент или view вместо правки
  `mg-core`;
- знает различия документации 7.2+, 8.15+, 10.9.0+ и 12.0.0;
- маршрутизирует задачи по шаблонам, плагинам, API, оплате и доставке;
- проверяет SQL, BOM, обязательные файлы и случайные изменения ядра;
- требует тестировать активацию, обновление, AJAX, webhooks, кеш и ключевые
  торговые сценарии.

Пример:

```text
Используй $moguta-codex-skill, проверь этот проект Moguta.CMS и создай плагин
доставки с серверным пересчётом стоимости.
```

## What it handles

- Moguta.CMS project reconnaissance and version/edition gates
- `mg-plugins`, metadata, lifecycle, settings, schema upgrades
- hooks through `MG::addAction()` and shortcodes
- `Pactioner.php`, public/admin AJAX, input and authorization checks
- `mg-templates`, views, layouts, components, inheritance, `config.ini`
- `mgAddMeta()`, `mgMeta()`, `mgExcludeMeta()`, asset merging
- `mg-pages` routes and exceptional direct-PHP integrations
- `DB::query()`, `PREFIX`, `DB::quote*`, and `Storage` caching
- external Moguta API batching and signature validation
- payment plugins, webhooks, fiscalization, and receipt behavior
- delivery calculators, cart recalculation, validation, and order persistence
- upgrade-safe validation and release checklists

## Research coverage

The package was built from the official
[Moguta.CMS developer documentation](https://wiki.moguta.ru/devhelp) and its
linked generated programmer reference.

The 2026-07-30 snapshot covers:

- 116 reachable official pages;
- 39 developer guides and 77 engine-reference pages;
- 795 documented methods/functions;
- 112 documented hook names.

The skill does not mirror the wiki. It keeps a navigable official link map and
symbol index, then requires the installed source to resolve version drift.
See [documentation coverage](docs/documentation-coverage.md).

## Read-only project inspector

The dependency-free inspector accepts a full Moguta.CMS project, standalone
plugin, or standalone template:

```bash
python3 skills/moguta-codex-skill/scripts/inspect_moguta.py \
  /path/to/moguta-project
```

JSON output:

```bash
python3 skills/moguta-codex-skill/scripts/inspect_moguta.py \
  /path/to/moguta-project \
  --json
```

Release gate:

```bash
python3 skills/moguta-codex-skill/scripts/inspect_moguta.py \
  /path/to/moguta-project \
  --strict
```

It checks structure, version/edition candidates, plugin metadata, template
requirements, UTF-8 BOMs, tracked `mg-core` changes, and a narrow
request-data-in-SQL heuristic. It is not a full security scanner.

## Skill architecture

```text
skills/moguta-codex-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── api-and-engine.md
│   ├── core-development.md
│   ├── documentation-map.md
│   ├── engine-symbol-index.md
│   ├── plugins.md
│   └── templates.md
└── scripts/
    └── inspect_moguta.py
```

The main skill stays concise. Detailed workflows and the large official symbol
map load only when the task needs them.

## Example prompts

```text
Use $moguta-codex-skill to find the safest hook for modifying an order after it
is created, and verify the callback contract in this installed engine.
```

```text
Use $moguta-codex-skill to modernize this pre-8.15 template with components and
inheritance while preserving compatibility.
```

```text
Use $moguta-codex-skill to review this payment plugin's webhook, duplicate
event handling, amount verification, fiscalization, and second receipt flow.
```

```text
Use $moguta-codex-skill to integrate the Moguta API with bounded batches,
signature validation, checkpoints, and idempotent imports.
```

## Development

```bash
python3 tools/validate_skill.py skills/moguta-codex-skill
python3 -m unittest discover -s tests -v
python3 -m py_compile \
  skills/moguta-codex-skill/scripts/inspect_moguta.py \
  tools/validate_skill.py
npx --yes skills add . --list
```

## Safety and licensing

Do not commit Moguta.CMS credentials, license data, proprietary engine or paid
plugin source, production database exports, uploads, logs, orders, or customer
records.

This project is an independent developer tool. It is not affiliated with,
endorsed by, or sponsored by Moguta.CMS. Moguta.CMS names and trademarks belong
to their respective owners. Users are responsible for their Moguta.CMS license
and third-party extension terms.
