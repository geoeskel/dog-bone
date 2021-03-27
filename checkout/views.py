from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Product
from basket.contexts import basket_contents

import stripe

# Create your views here.

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Checking if the method is 'POST and getting the 'basket'
    if request.method == 'POST':
        basket = request.session.get('basket', {})
        # Putting 'form_data' into dictionary so we can create its instance 
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        """ 
            1. 	We get the 'product_id' out of the basket.
            2. 	If its value is an integer we know we're working with an item that doesn't have sizes
                so the quantity will be the 'item_data'.
            3. 	If the item has sizes, iterate through each size and create a 'line_item' accordingly.
            4. 	If a product isn't found, add an error message.
            5. 	Delete the empty order and return the user to the shopping basket page.
        """
        if order_form.is_valid():
            # Needed for the order number to be passed as an argument
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
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
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket wasn't found in our database."
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))

            """
            Check if the user wants to save their profile information to the
            session. Then, redirect them to a 'checkout_success' page.
            """
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
    else:
        """
        Getting basket from the session, if nothins in the basket,
        print error message. Afterwards, redirect ot products page
        """
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, "There's nothing in your basket at the moment")
            return redirect(reverse('products'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        # Stripe requires the amount to charge as an int
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        # Payemnt intent
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Create instance of the order form and render it out
        order_form = OrderForm()

    # Alert message if you forgot to set STRIPE_PUBLIC_KEY    
    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is not found')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Successful checkout
    1.  Check if the user wants to save their information
        by getting that from the session
    2.  Use the 'order_number' to create the 'order'
    3.  Send the 'order' to the template
    4.  Display the success message to the user
    5.  Delete user's shopping bag from the session
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. We will send \
        you a confirmation email to {order.email}.')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)