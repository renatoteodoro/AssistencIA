---
name: project-sprint5-categories
description: Sprint 5.1/5.2 — Category model, admin, form, and migration for the categories app
metadata:
  type: project
---

Category model uses INCOME/EXPENSE choices (max_length=10), ForeignKey to AUTH_USER_MODEL with related_name='categories', and Meta ordering=['name'].

CategoryForm pops 'user' from kwargs (same pattern as AccountForm) even though category has no relational fields that need filtering — future-proofed for views that pass user=request.user. Select widget for category_type uses the same _SELECT_CLASSES constant pattern from accounts/forms.py.

Migration: categories/migrations/0001_initial.py — applied cleanly.

Flake8 note: categories/tests.py and categories/views.py have pre-existing Django boilerplate unused imports — not introduced by this sprint, not fixed here (out of scope).

Related: [[project-sprint4-accounts-model]]
