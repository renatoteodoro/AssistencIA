from decimal import Decimal

from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'public/home.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        now = timezone.now()

        try:
            from accounts.models import Account
            total_balance = (
                Account.objects.filter(user=user)
                .values_list('initial_balance', flat=True)
            )
            total_balance = sum(total_balance, Decimal('0'))
        except ImportError:
            total_balance = Decimal('0')

        try:
            from transactions.models import Transaction
            base_qs = Transaction.objects.filter(
                user=user,
                date__year=now.year,
                date__month=now.month,
            )
            monthly_income = sum(
                base_qs.filter(transaction_type='income')
                .values_list('amount', flat=True),
                Decimal('0'),
            )
            monthly_expense = sum(
                base_qs.filter(transaction_type='expense')
                .values_list('amount', flat=True),
                Decimal('0'),
            )
            recent_transactions = (
                Transaction.objects.filter(user=user)
                .order_by('-date')[:5]
            )
        except ImportError:
            monthly_income = Decimal('0')
            monthly_expense = Decimal('0')
            recent_transactions = []

        context['total_balance'] = total_balance
        context['monthly_income'] = monthly_income
        context['monthly_expense'] = monthly_expense
        context['recent_transactions'] = recent_transactions
        return context
