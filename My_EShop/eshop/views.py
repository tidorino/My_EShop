from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic as generic_views


from My_EShop.eshop.models import Category, Product

UserModel = get_user_model()


def index(request):
    categories = Category.objects.all()

    context = {
        'categories': categories,
    }
    return render(request, 'index.html', context)


class DetailsCategory(generic_views.DetailView):
    model = Category
    template_name = 'eshop_admin/details-category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


def category_products(request, pk, slug):
    products = Product.objects.filter(category_id=pk)
    categories = Category.objects.all()

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'eshop_admin/category-products.html', context)


class AddCategory(generic_views.CreateView):
    model = Category
    # template_name =


class EditCategory(generic_views.UpdateView):
    model = Category


class DeleteCategory(generic_views.DeleteView):
    model = Category





