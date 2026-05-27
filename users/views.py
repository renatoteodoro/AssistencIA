from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import LoginForm, RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    authentication_form = LoginForm
    template_name = 'auth/login.html'


__all__ = ['RegisterView', 'CustomLoginView', 'LogoutView']
