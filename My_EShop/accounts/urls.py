from django.urls import path, include

from My_EShop.accounts.views import RegisterUserView, LogInUserView, LogOutUserView, UserDetailsView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LogInUserView.as_view(), name='login user'),
    path('logout/', LogOutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='user details'),
        # path('edit/', UserEditView.as_view(), name='edit user'),
        # path('delete/', UserDeleteView.as_view(), name='delete user'),
    ])),
)
