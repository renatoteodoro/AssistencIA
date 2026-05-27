---
name: project-forms
description: Django form classes and their field structures used in AssistencIA templates
metadata:
  type: project
---

## LoginForm (users/forms.py — extends AuthenticationForm)

Fields:
- `username` — EmailInput, placeholder "seu@email.com", autofocus
- `password` — PasswordInput, placeholder "Senha"

Tailwind classes are applied by the form via `_FIELD_CLASSES` constant — templates just render `{{ form.username }}` and `{{ form.password }}`.

## RegisterForm (users/forms.py — extends UserCreationForm)

Model: `users.CustomUser`

Fields in order:
- `first_name` — TextInput, placeholder "Nome"
- `last_name` — TextInput, placeholder "Sobrenome"
- `email` — EmailInput, placeholder "seu@email.com"
- `password1` — PasswordInput, placeholder "Senha"
- `password2` — PasswordInput, placeholder "Confirme a senha"

All widgets already carry Tailwind classes from `_FIELD_CLASSES`. Templates render each field directly by name.

**How to apply:** When rendering auth forms field-by-field in templates, use these exact field names. No need to add CSS classes to inputs — the form widgets supply them.
