from django.contrib import admin

from django import forms
from django.forms import CheckboxSelectMultiple
from mptt.admin import DraggableMPTTAdmin
from mptt.fields import TreeManyToManyField

from My_EShop.eshop.models import Category, Product, Brand


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['title']

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    # specify pixel amount(levels of tree) for this ModelAdmin only:
    mptt_level_indent = 20
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Product,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(
            qs,
            Product,
            'category',
            'products_count',
            cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['name', 'category']
    formfield_overrides = {
        TreeManyToManyField: {'widget': CheckboxSelectMultiple},
    }


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title']