from django.contrib import admin
from .models import Product, Category  # imports Products and Category from .models

# Register your models here.
admin.site.register(Product)  # registering products
admin.site.register(Category)  # registering category
