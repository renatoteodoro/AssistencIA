---
name: project-sprint1-users
description: Sprint 1 implementation — CustomUser model, auth forms, views, URLs, and migrations for the users app
metadata:
  type: project
---

Sprint 1 backend tasks completed on 2026-05-27. The `users` app now has a fully functional custom user model with email-based authentication.

**Why:** Project requires email login with no username field, using Django's AbstractUser as the base.

**How to apply:** All other apps that reference the user model must use `settings.AUTH_USER_MODEL`, never import CustomUser directly.

Key decisions made:
- `CustomUser` extends `AbstractUser` (not `AbstractBaseUser`) to retain Django's built-in permissions framework with minimal boilerplate.
- `username = None` removes the username field entirely from AbstractUser.
- `CustomUserManager` uses `**extra_fields` pattern so `create_superuser` passes `first_name`/`last_name` through without needing to enumerate them.
- `AUTH_USER_MODEL = 'users.CustomUser'` added at the bottom of `core/settings.py` after `DEFAULT_AUTO_FIELD`.
- Superuser created non-interactively: `email=admin@assistencia.com`, `password=Admin1234!`.
- flake8 is NOT in requirements.txt — install via `pip install flake8` temporarily to lint.
- The auto-generated `users/tests.py` has an F401 warning (Django scaffold); this is expected and pre-existing.
- Templates at `templates/users/register.html` and `templates/users/login.html` created with Tailwind dark-mode design matching the project design system.

Related: [[project-apps-structure]]
