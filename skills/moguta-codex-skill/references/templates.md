# Template development

Use this reference for work under `mg-templates`, including components,
layouts, views, assets, inheritance, settings, and compatibility.

## Contents

- [Structure](#structure)
- [Rendering and assets](#rendering-and-assets)
- [Views, layouts, and data](#views-layouts-and-data)
- [Components and inheritance](#components-and-inheritance)
- [`config.ini`](#configini)
- [AJAX and functions](#ajax-and-functions)
- [Compatibility and release checks](#compatibility-and-release-checks)

## Structure

A recognized template requires:

```text
template.php
css/style.css
```

Common optional paths are:

```text
404.php
ajaxuser.php
functions.php
components/
controllers/
css/
images/
js/
layout/
locales/
models/
views/
config.ini
```

Keep presentation in views/components/layouts. Avoid copying core models and
controllers unless no stable extension point exists; copied logic must be
reconciled on every engine upgrade.

Official references:

- [Template structure](https://wiki.moguta.ru/devhelp/templates/kak-ustroeny-shablony)
- [Quick start](https://wiki.moguta.ru/devhelp/templates/sozdat-svoy-shablon-za-5-minut-bystryy-start)

## Rendering and assets

Place the page shell in `template.php`. Preserve the engine insertion points:

- `mgMeta(...)` for metadata, CSS, JavaScript, and supported core assets;
- `layout('content')` or the matching layout call for page content.

Register template/component assets with `mgAddMeta()` rather than raw tags.
The newer path-only syntax is documented for 8.15+ templates with
`config.ini`; older installations use a complete tag string. Verify the active
syntax in the installed template and engine.

Use `mgExcludeMeta([...])` only for an intentional replacement, and confirm
that removing the asset does not break another plugin or route.

Official references:

- [CSS/JS loading](https://wiki.moguta.ru/devhelp/templates/podklyuchenie-css-js)
- [Overriding/excluding assets](https://wiki.moguta.ru/devhelp/templates/pereopredelenie-podklyuchaemyh-js-iz-dvijka)
- [Engine constants](https://wiki.moguta.ru/devhelp/templates/direktivy-dvijka)

## Views, layouts, and data

Core public pages include cart, catalog, compare, enter, feedback, forgotpass,
group, index, order, payment, and personal. Override only the corresponding
file needed by the active template and preserve the expected `$data` contract.

Use layouts for reusable markup that the engine already exposes. Use
components for encapsulated PHP markup plus component-specific CSS/JS.

Before adding a query in a view:

1. inspect `$data`;
2. inspect the standard template call;
3. prefer a hook or reusable function to prepare missing data;
4. query directly only when necessary, with `DB::quote*`, caching, and bounded
   results.

Official references:

- [Engine pages](https://wiki.moguta.ru/devhelp/templates/stranitsy-formiruemye-dvijkom)
- [Layouts in `template.php`](https://wiki.moguta.ru/devhelp/templates/vstavki-komponentov-shablona-v-template-php)
- [`$data`](https://wiki.moguta.ru/devhelp/templates/massiv-peredavaemyh-dannyh-data)

## Components and inheritance

Components and inheritance are documented from 8.15.

`component()` accepts the component path, a data array, and an optional file
name. Inspect the standard template to learn the expected data contract for a
standard component.

Resolution can fall through:

1. active template;
2. configured parent template;
3. `moguta-standard`.

For a child template, copy only the files being changed and preserve the same
relative path. This reduces upgrade drift.

Official references:

- [Components](https://wiki.moguta.ru/devhelp/templates/komponenty)
- [Inheritance](https://wiki.moguta.ru/devhelp/templates/nasledovanie)

## `config.ini`

For component-based templates from 8.15, the documented sections are:

- `[MAIN]`: parent/standard inheritance and color-file strategy;
- `[COLORS]`: default CSS-variable schemes;
- `[SETTINGS]`: engine-setting overrides applied by the template;
- `[MISC]`: template-owned variables.

Important `[MAIN]` keys include:

- `TEMPLATE_INHERIT_FROM`;
- `TEMPLATE_INHERIT_FROM_STANDARD`;
- `TEMPLATE_COLOR_FILES`.

Treat `[SETTINGS]` as a migration with user impact: changing thumbnail sizes or
other global settings can affect existing data and generated media. Document
defaults and rollback.

Read `[MISC]` through the installed engine's `templateVars` convention. Do not
store secrets in template configuration.

Official reference: [`config.ini`](https://wiki.moguta.ru/devhelp/templates/fayl-nastroek-shablona-config-ini)

## AJAX and functions

Use `functions.php` for template-local helpers and hook registration.

The legacy template guide documents `ajaxuser.php` with a class extending
`Actioner`, called through the engine AJAX route. Confirm the current action
router, access checks, request shape, and response convention in the installed
version before implementing.

Do not expose an action merely because the router can call it. Validate
authorization, intent, types, identifiers, and error responses.

## Compatibility and release checks

Test at least:

- active, parent, and standard fallback resolution;
- CSS/JS deduplication and load order;
- 404 and affected engine pages;
- mobile and desktop widths;
- catalog, product, cart, order, login, and personal-account paths affected;
- template switch away and back;
- component missing-file fallback;
- no PHP warnings with representative empty and populated `$data`;
- cache merge enabled and disabled;
- clean install and upgrade from the oldest supported version.

The wiki's long “update to 7+” article is historical and template-specific.
Use it as a symptom checklist, then diff against the current standard template
instead of applying it mechanically.
