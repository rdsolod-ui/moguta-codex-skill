# Security policy

## Supported version

Security fixes are applied to the latest release.

## Report a vulnerability

Use GitHub private vulnerability reporting for this repository. Do not publish
credentials, Moguta.CMS license data, API/payment secrets, cookies, private
customer records, production database exports, or exploitable store details in
a public issue.

## Public-repository boundary

This repository must not contain:

- database configuration or backups;
- API, payment, delivery, SMTP, CRM, or marketplace credentials;
- authenticated browser state or cookies;
- production uploads, logs, orders, customers, or product exports;
- proprietary Moguta.CMS engine or paid-plugin source;
- instructions that bypass Moguta licensing or plugin authorization.

The repository validator detects common leaks, but maintainers must review
every change before publication.

## Skill behavior

The bundled inspector is read-only. It reports structure, version candidates,
metadata, tracked core changes, UTF-8 BOMs, and a narrow dynamic-SQL heuristic.
It does not prove that a Moguta.CMS installation or extension is secure.
