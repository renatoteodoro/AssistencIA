---
name: sprint1-auth-findings
description: Sprint 1 authentication QA findings — known bug in login error message rendering and confirmed design system compliance
metadata:
  type: project
---

AssistencIA Sprint 1 authentication was tested on 2026-05-27 against http://127.0.0.1:8000.

**Known Bug — Login error message has double space:**
URL: http://127.0.0.1:8000/users/login/
The invalid-credentials error message reads: "Por favor, entre com um e-mail  e senha corretos." — note the double space between "e-mail" and "e". This is a Django default form error string, likely from `AuthenticationForm`. Severity: Baixa.

**Error message HTML structure:**
- Login non-field errors render inside: `<div class="mb-5 bg-red-900/50 border border-red-700 rounded-lg p-3"><p class="text-red-300 text-sm">...</p></div>`
- Register field errors render as: `<p class="text-red-400 text-xs mt-1">...</p>`
- Neither uses class names containing "error", "alert", or "danger" — CSS selectors targeting those strings will miss these elements. Must match by `[class*="red"]` or by text content.

**Duplicate email error text:** "Usuário com este E-mail já existe." — standard Django unique constraint message.

**Design system — fully compliant on both /users/login/ and /users/register/:**
- Body: `bg-slate-950 text-slate-100 min-h-screen` — rgb(2,6,23) confirmed
- Card: `bg-slate-800 border border-slate-700 rounded-xl` — all present
- Gradient title: `from-indigo-500` present
- Primary button: `bg-indigo-600` present
- Indigo link: present on both pages

**Test accounts created during this session:**
- Email: qa@teste.com / Password: QaTeste1234! (registered successfully, can log in, lands on /dashboard/)

**Why:** Establishes baseline auth behavior and a known double-space bug for future regression.
**How to apply:** When re-testing login errors, search body text for "Por favor" or "senha corretos" — not generic English error keywords. When selecting error elements programmatically, use `[class*="red"]` not `[class*="error"]`.
