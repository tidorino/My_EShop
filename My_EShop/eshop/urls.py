from django.urls import path, include

from My_EShop.eshop import views
from My_EShop.eshop.views import \
    DetailsCategory, EditCategory, DeleteCategory, ProductsByCategoryView, CategoryListView

# from My_EShop.eshop.views import index, category_list, \
#     AddCategory, DetailsCategory, EditCategory, DeleteCategory, show_categories, product_detail

urlpatterns = (
    path('', views.index, name='index'),
    path('categories/', views.show_categories),
    path('c/', CategoryListView.as_view(), name='list-category'),

    path('add/', views.AddCategory.as_view(), name='add category'),
    path('category/<slug:slug>', views.category_list, name='category list'),
    path('item/<slug:slug>', views.product_detail, name='product detail'),
    path('<str:category_slug>/', ProductsByCategoryView.as_view(), name='category-detail'),
    path('category/<int:pk>/', include([
        # path('<slug:slug>', category_list, name='category products'),
        path('', DetailsCategory.as_view(), name='details category'),
        path('edit/', EditCategory.as_view(), name='edit category'),
        path('delete/', DeleteCategory.as_view(), name='delete category'),
    ])),

)
