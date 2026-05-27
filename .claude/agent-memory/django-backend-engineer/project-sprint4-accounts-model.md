---
name: project-sprint4-accounts-model
description: Sprint 4.1 — Account model created in accounts app with choices, audit fields, admin registration, and migration applied
metadata:
  type: project
---

Task 4.1 implemented the `Account` model in `accounts/models.py`.

Fields: `user` (FK → settings.AUTH_USER_MODEL, CASCADE, related_name='accounts'), `name` (CharField, max_length=100), `account_type` (CharField, choices: checking/savings/wallet), `initial_balance` (DecimalField, max_digits=12, decimal_places=2, default=0), `created_at`, `updated_at`.

Choices defined as class-level constants (`CHECKING`, `SAVINGS`, `WALLET`) before the fields per project convention.

`Meta.ordering = ['-created_at']`. `__str__` returns `self.name`.

Admin registered via `@admin.register(Account)` with `list_display = ['name', 'account_type', 'initial_balance', 'user']`.

Migration `accounts/migrations/0001_initial.py` generated and applied successfully. Uses `swappable_dependency(settings.AUTH_USER_MODEL)` — correct FK pattern.

**Why:** Foundational model for the accounts feature; will be referenced by transactions app.

**How to apply:** When building accounts views/forms (Sprint 4.2+), the `account_type` choices are accessed as `Account.CHECKING`, `Account.SAVINGS`, `Account.WALLET`. The `initial_balance` field is the starting balance — computed current balance will require aggregating transactions on top of it.
