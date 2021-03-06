from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
from math import ceil

# Create your views here.

def index(request):
    # products = Products.objects.all()
    # print(products)

    #params = {'product' : products, 'no_of_slides': nSlides, 'range':range(1,nSlides)}
    # print(params['range'])

    # allProds = [ [products, range(1,nSlides), nSlides], 
    #              [products, range(1,nSlides), nSlides] ]

    allProds = []

    catprods = Products.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prod = Products.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1,nSlides), nSlides])

    params = {'allProds' : allProds}
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
