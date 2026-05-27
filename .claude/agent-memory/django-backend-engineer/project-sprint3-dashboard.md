---
name: project-sprint3-dashboard
description: Sprint 3 task 3.3 — DashboardView added to core/views.py with try/except ImportError guards for Account and Transaction models not yet created
metadata:
  type: project
---

DashboardView (LoginRequiredMixin + TemplateView) lives in `core/views.py` and is routed at `dashboard/` in `core/urls.py`.

Context computed in `get_context_data`: `total_balance`, `monthly_income`, `monthly_expense`, `recent_transactions`.

**Why:** Account (Sprint 4) and Transaction (Sprint 5) models don't exist yet. `try/except ImportError` blocks allow the dashboard to render safely with zero/empty defaults until those apps are implemented.

**How to apply:** When Account and Transaction models are added, the ImportError guards remain harmless — they will simply never trigger. Do not remove them until both models are confirmed stable.

See also [[project-sprint1-users]], [[project-sprint2-profiles]].
