from django.shortcuts import render

# Create your views here.

def index(request):
    #   Returns the calculator page
    return render(request, 'calculator/calculator.html')