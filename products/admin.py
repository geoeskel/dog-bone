from django.contrib import admin
# imports Products and Category from .models
from .models import Product, Category

# Register your models here.


# class extending ModelAdmin class
class ProductAdmin(admin.ModelAdmin):
    # tuple that tells admin which fields to display
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )
    # orders by name; to reverse we put a '-' in front of 'name'
    ordering = ('name',)


# class extending ModelAdmin class
class CategoryAdmin(admin.ModelAdmin):
    list_display = (  # tuple that tells admin which fields to display
        'friendly_name',
        'name',
    )


# registering products and product admin
admin.site.register(Product, ProductAdmin)
# registering category and category admin
admin.site.register(Category, CategoryAdmin)
