# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

AssistencIA — sistema web de gestão de finanças pessoais. Django 5.2 full stack com SQLite e TailwindCSS. UI em português brasileiro; código em inglês.

## Common Commands

```bash
# Activate virtualenv (Windows)
.venv\Scripts\activate

# Run dev server
python manage.py runserver

# Create and apply migrations
python manage.py makemigrations <app_name>
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Check code style
flake8 .
```

## Architecture

`core/` is the Django project config directory (settings, root URLs, wsgi/asgi). There is no separate `config/` or `project/` folder — `DJANGO_SETTINGS_MODULE` is `core.settings`.

Six apps, each with a single responsibility:

| App | Role |
|---|---|
| `users` | Custom user model — login by email, no username |
| `profiles` | One-to-one profile created automatically via signal on user save |
| `accounts` | Bank accounts owned by the logged-in user |
| `categories` | Transaction categories (income / expense) owned by the user |
| `transactions` | Financial entries (income / expense) linked to account + category |
| `core` | Public landing page, authenticated dashboard, root URL config |

Each app will have its own `urls.py` included in `core/urls.py` under a matching prefix: `users/` (auth routes), `accounts/`, `categories/`, `transactions/`.

## Key Conventions

**User isolation** — every authenticated queryset must filter by `user=request.user`. Views that fetch a single object must return 404 if it doesn't belong to the requesting user. This is enforced via `get_queryset()` in CBVs.

**Class-Based Views** — use CBVs with `LoginRequiredMixin` for all authenticated views.

**Audit fields** — every model must include:
```python
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
```

**Signals** — live in `<app>/signals.py` and are registered in `<app>/apps.py` via `ready()`.

**Forms** — use `ModelForm`; filter relational querysets by the logged-in user inside `__init__`.

**Code style** — PEP8, single quotes, English identifiers. Run `flake8` before committing.

**AUTH_USER_MODEL** — will be `users.CustomUser` (not yet implemented). All FK references to the user model must use `settings.AUTH_USER_MODEL`, not `User` directly.

**Deletion guard** — `Account` and `Category` can only be deleted if they have no linked transactions. Check before deleting and show an informative message when blocked.

**No Docker, no automated tests** — both are out of scope for the current sprints and must not be added until the backlog sprints (8 and 9).

## Design System

Dark-mode first (Tailwind `dark` class). Core tokens:

- Background: `bg-slate-950`
- Surface/card: `bg-slate-800 border border-slate-700 rounded-xl`
- Primary action: `bg-indigo-600 hover:bg-indigo-700`
- Success / income: `text-emerald-400` / `bg-emerald-900`
- Danger / expense: `text-red-400` / `bg-red-900`
- Hero gradient: `bg-gradient-to-br from-indigo-500 via-purple-600 to-cyan-500`

Full component reference in [`docs/design-system.md`](docs/design-system.md).
