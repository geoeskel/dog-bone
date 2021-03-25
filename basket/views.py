from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_basket(request):
    """ View that renders the content of shopping basket page """

    return render(request, 'basket/basket.html')

# We submit the form to the 'add_to_basket' view.
# Once in the view, it picks the 'basket' variable (if exists)
# or create if it doesn't and then adds the item to the basket
# (or adds the quantity if the item already exists)
# and then it overrites the 'basket' variable
# with the updated one from the session


def add_to_basket(request, item_id):
    """ Add product quantity to the shopping basket """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    #  Checking if product has a size in request.POST
    # if yes, overrite the None with the value from request.POST
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # We create 'basket' variable
    # to store the basket content in the browsing session
    basket = request.session.get('basket', {})

    # If the item is in the basket, increment the quantity.
    # If the item is not in the basket, add it as dictionary
    # It allows us adding multiple items with the same id
    # but different sizes (e.g. Dog Food with 1kg and 5kg)
    if size:
        if item_id in list(basket.keys()):
            if size in basket[item_id]['items_by_size'].keys():
                basket[item_id]['items_by_size'][size] += quantity
                messages.success(request, f'Updated {size.upper()}kg {product.name} amount in your basket to {basket[item_id]["items_by_size"][size]}')
            else:
                basket[item_id]['items_by_size'][size] = quantity
                messages.success(request, f'Added {size.upper()}kg {product.name} to your basket')
        else:
            basket[item_id] = {'items_by_size': {size: quantity}}
            messages.success(request, f'Added {size.upper()}kg {product.name} to your basket')
    else:
        if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request, f'Updated {product.name} amount in your basket to {basket[item_id]}')
        else:
            basket[item_id] = quantity
            messages.success(request, f'{product.name} added to your basket')

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)


def update_basket(request, item_id):
    """ Update product quantity in the shopping basket """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    #  Checking if product has a size in request.POST
    # if yes, overrite the None with the value from request.POST
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    # We create 'basket' variable
    # to store the basket content in the browsing session
    basket = request.session.get('basket', {})

    # If the item quantity > 0, set the item quantity accordingly
    # Otherwise, remove the item. If item has a size,
    # we drill down the item dictionary, find the specific size
    # and either set the size to the updated one or delete
    # if submitted quantity is 0
    if size:
        if quantity > 0:
            basket[item_id]['items_by_size'][size] = quantity
            messages.success(request, f'Updated {size.upper()}kg {product.name} amount in your basket to {basket[item_id]["items_by_size"][size]}')

        else:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
                messages.success(request, f'Removed {size.upper()}kg {product.name} from your basket')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated {product.name} amount in your basket to {basket[item_id]}')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))


def delete_from_basket(request, item_id):
    """ Delete product from the shopping basket """

    #  Checking if product has a size in request.POST
    # if yes, overrite the None with the value from request.POST
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        # We create 'basket' variable
        # to store the basket content in the browsing session
        basket = request.session.get('basket', {})

        # If item with size is in the basket, we want to delete
        # this size key from the basket
        # If 'items_by_size' is empty, we want to remove the
        # entire 'item_id' to avoid having empty item dictionaries
        # If item has no size, remove the 'item_id'
        # Afterward, we want to return httpresponse 200
        # (item successfully removed)
        if size:
            del basket[item_id]['items_by_size'][size]
            if not basket[item_id]['items_by_size']:
                basket.pop(item_id)
            messages.success(request, f'Removed {size.upper()}kg {product.name} from your basket')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
