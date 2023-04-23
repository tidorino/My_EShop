from django.contrib import admin

from My_EShop.eshop.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']
