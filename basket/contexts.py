from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    # Empty list for the basket items with a total and product count
    basket_items = []
    total = 0
    product_count = 0
    delivery = 0
    # Accessing the session's shopping basket
    basket = request.session.get('basket', {})

    for item_id, item_data in basket.items():
        # Checking if item_data has size
        # (if it is an integer it will be a quantity only)
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.price
            product_count += item_data
            # List of bag items dictionary containing item id,
            # amount of items and the product object (product image, etc.)
            basket_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            # If it has size, we need to iterate through the dictionary
            # incrementing item total accordingly
            # and adding the item to the basket
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                basket_items.append({
                    'item_id': item_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
