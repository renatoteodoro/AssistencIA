---
name: project-sprint6-transactions
description: Sprint 6 — Transaction model, form, views, and URLs; migration 0001_initial applied
metadata:
  type: project
---

Sprint 6 implemented the `transactions` app (tasks 6.1–6.4).

**Model** (`transactions/models.py`): `Transaction` with FKs to `accounts.Account` and `categories.Category` (both via string references), `user` FK to `settings.AUTH_USER_MODEL`. Fields: `description`, `amount` (DecimalField 12,2), `transaction_type` (income/expense choices), `date` (DateField), audit fields. `Meta.ordering = ['-date', '-created_at']`.

**Admin** (`transactions/admin.py`): `@admin.register` with `list_display` for description, user, account, category, transaction_type, amount, date.

**Form** (`transactions/forms.py`): `TransactionForm` — `__init__` pops `user` kwarg and filters both `account` and `category` querysets by that user. DateInput uses `type="date"` attr alongside `_INPUT_CLASSES`.

**Views** (`transactions/views.py`): Four CBVs — `TransactionListView` supports GET filter params (`month`, `year`, `account`, `category`) with try/except guards for invalid values; injects `accounts`, `categories`, and current filter values into context. Create/Update/Delete follow the standard pattern from categories.

**URLs** (`transactions/urls.py`): `app_name = 'transactions'`; routes: `list/`, `new/`, `<pk>/edit/`, `<pk>/delete/`.

**core/urls.py**: Added `transactions/` path with multi-line formatting to stay under 79 chars.

**Migration**: `transactions/migrations/0001_initial.py` — applied cleanly. `flake8` and `manage.py check` both pass with 0 issues.

**Why:** Completes the core data entry layer; categories/accounts deletion guards already rely on `category.transactions.exists()` and `account.transactions.exists()` via the `related_name='transactions'` set here.

**How to apply:** When building dashboard aggregations or reports in Sprint 7, query `Transaction.objects.filter(user=request.user)` — the model ordering is already `-date, -created_at`.
