from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,TemplateView,DetailView,CreateView,DeleteView,UpdateView

# Create your views here.

def index(request):

    li = ["Alllen", "Sreerag", "alwin", "justin", "allu"]

    context = {'names': li}

    return render(request, 'myapp/index.html', context=context)


def new_one(request):
    return render(request, 'listing/new_one.html')

class ProductListView(ListView):
    model = Product
    context_object_name = 'myapp/products.html'
    template_name='products'

@login_required
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

        p = Product(name=name,price=price,description=desc,image=image)
        p.seller_name = request.user
        p.save()
        
        return redirect('/myapp/products')

    return render(request, 'myapp/addproducts.html')

def update_products(request,id):
    p = Product.objects.get(id=id)
    context = {'p': p}
    
    if request.method == 'POST':
        p.name = request.POST.get('name')
        p.price = request.POST.get('price')
        p.description = request.POST.get('desc')
        try:
            p.image = request.FILES['upload']
        except:
            pass
        
        p.save()
        return redirect('/myapp/products')
        
    return render(request, 'myapp/update_product.html', context=context)

def delete_products(request,id):
    p = Product.objects.get(id=id)
    context = {'p': p}
    
    if request.method == 'POST':
        p.delete()
        
        return redirect('/myapp/products')

    return render(request, 'myapp/delete_product.html', context=context)

def my_place(request):

    return render(request, 'myplace/assignment.html')
