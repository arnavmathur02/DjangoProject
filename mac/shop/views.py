from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse("We are at the About Page")

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
