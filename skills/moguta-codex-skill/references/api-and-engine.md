# API and engine reference workflow

Use this reference for external API integrations and exact engine symbol/hook
lookup.

## Contents

- [External API boundary](#external-api-boundary)
- [Documented API operations](#documented-api-operations)
- [Batch and pagination limits](#batch-and-pagination-limits)
- [Integration design](#integration-design)
- [Engine lookup](#engine-lookup)
- [Documentation drift](#documentation-drift)

## External API boundary

The official guide says the Moguta.CMS external API is available in the
Hypermarket edition. A configured application uses a token, and the client
library also accepts a secret used to validate response signatures.

Do not place tokens or secrets in URLs, client-side JavaScript, repositories,
fixtures, logs, screenshots, or issue text. Although the wiki shows GET
examples, prefer HTTPS and a server-side transport that keeps credentials out
of access logs and browser history.

Official references:

- [API guide](https://wiki.moguta.ru/devhelp/api)
- [`mogutaApi`](https://wiki.moguta.ru/help/Libraries/mogutaApi.html)
- [`Controllers_Api`](https://wiki.moguta.ru/help/Controller/Controllers_Api.html)

## Documented API operations

The generated controller reference documents these operation names:

- connectivity: `test`;
- users: `getUsers`, `importUsers`, `deleteUser`, `findUser`;
- categories: `getCategory`, `importCategory`, `deleteCategory`;
- orders: `getOrder`, `importOrder`, `deleteOrder`;
- products: `getProduct`, `importProduct`, `deleteProduct`;
- custom fields: `createCustomFields`.

Treat operation names, aliases, payload fields, and response shapes as
version-specific. Search the installed `Controllers_Api` implementation before
building or changing a production integration.

## Batch and pagination limits

At the 2026-07-30 documentation snapshot, the controller reference states:

- paged users/categories/orders: maximum `count` 250;
- paged products: maximum `count` 100;
- user/category/order imports: recommended batches up to 100;
- product imports: maximum batches of 100.

These values can drift. Read the matching installed controller and implement
smaller configurable batches, retry/backoff, checkpointing, and deterministic
deduplication.

## Integration design

For every integration:

1. Confirm edition, version, API enablement, and application scope.
2. Store credentials in server-side secret storage.
3. Validate response status, error code, signature, and expected schema.
4. Use stable external IDs and idempotency rules for imports.
5. Page exports until an explicit end condition.
6. Bound batch size and request timeout.
7. Retry only safe/idempotent operations.
8. Log correlation IDs and counts, never secrets or full personal records.
9. Quarantine malformed records and continue only when partial processing is
   explicitly safe.
10. Reconcile totals and persist a restart checkpoint.

Test invalid token, invalid signature, API disabled, bad method, malformed
payload, empty result, partial batch, timeout, rate/size limit, duplicate
delivery, and schema drift.

## Engine lookup

Use [engine-symbol-index.md](engine-symbol-index.md) to locate the documented
class page, then inspect the target source for:

- visibility and static/instance calling style;
- parameters, defaults, and accepted shapes;
- return type and mutation side effects;
- hook creation before/after the method;
- exceptions, errors, cache, and database behavior;
- version-specific aliases or deprecated methods.

The bundled index covers 795 documented methods/functions and 112 hook names
from the research snapshot. It intentionally does not reproduce the full wiki
descriptions.

For a broad route or unfamiliar subsystem, use
[documentation-map.md](documentation-map.md).

## Documentation drift

The generated engine reference contains broken links and inconsistent anchors,
and some method pages can be older than newer narrative guides. Apply this
resolution rule:

1. installed source/call site;
2. official example bundled for the installed version;
3. class/method page;
4. narrative developer guide;
5. inference.

If behavior still cannot be confirmed, state the uncertainty and add a
minimal, reversible runtime probe rather than inventing a signature.
