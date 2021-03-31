# 'uuid' generates the order number
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile

# Create your models here.

"""
When user checks out we will use info they put on payment form to create
an 'Order' instance. Then, we iterate through the items in the shopping
basket and create 'OrderLineItem' for each individual item, attach it
to order and update the 'grand_total'"""

class Order(models.Model):
    """
    Requered character fields. Set postcode and county null and false to True
    as they are not present in every geographical location
    """
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    # Prevents finding duplicate order if the customer ordered the same thing
    # on multiple occasions
    original_basket = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    """
    Generate a random order number using 'uuid'
    '_' before 'generate_order_number' indicates that
    it is a private method that will only be used inside
    this class
    """
    def _generate_order_number(self):
        return uuid.uuid4().hex.upper()
    """
    Update 'grand total' each time a 'lineitem' is added
    Delivery cost is always 0 as we offer free delivery
    so we don't have to account for that
    """
    def update_total(self):
        self.grand_total = self.lineitems.aggregate(Sum('lineitem_total'))['lineitem_total__sum']
        self.save()

    """
    If the order does not have an order number, we call the
    '_generate_order_number' to create one and updates
    the original save
    """
    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    # Individual shopping basket item relating to a specific order
    # referencing the product and its details
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    product_size = models.CharField(max_length=2, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    """
    Sets the 'lineitem' total and and updates
    the original save
    """
    def save(self, *args, **kwargs):
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'
