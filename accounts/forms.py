from django import forms

from .models import Account

_INPUT_CLASSES = (
    'w-full bg-slate-700 border border-slate-600 text-slate-100 '
    'placeholder-slate-400 rounded-lg px-3 py-2 text-sm '
    'focus:outline-none focus:ring-2 focus:ring-indigo-500 '
    'focus:border-transparent transition-all duration-200'
)
_SELECT_CLASSES = (
    'w-full bg-slate-700 border border-slate-600 text-slate-100 '
    'rounded-lg px-3 py-2 text-sm focus:outline-none '
    'focus:ring-2 focus:ring-indigo-500'
)


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'account_type', 'initial_balance']
        widgets = {
            'name': forms.TextInput(attrs={'class': _INPUT_CLASSES}),
            'initial_balance': forms.NumberInput(
                attrs={'class': _INPUT_CLASSES}
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['account_type'].widget = forms.Select(
            attrs={'class': _SELECT_CLASSES},
            choices=Account.ACCOUNT_TYPE_CHOICES,
        )
