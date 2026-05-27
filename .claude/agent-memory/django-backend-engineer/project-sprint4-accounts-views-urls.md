---
name: project-sprint4-accounts-views-urls
description: Sprint 4.3/4.4 — Accounts CBVs and URL routing implemented
metadata:
  type: project
---

Tasks 4.3 and 4.4 are complete. Four CBVs in `accounts/views.py`, `accounts/urls.py` created, and `core/urls.py` updated.

**AccountListView** — ListView, filters by `user=request.user` in `get_queryset()`.

**AccountCreateView** — CreateView with `AccountForm`; assigns `form.instance.user = self.request.user` in `form_valid` before calling super. `success_url = reverse_lazy('accounts:account_list')`.

**AccountUpdateView** — UpdateView with `AccountForm`; `get_queryset()` scoped to `user=request.user` for ownership enforcement.

**AccountDeleteView** — DeleteView; overrides `post()` to check `account.transactions.exists()` before deleting. Uses `try/except AttributeError` because the `Transaction` model FK to `Account` is not yet defined (Sprint 5). On conflict, adds `messages.error` and redirects without deleting.

**URL namespace** — `app_name = 'accounts'`; included in `core/urls.py` as `path('accounts/', include('accounts.urls', namespace='accounts'))`.

**Template names expected** (not yet created — frontend sprint):
- `accounts/account_list.html`
- `accounts/account_form.html`
- `accounts/account_confirm_delete.html`

**Why:** `try/except AttributeError` on `account.transactions` is intentional — the reverse relation only exists once `transactions.Transaction` defines its FK to `Account`. The guard will work transparently once Sprint 5 creates that model.

**How to apply:** When Sprint 5 adds `Transaction.account = ForeignKey(Account, related_name='transactions', ...)`, the guard in `AccountDeleteView.post()` will activate automatically with no changes needed here.

See also: [[project-sprint4-accounts-model]]
