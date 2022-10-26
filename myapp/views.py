from django.shortcuts import render,redirect
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

    p = Product.objects.all()
    context = {'products': p}

    return render(request, 'myapp/products.html', context=context)


def products_detail(request, id):
    p = Product.objects.get(id=id)
    context = {'p': p}
    return render(request, 'myapp/product_details.html', context=context)

# to add poducts using html form
def add_products(request,):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        desc = request.POST.get('desc')
        image = request.FILES['upload']

        p = Product(name=name, price=price, description=desc, image=image)
        p.save()
        
        return redirect('/myapp/products')

    return render(request, 'myapp/addproducts.html')

def update_products(request,id):
    p = Product.objects.get(id=id)
    context = {'p': p}
    if request.method == 'POST':
        p.name = request.POST.get('name')
        p.price = request.POST.get('price')
        p.desc = request.POST.get('desc')
        p.image = request.FILES['upload']
        
        return redirect('/myapp/products')
        p.save()

    return render(request, 'myapp/update_product.html', context=context)

def my_place(request):

    return render(request, 'myplace/assignment.html')
