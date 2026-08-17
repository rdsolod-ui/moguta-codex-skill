# Operations and upgrades

Use this reference for hosting, runtime compatibility, deployment, updates,
backups, rollback, hardening, and major-version migrations.

## Contents

- [Source and version boundary](#source-and-version-boundary)
- [Current runtime matrix](#current-runtime-matrix)
- [Major migration gates](#major-migration-gates)
- [Pre-change evidence](#pre-change-evidence)
- [Deployment and update workflow](#deployment-and-update-workflow)
- [Backup and recovery](#backup-and-recovery)
- [Nginx and filesystem hardening](#nginx-and-filesystem-hardening)
- [Docker boundary](#docker-boundary)
- [Post-release validation](#post-release-validation)
- [License-aware operations](#license-aware-operations)

## Source and version boundary

The official release history listed Moguta.CMS 13.1.1 on 2026-08-17. Treat
that as the current public release at the audit date, not as proof of the
version installed on a target site.

Before applying this reference, detect the installed `VER`, edition, PHP build,
ionCube Loader, database version, active/parent template, and plugin versions.
The installed files and runtime behavior take priority over a newer wiki page.

Official sources:

- [Version history](https://moguta.ru/blog/istoriya-versiy)
- [System requirements](https://wiki.moguta.ru/ustanovka-sistemy/sistemnye-trebovaniya)
- [System/update administration](https://wiki.moguta.ru/settings/sistema)
- [Update guide](https://wiki.moguta.ru/ustanovka-sistemy/obnovlenie-sistemi)

## Current runtime matrix

The system-requirements page checked on 2026-08-17 lists:

- Linux;
- MySQL 5.7.7+ with MySQL 8+ recommended;
- Apache with `mod_rewrite`, Apache behind Nginx, or pure Nginx;
- PHP 7.3, 7.4, 8.1, 8.2, 8.3, or 8.4;
- ionCube Loader 15.0.0;
- the documented JSON, XML, mbstring, OpenSSL, GD, curl, mysqli, ZIP,
  fileinfo, EXIF, and related PHP extensions.

PHP 8.0 is not in the documented list. The license explains that encrypted
product files can require a distribution built for the selected PHP line.
Never switch PHP first and hope the existing distribution will load.

## Major migration gates

- 8.15+: component templates, inheritance, `config.ini`, and the newer asset
  registration conventions.
- 10.9.0+: payment methods are plugins.
- 11.0+: PHP 8.1-8.3 support; templates and plugins also need compatible
  updates when moving to PHP 8.
- 12.0+: fiscalization, marking, second-receipt behavior, extra page fields,
  and the official Docker image.
- 13.0+: PHP 8.4 support, product/variant media changes, and mPDF replacing
  TCPDF. Regression-test custom invoices, acts, and other PDF layouts.
- 13.1+: support ended for old non-component templates. Migrate to a supported
  component template before relying on future engine updates.

Official release notes:

- [12.0.0](https://moguta.ru/blog/istoriya-versiy/reliz-moguta-cms-12-0-0)
- [13.0.0](https://moguta.ru/blog/istoriya-versiy/reliz-moguta-cms-13-0-0)
- [13.1.0](https://moguta.ru/blog/istoriya-versiy/reliz-moguta-cms-13-1-0)

## Pre-change evidence

Capture without exposing secrets:

1. active release path and Git commit or a file manifest/hash;
2. `VER`, edition, PHP, ionCube, database, web server, and enabled extensions;
3. active/parent template and whether it has `components/` and `config.ini`;
4. installed plugin versions and known custom payment/delivery integrations;
5. tracked or locally modified `mg-core` files;
6. cron, queues, webhooks, SMTP, payment callbacks, and external sync jobs;
7. database size, uploads size, available disk space, and backup destination;
8. current public/admin smoke results and rollback owner.

Do not print `config.ini`, database passwords, license keys, API tokens,
payment secrets, cookies, or customer data while collecting evidence.

## Deployment and update workflow

1. Create full file and database backups and prove they can be read.
2. Restore to an isolated copy or staging environment.
3. Reproduce the target PHP/ionCube/database matrix.
4. Inventory core edits and reconcile each one with an extension point or a
   documented rebase plan.
5. Update the engine, active template, and plugins as one compatibility set.
6. Run database migrations only after backup and rollback coordinates exist.
7. Clear application and browser asset caches where required.
8. Run the post-release matrix before changing the production traffic gate.
9. Keep the previous release and database rollback point until the acceptance
   window closes.

Do not claim success from an admin banner alone. Verify the active public
release, critical commerce routes, background jobs, and integrations.

## Backup and recovery

The admin UI can create file and database backups, but large sites can exceed
web-request time or storage limits. For production, also maintain an external
backup with:

- database dump consistency and restore command;
- product images, uploads, custom templates/plugins, and the exact engine
  distribution needed by the current PHP line;
- encryption at rest, restricted access, retention, and off-host storage;
- periodic restore tests with measured recovery time and data-loss window.

Do not keep the only backup inside the web root. The license states that old
distributions may not remain available after subscription expiry, so retaining
the verified file set is operationally important.

Official references:

- [Backups](https://wiki.moguta.ru/settings/rezervnye-kopii)
- [License](https://wiki.moguta.ru/ustanovka-sistemy/licenziya)

## Nginx and filesystem hardening

The official pure-Nginx page provides a routing starting point, not a complete
production security policy. Add rules appropriate to the installed version:

- deny secrets, backups, logs, dotfiles, repository metadata, and temporary
  archives;
- prevent PHP execution in uploads and writable media paths;
- allow PHP only through the intended front controller and admin/API routes;
- set request/body/time limits for imports and uploads deliberately;
- configure HTTPS, secure cookies, HSTS only after HTTPS is stable, and safe
  static-file caching;
- preserve required payment/API callback routes during restrictions.

The update guide mentions temporarily using CHMOD 777. Prefer the narrowest
writable paths with the correct web-server owner. If broad access is
unavoidable during a vendor update, time-box it, record it, and restore least
privilege immediately afterward.

Official reference: [Pure Nginx installation](https://wiki.moguta.ru/ustanovka-sistemy/ustanovka-na-chistyy-nginx-bez-apache)

## Docker boundary

The official Docker quick start is useful for evaluation, but its examples
show default database credentials and an optional browser database manager.
For production:

- pin the image by an audited immutable reference when available;
- override every credential through protected secret delivery;
- keep `DBMS=off` and do not expose database/admin ports publicly;
- verify exactly which application, upload, search-index, and database data the
  official all-in-one image keeps in each mount; do not assume one web-root
  volume covers a consistent database backup;
- isolate networks, use explicit persistent volumes, and define ownership;
- use a restart policy, health check, resource/PID limits, log rotation,
  `no-new-privileges`, reduced capabilities, and a read-only filesystem where
  the audited image permits them; never mount the Docker socket;
- place TLS, backups, monitoring, log rotation, health checks, and resource
  limits outside the one-line quick start;
- rehearse image upgrade and rollback with the persisted database/files.

Official reference: [Docker installation](https://wiki.moguta.ru/ustanovka-sistemy/ustanovka-iz-docker-image)

## Post-release validation

Test at minimum:

- public home, catalog, category, product, search, 404, login, and account;
- cart add/update/remove and order submission;
- every enabled payment and delivery path, including failed and duplicate
  callbacks;
- admin login, product/order editing, permissions, imports, and cache clear;
- SMTP and transactional messages;
- cron/background jobs and 1C, RetailCRM, API, CSV/YML, or other active sync;
- component/parent-template fallback, combined assets, and mobile/desktop;
- custom PDFs after 13.0 and all legacy-template paths before 13.1+ rollout;
- negative checks proving that DBMS, secrets, dumps, repository metadata, and
  PHP execution in upload paths are not exposed;
- error logs, response codes, cache hit/miss behavior, and disk growth.

Record the active release hash, checks, failures, manual gates, and rollback
status. A syntax-only check is not production validation.

If production accepted new orders or payments after cutover, do not blindly
restore an older database. Freeze writes and reconcile the new transactions
before a database rollback.

## License-aware operations

The official license allows modification of the downloaded instance but warns
that modifications can affect support and updates. It prohibits decrypting or
reverse-engineering encrypted components. Work through documented open
extension layers and observable runtime behavior; do not attempt to extract
protected source.

Before giving support staff access, create a complete backup. Rotate temporary
credentials after the support window and never store their values in Git,
Markdown, screenshots, logs, or issue text.
