from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Product
from django.db.models import Q
# Create your views here.


def index(request):

    li = ["Alllen", "Sreerag", "alwin", "justin", "allu"]

    context = {'names': li}

    return render(request, 'myapp/index.html', context=context)


def new_one(request):
    return render(request, 'listing/new_one.html')


def products(request):
    p = Product.objects.filter(price__gt = 100000)
    context = {'products': p}

    return render(request, 'myapp/products.html', context=context)


def my_place(request):

    return render(request, 'myplace/assignment.html')
