from django.urls import path

from My_EShop.accounts.views import RegisterUserView, LogInUserView, LogOutUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view, name='register user'),
    path('login/', LogInUserView.as_view, name='login user'),
    path('logout/', LogOutUserView.as_view, name='logout user'),
)
