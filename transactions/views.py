from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from accounts.models import Account
from categories.models import Category

from .forms import TransactionForm
from .models import Transaction


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/transaction_list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        qs = Transaction.objects.filter(user=self.request.user)

        month = self.request.GET.get('month')
        year = self.request.GET.get('year')
        account_pk = self.request.GET.get('account')
        category_pk = self.request.GET.get('category')

        if month and year:
            try:
                qs = qs.filter(date__month=int(month), date__year=int(year))
            except (ValueError, TypeError):
                pass

        if account_pk:
            try:
                qs = qs.filter(account__pk=int(account_pk))
            except (ValueError, TypeError):
                pass

        if category_pk:
            try:
                qs = qs.filter(category__pk=int(category_pk))
            except (ValueError, TypeError):
                pass

        return qs.order_by('-date', '-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = Account.objects.filter(user=self.request.user)
        context['categories'] = Category.objects.filter(user=self.request.user)
        context['filter_month'] = self.request.GET.get('month', '')
        context['filter_year'] = self.request.GET.get('year', '')
        context['filter_account'] = self.request.GET.get('account', '')
        context['filter_category'] = self.request.GET.get('category', '')
        return context


class TransactionCreateView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:transaction_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionUpdateView(LoginRequiredMixin, UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'transactions/transaction_form.html'
    success_url = reverse_lazy('transactions:transaction_list')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TransactionDeleteView(LoginRequiredMixin, DeleteView):
    model = Transaction
    template_name = 'transactions/transaction_confirm_delete.html'
    success_url = reverse_lazy('transactions:transaction_list')

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
