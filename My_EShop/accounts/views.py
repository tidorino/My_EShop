from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from My_EShop.accounts.forms import RegisterUserForm

UserModel = get_user_model()


class RegisterUserView(CreateView):
    template_name = 'accounts/home_no_profile.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, ** kwargs)
        login(request, self.object)
        return response


class LogInUserView(LoginView):
    template_name = 'accounts/login.html'


class LogOutUserView(LogoutView):

    #  Override next_page of  def get_default_redirect_url from LogoutView or
    # I can add in setting.py we add LOGOUT_URL = reverse_lazy('index')
    next_page = reverse_lazy('index')
