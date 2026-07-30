# Plugin development

Use this reference for plugin structure, lifecycle, hooks, shortcodes, AJAX,
delivery, payment, packaging, and upgrade safety.

## Contents

- [Structure and identity](#structure-and-identity)
- [Lifecycle and storage](#lifecycle-and-storage)
- [Hooks](#hooks)
- [Shortcodes](#shortcodes)
- [AJAX](#ajax)
- [Delivery plugins](#delivery-plugins)
- [Payment plugins](#payment-plugins)
- [Packaging and validation](#packaging-and-validation)

## Structure and identity

The only universally required plugin file is `index.php`, beginning with the
metadata block expected by Moguta.CMS. The official guide documents fields for
name, description, author, version, and an optional update restriction.

Common structure:

```text
plugin-folder/
├── index.php
├── Pactioner.php
├── pageplugin.php
├── readme.txt
├── css/
├── js/
├── locales/
├── src/
└── views/
```

Only add files needed by the plugin. Keep `index.php` in UTF-8 without BOM.
Namespace the folder, PHP class, option keys, table names, JavaScript module,
shortcode, route, and cache keys to avoid collisions.

The wiki recommends starting from its official plugin blank, but that archive
can change. Inspect and security-review the downloaded version before use; do
not treat it as trusted application code merely because it is official.

Official references:

- [Plugin structure](https://wiki.moguta.ru/devhelp/plugins/struktura-faylov-plagina)
- [Quick start](https://wiki.moguta.ru/devhelp/plugins/kak-sdelat-plagin)
- [Official blank](https://wiki.moguta.ru/devhelp/plugins/zagotovka-dlya-plagina)

## Lifecycle and storage

Make activation and upgrade repeatable:

- create tables/indexes only when missing;
- store a plugin schema version;
- migrate existing rows without destructive defaults;
- do not silently delete business data on deactivation;
- make reactivation safe;
- define an explicit uninstall policy;
- use `PREFIX` and quoted values for every query.

If the plugin must be listed or distributed through Moguta's ecosystem, verify
the current partner/allowlist and marketplace requirements. The developer wiki
states that development plugin folders may need approval for a specific site.

Official reference: [Allowing a plugin for clients](https://wiki.moguta.ru/devhelp/plugins/kak-razreshit-ispolzovanie-plagina-klientam)

## Hooks

Register handlers through `MG::addAction()` or its current global wrapper.
Confirm the exact hook name, case, argument mode, priority, and return contract
at the installed `MG::createHook()` call site.

For result-wrapping hooks, the documented handler receives one structure with
the original result and arguments and must return the replacement/preserved
result. Never drop the original result accidentally.

Hook-name examples in prose are not consistently cased. The wiki explains
method hooks as class and method joined with `_`, commonly lowercased in
registration examples, while the generated hook index displays mixed case.
Use the literal string executed by the installed engine.

Official references:

- [Hooks and shortcodes](https://wiki.moguta.ru/devhelp/plugins/huki-i-obrabotchiki)
- [Handling a hook](https://wiki.moguta.ru/devhelp/plugins/kak-obrabotat-huk-dvijka)
- [Hook index](https://wiki.moguta.ru/help/Hooks)

## Shortcodes

Register a unique lowercase shortcode and keep rendering deterministic.

- Parse only documented attributes.
- Apply defaults and validate enumerated/range values.
- Escape output for HTML, attribute, and URL contexts.
- Avoid unbounded database work on every render.
- Cache stable output and invalidate it on relevant changes.
- Test paired/unpaired forms and content inserted by the admin editor.

The wiki notes that shortcode attributes inserted through the admin editor use
double quotes.

## AJAX

The official blank routes plugin AJAX through `Pactioner.php`. Follow the
installed action router rather than inventing a direct executable PHP endpoint.

For every action:

- enforce admin/public authorization separately;
- validate the requested operation and every parameter;
- reject unexpected fields and unsafe file paths;
- quote all SQL;
- return the engine's normal structured response;
- avoid leaking stack traces or secrets;
- make retries safe for state-changing operations.

Official reference: [Public AJAX example](https://wiki.moguta.ru/devhelp/plugins/kak-otpravit-ajax-zapros-v-plagin-primer)

## Delivery plugins

The official delivery guide requires a complete flow, not only a price API:

1. render the calculator on checkout;
2. calculate from cart and user-entered delivery data;
3. recalculate when the cart changes;
4. validate before order submission;
5. persist the chosen service/data and final cost;
6. handle order creation in the public flow;
7. account for admin-created/edited orders where hook arguments can differ.

Do not trust a browser price when saving an order. Recalculate or verify the
server-side quote, bind it to the cart/address/options, define expiration, and
handle provider timeout/failure.

Official references:

- [Delivery plugin guide](https://wiki.moguta.ru/devhelp/plugins/instruktsiya-po-razrabotke-plagina-dostavki)
- [Delivery plugin hook](https://wiki.moguta.ru/devhelp/plugins/plagin-dostavki)

## Payment plugins

Payment methods are documented as plugins from 10.9.0. Verify the site uses
the plugin-based payment system before editing.

The current guide describes:

- plugin metadata marking the extension as a payment plugin;
- activation that creates or resolves the payment record;
- a payment-form handler;
- a `Models_Payment_handleRequest` webhook handler;
- `Controllers_Payment::actionWhenPayment()` after provider verification;
- 12.0.0 additions for marking, fiscalization, receipt data, and a second
  receipt hook.

The guide currently shows an unusual metadata spelling for the payment marker.
Confirm the exact key in the installed parser or official example instead of
normalizing it by intuition.

For webhooks:

- verify the provider signature and event type;
- obtain/verify the payment status server-to-server when supported;
- match merchant, currency, amount, order, and environment;
- make duplicate delivery idempotent;
- record a safe event identifier, not secrets or full payment data;
- return the provider-required status only after durable processing;
- test invalid signature, wrong amount, replay, timeout, and out-of-order events.

Official references:

- [Payment plugin guide](https://wiki.moguta.ru/devhelp/plugins/razrabotka-sposoba-oplaty)
- [`Models_Payment`](https://wiki.moguta.ru/help/Model/Models_Payment.html)
- [`Controllers_Payment`](https://wiki.moguta.ru/help/Controller/Controllers_Payment.html)

## Packaging and validation

Before release:

- lint all PHP and JavaScript;
- activate on a clean compatible installation;
- upgrade a populated prior version;
- deactivate/reactivate without data loss;
- verify admin settings and localization;
- validate public and admin AJAX authorization;
- test with caching/asset merging on and off;
- check no secrets, logs, uploads, backups, or production data are packaged;
- document minimum/maximum tested Moguta.CMS and PHP versions;
- verify the plugin folder name is allowed where Moguta licensing requires it.
