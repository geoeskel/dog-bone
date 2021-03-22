from django.db import models

# Category model (inherit from models.Model)
class Category(models.Model):

    class Meta:
        # fixing spelling of the plural of category
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    # friendly name is optional (null and blank = True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # string name definition
    def __str__(self):  
        return self.name

    # returns friendly name if exists
    def get_friendly_name(self):  
        return self.friendly_name

# Product model
class Product(models.Model):
    #foreign key to the category model, can be null in db and blank in forms, 
    # if category is deleted any item in this category will have NULL in the field instead of deleting the item
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):  # string name definition
        return self.name