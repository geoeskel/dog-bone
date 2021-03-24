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

    for item_id, quantity in basket.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        # List of bag items dictionary containing item id,
        # amount of items and the product object (product image, etc.)
        basket_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
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
