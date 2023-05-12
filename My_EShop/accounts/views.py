from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from My_EShop.accounts.forms import RegisterUserForm
from My_EShop.eshop.models import Category

UserModel = get_user_model()


class RegisterUserView(CreateView):
    template_name = 'accounts/create_profile.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, ** kwargs)
        login(request, self.object)
        return response


class LogInUserView(LoginView):
    template_name = 'accounts/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories

        return context



class LogOutUserView(LogoutView):

    #  Override next_page of  def get_default_redirect_url from LogoutView or
    # I can add in setting.py we add LOGOUT_URL = reverse_lazy('index')
    next_page = reverse_lazy('index')


class UserDetailsView(DetailView):
    pass