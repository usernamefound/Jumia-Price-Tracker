from django.shortcuts import render, reverse

from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.views.generic import CreateView
from links.models import CustomUser
from .forms import SignupForm


class Login(LoginView):
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    template_name = 'accounts/login.html'


class Signup(CreateView):
    template_name = 'accounts/signup.html'
    model = CustomUser
    form_class = SignupForm

    def get_success_url(self):
        messages.success(self.request, 'Account created successfully! You can now login to your account.')
        return reverse('links:tracker')