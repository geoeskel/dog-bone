from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None  # setting the query to None makes sure we don't get an error when loading the page without a search term
    categories = None # same as above

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)  # filtering the products to check if they are in specific categoty list
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Enter search criteria")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)  # using Q function; we are checking if the name OR description equals the searched phrase. 'i' in front of 'contains' makes it case insensitive 
            products = products.filter(queries)  # passing the queries to the filter method to filter the products


    context = {
        'products': products,
        'search_term': query,  # adding query to the context
        'current_categories': categories,  # returns the categories so we can use it in the template
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)