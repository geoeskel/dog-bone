from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

"""
Getting basket from the session, if nothins in the basket, print error message
Afterwards, redirect ot products page
"""


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    # Create instance of the order form and render it out
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
