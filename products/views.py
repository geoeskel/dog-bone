from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm

# Create your views here.

def all_products(request):
    """ A view to show all products, including sorting and search queries """

    # setting the query, categories, sort and direction to 'None' makes sure
    # we don't get an error when loading the page without a search term
    # and the template is shown properly when not using any sorting
    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None


    if request.GET:
        # We check if 'sort' is in request.GET, then we set sort to 'none' 
        # and to 'sortkey' (to apply lowercase to it for search and to preserve the original parameter),
        # then we rename sprtkey to 'lower_name' if the user is sorting by name and annotate the list of products
        # with a new name and check if the direction is descending to decide whether to reverse the order with '-'
        # then we sort the products using '.order_by' model method
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                # '__' allows us to drill into the related model so it changes the products from line 40 to: products.order_by('category__name')
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            # filtering the products to check if they are in specific categoty list
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            # using Q function; we are checking if the name OR description 
            # equals the searched phrase. 'i' in front of 'contains' makes it case insensitive 
            # and then we are passing the queries to the filter method in order to filter the products
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        # we are returning the current sorting methodology to the template by using string formatting
    current_sorting = f'{sort}_{direction}'

    context = {
        # adding query to the context and returning the categories so we can use it in the template
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    #   A view to show individual product details

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
    

def add_product(request):
    #   Add a product to the store
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product added successfully')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Incorrect form?')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

def edit_product(request, product_id):
    #   Edit a product
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Invalid form?')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)

def delete_product(request, product_id):
    #   Delete a product
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted')
    return redirect(reverse('products'))