# Core development workflow

Use this reference for architecture, security, database, caching, routing,
version compatibility, and release validation.

## Contents

- [Source priority](#source-priority)
- [Project reconnaissance](#project-reconnaissance)
- [MVC and extension boundaries](#mvc-and-extension-boundaries)
- [Database safety](#database-safety)
- [Input and output safety](#input-and-output-safety)
- [Assets and caching](#assets-and-caching)
- [Pages and routes](#pages-and-routes)
- [Version and edition gates](#version-and-edition-gates)
- [Validation matrix](#validation-matrix)

## Source priority

Use this order when facts conflict:

1. the user's current requirement;
2. the installed Moguta.CMS source and runtime behavior;
3. tests and a reproducible local/staging probe;
4. documentation for the matching version;
5. the current public wiki;
6. assumptions.

The public developer wiki is useful but internally mixed. It contains examples
for older releases, newer sections such as the 12.0.0 payment notes, broken
generated-reference links, inconsistent hook casing, and occasional typos.
Never copy an example without checking the installed call site.

Official starting points:

- [Developer documentation](https://wiki.moguta.ru/devhelp)
- [MVC overview](https://wiki.moguta.ru/devhelp/mvc)
- [Programmer reference](https://wiki.moguta.ru/devhelp/manual)

## Project reconnaissance

Identify these coordinates before editing:

- project root and Git state;
- `VER` or another installed-version marker;
- product edition and enabled feature set;
- PHP and database versions;
- active template and its parent/standard inheritance;
- target plugin folder, metadata, activation state, and schema version;
- deployment and rollback process;
- existing test, lint, and smoke commands.

Typical roots and extension paths:

```text
mg-core/        engine implementation
mg-admin/       administration UI
mg-plugins/     plugins
mg-templates/   public templates
mg-pages/       engine-managed custom pages
```

Do not read or print database passwords, API keys, cookies, or payment secrets
while discovering the version.

## MVC and extension boundaries

Moguta.CMS separates models, views, and controllers. Models own entity and
database logic, controllers prepare `$data`, and views render it.

Prefer extensions over copied core behavior:

- attach plugin or template handlers to existing hooks;
- change markup through a template view, layout, or component;
- put reusable template functions and hook registration in `functions.php`;
- create engine-managed public pages under `mg-pages`;
- override a model/controller only when a stable hook cannot implement the
  requirement.

Template copies of core models/controllers drift when the engine is upgraded.
If an override is required, record the upstream file/version it was based on
and add a comparison step to the upgrade checklist.

Official references:

- [Engine-generated pages](https://wiki.moguta.ru/devhelp/templates/stranitsy-formiruemye-dvijkom)
- [`$data` in templates](https://wiki.moguta.ru/devhelp/templates/massiv-peredavaemyh-dannyh-data)

## Database safety

Route engine queries through `DB::query()` and use `PREFIX` for engine tables.
Choose the quote method by value shape:

| Dynamic fragment | Required helper |
| --- | --- |
| string | `DB::quote()` |
| integer | `DB::quoteInt()` |
| decimal/float | `DB::quoteFloat()` |
| values in `IN (...)` | `DB::quoteIN()` |

Do not interpolate `$_GET`, `$_POST`, `$_REQUEST`, cookies, API payloads, or
untrusted plugin settings into SQL. Do not use `DB::quote()` as a substitute
for type validation or output encoding.

For writes:

- validate the complete input contract;
- use a unique plugin table prefix/name;
- make activation and schema migration repeatable;
- protect destructive operations with an explicit scope;
- preserve existing data during upgrade and rollback;
- test empty, duplicate, malformed, and concurrent cases.

Official references:

- [SQL safety guide](https://wiki.moguta.ru/devhelp/sql)
- [`DB` class](https://wiki.moguta.ru/help/Libraries/DB.html)

## Input and output safety

Treat every public route, shortcode attribute, AJAX request, API payload, file
upload, and saved option as untrusted.

- Check the user's authorization and the intended action before mutation.
- Validate required keys, types, ranges, identifiers, and allowed values.
- Reject unexpected file types and store uploads outside executable paths when
  possible.
- Encode HTML output for its context; do not confuse SQL quoting or input
  cleanup with HTML/attribute/URL encoding.
- Avoid revealing exception traces, SQL, paths, tokens, or customer data.
- Keep state-changing actions idempotent where callbacks or retries can repeat.

Inspect the target engine's existing admin and public handlers for its exact
authorization and request-validation conventions.

## Assets and caching

Register styles and scripts with `mgAddMeta()` so Moguta.CMS can order,
deduplicate, inherit, and merge them. Use the syntax supported by the installed
version. `mgExcludeMeta()` is documented for template exclusions from 7.2+.

Cache expensive queries or computation with `Storage::get()` and
`Storage::save()`. A cache implementation is incomplete without:

- a deterministic, namespaced key;
- all inputs that change the result represented in the key;
- an invalidation path on create/update/delete/config change;
- a safe miss path;
- a test that stale data is not returned.

Official references:

- [External JS/PHP integration](https://wiki.moguta.ru/devhelp/podklyuchenie-storonnih-js-i-php-skriptov)
- [Caching](https://wiki.moguta.ru/devhelp/keshiruyte-dannye)
- [`Storage` class](https://wiki.moguta.ru/help/Libraries/Storage.html)

## Pages and routes

Prefer `mg-pages/<name>.php` for an engine-managed custom page. It becomes
available at the corresponding clean URL and keeps the engine bootstrap and
security boundary.

The wiki also documents `.htaccess` exclusions for running PHP outside the
engine. Treat that as an exceptional integration path: verify the need,
bootstrap/authentication boundary, web-server configuration, direct-access
security, and deployment behavior before using it.

Official references:

- [`mg-pages` pages](https://wiki.moguta.ru/devhelp/sozdanie-stranits/sozdanie-stranits-sayta)
- [Direct PHP exception](https://wiki.moguta.ru/devhelp/kak-zapustit-php-skript-iz-kornevoy-direktorii-ili-lyuboy-papki-na-servere)

## Version and edition gates

Known documentation milestones are navigation hints, not a substitute for
source verification:

- 7.2+: per-template meta exclusions are documented;
- 8.15+: template components, `config.ini`, inheritance, template-bundled
  plugins, and newer `mgAddMeta()` path syntax are documented;
- 8.6+: the customizable order form is documented, with edition fallback;
- 10.9.0+: payment methods are documented as plugins;
- 12.0.0+: the payment guide adds marking, fiscalization, and second-receipt
  behavior;
- the external API guide says the API is available in the Hypermarket edition.

Confirm each gate in the installed source and license/edition before using it.

## Validation matrix

For every change, choose applicable checks:

- `php -l` on changed PHP;
- project inspector before and after;
- unit/static/integration tests;
- plugin activate, deactivate, reactivate, and upgrade;
- schema creation on clean install and migration on populated install;
- admin/public success and failure routes;
- unauthorized and malformed AJAX/API requests;
- cache hit, miss, invalidation, and disabled-cache behavior;
- desktop/mobile and affected commerce flows;
- payment/delivery webhook replay, invalid signature, timeout, and retry;
- Git diff for core edits, secrets, uploads, caches, and unrelated files.

Do not report production readiness when only syntax or a happy path was tested.
