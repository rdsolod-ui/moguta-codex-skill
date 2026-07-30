# Documentation coverage

## Research boundary

The skill was prepared from the official
[Moguta.CMS developer entry point](https://wiki.moguta.ru/devhelp) on
2026-07-30 (Europe/Moscow).

The crawl followed every reachable HTML page under:

- `/devhelp` for architecture, task, template, plugin, and API guides;
- `/help` for generated libraries, models, controllers, views, functions, and
  hooks linked from the programmer reference.

Result:

- 116 reachable official pages;
- 39 developer-guide pages;
- 77 generated-reference pages;
- 795 documented methods/functions indexed;
- 112 documented hook names indexed.

The repository stores a title/link map and symbol names, not a mirror of the
official prose or proprietary engine source.

## Upstream link observations

The official navigation exposed six failing targets at snapshot time:

- four generated `index.php` category links returned HTTP 502 while their
  clean category URLs worked;
- `default/temp.html` returned HTTP 404;
- a lowercase duplicate `help/Views/product.html` returned HTTP 404 while the
  canonical case-sensitive `help/Views/Product.html` worked.

These failures are recorded in the skill's documentation map and are not
treated as missing unique sections.

## Drift policy

Moguta.CMS documentation spans multiple release eras. The skill therefore
requires the agent to identify the installed version/edition and inspect the
exact target call site before implementing.

Re-run coverage research when:

- the official navigation changes;
- new Moguta.CMS version milestones appear;
- a symbol/hook lookup fails;
- the installed engine conflicts with the bundled reference.
