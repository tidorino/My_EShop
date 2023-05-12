from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic as generic_views


from My_EShop.eshop.models import Category, Product

UserModel = get_user_model()


def index(request):
    categories = Category.objects.all()
    products = Product.products.all()

    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'index.html', context)


def show_categories(request):
    return render(request, 'categories.html', {'categories': Category.objects.all()})


class CategoryListView(generic_views.ListView):
    model = Category
    template_name = "eshop_admin/list-category.html"


class DetailsCategory(generic_views.DetailView):
    model = Category
    template_name = 'eshop_admin/details-category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


def category_list(request, slug):
    category = get_object_or_404(Category, category_slug=slug)
    try:
        product = Product.objects.filter(category=category)
    except Product.DoesNotExist:
        product = None

    context = {
        'category': category,
        'product': product,
        # 'categories': Category.objects.all(),
    }
    return render(request, 'eshop_admin/category-list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, product_slug=slug, in_stock=True)

    context = {
        'product': product,
        'categories': Category.objects.all(),
    }
    return render(request, 'eshop_admin/product_detail.html', context)


class ProductsByCategoryView(generic_views.ListView):
    ordering = 'id'
    paginate_by = 10
    template_name = 'eshop_admin/products_by_category.html'


    def get_queryset(self):
        # https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic-display/#dynamic-filtering
        # the following category will also be added to the context data

        self.category = Category.objects.get(category_slug=self.kwargs['category_slug'])
        queryset = Product.objects.filter(category=self.category)

         # need to set ordering to get consistent pagination results
        queryset = queryset.order_by(self.ordering)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class AddCategory(generic_views.CreateView):
    model = Category
    # template_name =



class EditCategory(generic_views.UpdateView):
    model = Category


class DeleteCategory(generic_views.DeleteView):
    model = Category





