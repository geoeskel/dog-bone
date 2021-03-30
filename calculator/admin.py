from django.contrib import admin
# imports Breed from .models
from .models import Breeds

# Register your models here.

# registering breed and category breed admin
admin.site.register(Breeds)
