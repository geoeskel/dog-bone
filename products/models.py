from django.db import models

# Category model (inherit from models.Model)
class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)  # friendly name is optional (null and blank = True)

    def __str__(self):  # string name definition
        return self.name

    def get_friendly_name(self):  # returns friendly name if exists
        return self.friendly_name

# Product model
class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)  #foreign key to the category model, can be null in db and blank in forms, if category is deleted any item in this category will have NULL in the field instead of deleting the item
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):  # string name definition
        return self.name