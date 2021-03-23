from django.shortcuts import render

# Create your views here.

def view_basket(request):
    """ View that renders the content of shopping basket page """
    
    return render(request, 'basket/basket.html')

