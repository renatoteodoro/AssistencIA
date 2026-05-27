from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import CustomUser

_FIELD_CLASSES = (
    'bg-slate-700 border border-slate-600 text-slate-100 placeholder-slate-400 '
    'rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 '
    'focus:ring-indigo-500 focus:border-transparent transition-all duration-200'
)


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': _FIELD_CLASSES,
                'placeholder': 'Nome',
            }),
            'last_name': forms.TextInput(attrs={
                'class': _FIELD_CLASSES,
                'placeholder': 'Sobrenome',
            }),
            'email': forms.EmailInput(attrs={
                'class': _FIELD_CLASSES,
                'placeholder': 'seu@email.com',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget = forms.PasswordInput(attrs={
            'class': _FIELD_CLASSES,
            'placeholder': 'Senha',
        })
        self.fields['password2'].widget = forms.PasswordInput(attrs={
            'class': _FIELD_CLASSES,
            'placeholder': 'Confirme a senha',
        })


class LoginForm(AuthenticationForm):
    error_messages = {
        'invalid_login': 'Por favor, entre com um e-mail e senha corretos.',
        'inactive': 'Esta conta está inativa.',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.EmailInput(attrs={
            'class': _FIELD_CLASSES,
            'placeholder': 'seu@email.com',
            'autofocus': True,
        })
        self.fields['password'].widget = forms.PasswordInput(attrs={
            'class': _FIELD_CLASSES,
            'placeholder': 'Senha',
        })
