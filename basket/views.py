from django.shortcuts import render, redirect

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

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    # We create 'basket' variable
    # to store the basket content in the browsing session
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)
