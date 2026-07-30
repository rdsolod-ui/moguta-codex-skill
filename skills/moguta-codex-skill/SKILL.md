---
name: moguta-codex-skill
description: Develop, inspect, debug, modernize, and review Moguta.CMS PHP projects, including plugins, templates/themes, hooks, shortcodes, AJAX handlers, API integrations, payment and delivery extensions, MVC overrides, database access, caching, and version compatibility. Use for repositories or tasks mentioning Moguta, Moguta.CMS, mg-core, mg-plugins, mg-templates, mg-pages, Pactioner.php, pageplugin.php, mgAddAction, mgAddShortcode, mgAddMeta, Models_*, Controllers_*, or the Moguta developer API.
---

# Moguta.CMS development

Use the installed project and its exact Moguta.CMS version as the primary
technical truth. Treat the bundled references as a researched navigation layer
over the official documentation, not as a substitute for the target source.

## Start with evidence

1. Resolve the actual project root and preserve unrelated user changes.
2. Run the read-only inspector:

   ```bash
   python3 scripts/inspect_moguta.py /path/to/moguta-project
   ```

3. Inspect `git status`, the active template, the target plugin, the `VER`
   constant or other installed version marker, PHP/runtime constraints, and
   available tests.
4. Classify the request as core behavior, plugin, template, page, API,
   payment, delivery, data migration, or diagnosis.
5. Search the installed code for the exact class, method, hook, route, and
   calling convention before implementing.
6. Open only the reference needed for the current task.

## Route the task

- Read [core-development.md](references/core-development.md) for architecture,
  security, SQL, caching, pages, version gates, and validation.
- Read [plugins.md](references/plugins.md) for plugin metadata, lifecycle,
  hooks, shortcodes, AJAX, payment, and delivery work.
- Read [templates.md](references/templates.md) for template structure,
  components, inheritance, assets, views, layouts, and `config.ini`.
- Read [api-and-engine.md](references/api-and-engine.md) for external API work,
  engine classes, method lookup, and hooks.
- Search [engine-symbol-index.md](references/engine-symbol-index.md) when an
  exact documented function, method, class, or hook must be located.
- Search [documentation-map.md](references/documentation-map.md) when the task
  needs the canonical official page or broader coverage.

For large reference files, search before reading:

```bash
rg -n "Models_Order|Models_Payment|mgAddAction|hook-name" references/
```

## Choose the least fragile extension point

Prefer, in order:

1. an existing plugin extension point or hook;
2. an existing template component, layout, `functions.php`, or view override;
3. an `mg-pages` route for a new engine-managed page;
4. a narrowly scoped model/controller override only when no stable hook or
   view-level solution exists.

Do not edit `mg-core` for a normal customization. If a core change is
unavoidable, isolate it, document why no extension point works, and provide an
upgrade/rebase procedure.

## Enforce the version gate

Do not infer compatibility from a current-looking wiki example.

- Verify the installed version and edition.
- Compare the installed implementation with the official page.
- Preserve old/new branches when the project must support multiple versions.
- Treat documented milestones as gates: template components and inheritance
  start at 8.15; payment methods become plugins at 10.9.0; the payment guide
  adds 12.0.0 fiscalization and receipt behavior.
- Treat spelling, case, callback arguments, return values, and metadata keys as
  source-sensitive. Confirm them in the installed engine or a bundled official
  example.

## Protect security and upgrades

- Use `PREFIX` and the appropriate `DB::quote*` method for every dynamic SQL
  fragment. Never interpolate request data into SQL.
- Validate authorization, intent, input shape, and output encoding for AJAX and
  public routes.
- Keep API tokens, payment secrets, credentials, production data, and config
  values out of commits, logs, fixtures, and responses.
- Register CSS/JS through `mgAddMeta()` and remove assets through
  `mgExcludeMeta()` only when the target version supports the behavior.
- Cache expensive work through `Storage` with deterministic keys and explicit
  invalidation.
- Keep plugin identifiers, PHP classes, shortcodes, tables, and routes uniquely
  namespaced.
- Preserve hook results and return the required value for hooks that wrap a
  function result.

## Validate the change

Run the narrowest complete matrix available:

1. PHP syntax checks for every changed PHP file.
2. The inspector again, using `--strict` for release checks.
3. Existing unit/integration tests and static analysis.
4. Activation/deactivation and upgrade checks for plugins.
5. Public and admin AJAX success, invalid-input, and unauthorized cases.
6. Desktop/mobile rendering for templates, plus cart, catalog, product, order,
   login, and account flows affected by the change.
7. Cache-disabled and cache-enabled behavior.
8. API/webhook signature, retry, idempotency, and failure behavior where
   relevant.
9. A clean diff confirming that `mg-core`, secrets, generated caches, uploads,
   and unrelated files were not changed accidentally.

Report the detected version/edition, chosen extension point, files changed,
checks executed, compatibility assumptions, and any remaining manual or
production-only verification.
