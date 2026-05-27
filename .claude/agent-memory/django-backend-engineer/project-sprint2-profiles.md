---
name: project-sprint2-profiles
description: Sprint 2 — Profile model, auto-creation signal, admin registration, migrations applied
metadata:
  type: project
---

Sprint 2 implemented the `profiles` app with automatic profile creation on user registration.

**Profile model** (`profiles/models.py`): OneToOneField to `settings.AUTH_USER_MODEL` with `related_name='profile'`, `on_delete=CASCADE`. Has `created_at`/`updated_at` audit fields. `__str__` returns `str(self.user)`. Meta: `verbose_name='perfil'`, `verbose_name_plural='perfis'`.

**Signal** (`profiles/signals.py`): `post_save` on `get_user_model()` with `dispatch_uid='create_user_profile'`. Creates `Profile` only when `created=True`. Registered via `profiles/apps.py` `ready()` method.

**Admin** (`profiles/admin.py`): `ProfileAdmin` with `list_display`, `search_fields` on `user__email`, `readonly_fields` for audit fields.

**Migration**: `profiles/migrations/0001_initial.py` — applied successfully.

**Flake8 config**: `.flake8` created at project root to exclude `*/migrations/*` and `.venv`. Scaffold stubs (`tests.py`, `views.py`) cleared of unused imports.

**Why:** Signal pattern with `dispatch_uid` prevents duplicate profile creation in test environments. `get_user_model()` used instead of direct import to respect `AUTH_USER_MODEL` indirection.

**How to apply:** When Sprint 3+ views need to access the profile, use `request.user.profile` (guaranteed to exist for any user created after this signal is active). Existing users created before the signal will not have profiles — handle with `get_or_create` if needed.
