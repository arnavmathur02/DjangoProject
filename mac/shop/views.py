from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from math import ceil

# Create your views here.

def index(request):
    products = Products.objects.all()
    print(products)
    n = len(products)

    nSlides = n//4 + ceil((n/4) - (n//4))

    params = {'product' : products, 'no_of_slides': nSlides, 'range':range(1,nSlides)}
    # print(params['range'])
    return render(request,'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at the contact Page")

def tracker(request):
    return HttpResponse("We are at the tracker Page")

def search(request):
    return HttpResponse("We are at the search Page")


def productView(request):
    return HttpResponse("We are at the Products Views Page")

def checkout(request):
    return HttpResponse("We are at the checkout Page")
