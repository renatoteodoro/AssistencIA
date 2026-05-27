---
name: project-url-names
description: Known URL names registered in the AssistencIA project for use in {% url %} tags
metadata:
  type: project
---

URL names confirmed from users/urls.py and core/urls.py:

- `login` — CustomLoginView, template `auth/login.html`, path `users/login/`
- `register` — RegisterView, template `auth/register.html`, path `users/register/`
- `logout` — LogoutView, path `users/logout/`

**Why:** These are the only URL names currently wired up (Sprint 1). Template `{% url %}` tags must use these exact names.

**How to apply:** When writing nav links or form actions, use these names. Do not invent names like `users:login` or `auth:login` — there are no namespaces yet.
