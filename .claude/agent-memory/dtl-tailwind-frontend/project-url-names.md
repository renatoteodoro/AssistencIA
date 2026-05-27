---
name: project-url-names
description: Known URL names and namespaces registered in the AssistencIA project for use in {% url %} tags
metadata:
  type: project
---

URL names confirmed from urls.py files:

**Flat (no namespace) — users app and core:**
- `home` — HomeView (core), public landing page, path `/`
- `dashboard` — authenticated dashboard (core), path `dashboard/`
- `login` — CustomLoginView, template `auth/login.html`, path `users/login/`
- `register` — RegisterView, template `auth/register.html`, path `users/register/`
- `logout` — LogoutView, path `users/logout/`

**Namespaced apps (Sprint 3+ task spec defines these):**
- `accounts:account_list` — namespace `accounts`, app `accounts`
- `categories:category_list` — namespace `categories`, app `categories`
- `transactions:transaction_list` — namespace `transactions`, app `transactions`
- `users:logout` — confirmed in use: `app.html` (layouts) uses this form, so `app_name = 'users'` is set in users/urls.py

**Active state detection in sidebar:**
- Dashboard: `request.resolver_match.url_name == 'dashboard'`
- Accounts / Categories / Transactions: `request.resolver_match.namespace == '<app_name>'`

**Why:** users/urls.py had no app_name in earlier sprints. Task 3.2 spec uses `users:logout` — verify if app_name was added. Namespaced apps (accounts, categories, transactions) are defined in Sprint 3 task spec.

**How to apply:** When writing nav links or form actions, verify the relevant urls.py for app_name. Do not assume namespace exists without checking. Task specs may use namespaced forms; always cross-check against the actual urls.py.
