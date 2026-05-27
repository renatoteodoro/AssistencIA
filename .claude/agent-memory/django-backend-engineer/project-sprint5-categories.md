---
name: project-sprint5-categories
description: Sprint 5 — Category model, admin, form, views, and URLs for the categories app (tasks 5.1–5.4 complete)
metadata:
  type: project
---

Category model uses INCOME/EXPENSE choices (max_length=10), ForeignKey to AUTH_USER_MODEL with related_name='categories', and Meta ordering=['name'].

CategoryForm pops 'user' from kwargs (same pattern as AccountForm) even though category has no relational fields that need filtering — future-proofed for views that pass user=request.user. Select widget for category_type uses the same _SELECT_CLASSES constant pattern from accounts/forms.py.

Migration: categories/migrations/0001_initial.py — applied cleanly.

Tasks 5.3/5.4: 4 CBVs in categories/views.py (List, Create, Update, Delete), all with LoginRequiredMixin. Create and Update override get_form_kwargs() to pass user=self.request.user to CategoryForm. Delete guards against linked transactions via category.transactions.exists() with try/except AttributeError (same pattern as AccountDeleteView). categories/urls.py created with app_name='categories'. core/urls.py updated with path('categories/', include('categories.urls', namespace='categories')).

Related: [[project-sprint4-accounts-views-urls]]
