from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.


# Allows us to add and edit line items from inside the order
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    # Adding 'OrderLineItemAdminInline' option to 'OrderAdmin' interface
    inlines = (OrderLineItemAdminInline,)

    # Set as read only so they cannot be maniputaled to compromise the order
    readonly_fields = ('order_number', 'date', 'grand_total','original_basket', 'stripe_pid')

    fields = ('order_number', 'user_profile', 'date', 'full_name', 'email', 'phone_number', 'country', 'postcode', 'town_or_city', 'street_address1', 'street_address2', 'county', 'delivery_cost', 'grand_total', 'original_basket', 'stripe_pid')

    list_display = ('order_number', 'date', 'full_name', 'grand_total',)

    # '-date' filters the orders chronologically, newest orderst first
    ordering = ('-date',)

# Registering 'Order' and 'OrderAdmin'
admin.site.register(Order, OrderAdmin)