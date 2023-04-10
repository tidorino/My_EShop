from django.urls import path

from My_EShop.eshop.views import index

urlpatterns = (
    path('', index, name='index'),
)