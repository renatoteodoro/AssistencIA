from django import forms

from accounts.models import Account
from categories.models import Category

from .models import Transaction

_INPUT_CLASSES = (
    'w-full bg-slate-700 border border-slate-600 text-slate-100 '
    'placeholder-slate-400 rounded-lg px-3 py-2 text-sm '
    'focus:outline-none focus:ring-2 focus:ring-indigo-500 '
    'focus:border-transparent transition-all duration-200'
)
_SELECT_CLASSES = (
    'w-full bg-slate-700 border border-slate-600 text-slate-100 '
    'rounded-lg px-3 py-2 text-sm focus:outline-none '
    'focus:ring-2 focus:ring-indigo-500 '
    'focus:border-transparent transition-all duration-200'
)


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'description',
            'amount',
            'transaction_type',
            'date',
            'account',
            'category',
        ]
        widgets = {
            'description': forms.TextInput(attrs={'class': _INPUT_CLASSES}),
            'amount': forms.NumberInput(attrs={'class': _INPUT_CLASSES}),
            'transaction_type': forms.Select(attrs={'class': _SELECT_CLASSES}),
            'date': forms.DateInput(
                attrs={'class': _INPUT_CLASSES, 'type': 'date'},
            ),
            'account': forms.Select(attrs={'class': _SELECT_CLASSES}),
            'category': forms.Select(attrs={'class': _SELECT_CLASSES}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        self.fields['account'].queryset = Account.objects.filter(
            user=self.user,
        )
        self.fields['category'].queryset = Category.objects.filter(
            user=self.user,
        )
