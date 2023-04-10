from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('My_EShop.eshop.urls')),
    path('accounts/', include('My_EShop.accounts.urls')),
]
