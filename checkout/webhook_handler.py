from django.http import HttpResponse

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time


class Stripe_Webhook_Handler:
    # Stripe Webhooks

    # '__init__' is a setup method called each time an instance of a class
    # is created. Used to a assign the request as an attribute of the class
    def __init__(self, request):
        self.request = request

    # Generic, unknown and unexpected wh
    def handle_event(self, event):

        # Takes the event stripe is sending us and returns an HTTP response
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    # Payment_intent.succeeded wh
    def handle_payment_intent_succeeded(self, event):

        # Print out 'PaymentIntent' from stripe
        intent = event.data.object
        print(intent)
        pid = intent.id
        basket = intent.metadata.basket
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        #   To ensure the data is in the same form as what we want in our database,
        #   replace any empty strings in the shipping details with 'None'
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        #   Update profile information if 'save_info' was checked
        #   1. Get the username from 'intent.metadata.username'
        #   2. If the username isn't anonymous user, the user is authenticated
        #   3. If they are authenticated, get 'UserProfile' using 'user__username'
        #   4. Then, update the profile's shipping details  
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_town_or_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.line1
                profile.default_street_address2 = shipping_details.address.line2
                profile.default_county = shipping_details.address.state
                profile.save()

        #   1. Check if the order exists already
        #   2. If yes, return a response and say all is good
        #   3. If not, create it here in the webhook
        order_exists = False
        #   Preventing the order being added to the database twice
        #   if the view is slow or hasn't created the order by the time
        #   we get the webhook from stripe
        attempt = 1
        while attempt <= 5:
            try:
                #   'iexact' = exact match but case insensitive
                #   Makes sure we have the exact order in the webhook handler
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    town_or_city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.line1,
                    street_address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_basket=basket,
                    stripe_pid=pid,
                )

                order_exists = True
                # If the order is found, break out from the loop
                break
            except Order.DoesNotExist:
                #   Preventing the order being added to the database twice
                #   if the view is slow or hasn't created the order by the time
                #   we get the webhook from stripe
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    town_or_city=shipping_details.address.city,
                    street_address1=shipping_details.address.line1,
                    street_address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_basket=basket,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(basket).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)

        # Takes the event stripe is sending us and returns an HTTP response
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created an order in webhook',
            status=200)

    # Payment_intent.payment_failed wh
    def handle_payment_intent_payment_failed(self, event):

        # Takes the event stripe is sending us and returns an HTTP response
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)