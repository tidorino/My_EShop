from django.urls import path, include

from My_EShop.eshop.views import index, category_products,\
    AddCategory, DetailsCategory, EditCategory, DeleteCategory

urlpatterns = (
    path('', index, name='index'),

    path('add/', AddCategory.as_view(), name='add category'),
    path('category/<int:pk>/', include([
        path('<slug:slug>', category_products, name='category products'),
        path('', DetailsCategory.as_view(), name='details category'),
        path('edit/', EditCategory.as_view(), name='edit category'),
        path('delete/', DeleteCategory.as_view(), name='delete category'),
    ])),

)
