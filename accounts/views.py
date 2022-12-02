from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import *


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'
    context_object_name = 'login'
    success_url = reverse_lazy('store:home')

    def get_success_url(self):
        return reverse_lazy('store:home')


@login_required
def home(request):
    return render(request, 'accounts/home.html')


def logout_user(request):
    logout(request)
    return redirect('store:home')


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/pages-sign-up.html'
    context_object_name = 'register'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('store:home')