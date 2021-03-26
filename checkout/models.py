from django.db import models

# Create your models here.


# When user checks out we will use info they put on payment form to create
# an 'Order' instance. Then, we iterate through the items in the shopping basket
# and create 'OrderLineItem' for each individual item and attach it to order
# and update the 'grand_total'
class Order(models.Model):
    # Requered character fields. Set postcode and county null and false to True
    # as they are not present in every geographical location
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)        
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)


class OrderLineItem(models.Model):
    # Individual shopping basket item relating to a specific order
    # referencing the product and its details
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
