from django.contrib import admin
from .models import Product, Category  # imports Products and Category from .models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):  # class extending ModelAdmin class
    list_display = (  # tuple that tells admin which fields to display
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)  # orders by name; to reverse we put a '-' in front of 'name'

class CategoryAdmin(admin.ModelAdmin):  # class extending ModelAdmin class
    list_display = (  # tuple that tells admin which fields to display
        'friendly_name',
        'name',    
    )

admin.site.register(Product, ProductAdmin)  # registering products and product admin
admin.site.register(Category, CategoryAdmin)  # registering category and category admin

