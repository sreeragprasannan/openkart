from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,TemplateView,DetailView,CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy

# Create your views here.

def index(request):

    li = ["Alllen", "Sreerag", "alwin", "justin", "allu"]

    context = {'names': li}

    return render(request, 'myapp/index.html', context=context)


def new_one(request):
    return render(request, 'listing/new_one.html')


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'myapp/products.html'


def products(request):

    p = Product.objects.all()
    context = {'products': p}

    return render(request, 'myapp/products.html', context=context)

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'p'
    template_name = 'myapp/product_details.html'
    

def products_detail(request, id):
    p = Product.objects.get(id=id)
    context = {'p': p}
    return render(request, 'myapp/product_details.html', context=context)


class ProductCreateView(CreateView):
    model = Product
    fields = ['name','price','description','image','seller_name']
    template_name = 'myapp/addproducts.html'
    success_url = reverse_lazy('myapp:products')

# to add poducts using html form
@login_required
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


class ProductsUpdateView(UpdateView):
    model = Product
    context_object_name = 'p'
    template_name = 'myapp/update_product.html'
    fields = ['name','price','description','image','seller_name']
    success_url = reverse_lazy('myapp:products')
    
  
@login_required
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


class ProductDeleteView(DeleteView):
    model = Product
    context_object_name = 'p'
    template_name = 'myapp/delete_product.html'
    success_url = reverse_lazy('myapp:products')

@login_required
def delete_products(request,id):
    p = Product.objects.get(id=id)
    context = {'p': p}
    
    if request.method == 'POST':
        p.delete()
        
        return redirect('/myapp/products')

    return render(request, 'myapp/delete_product.html', context=context)

def my_place(request):

    return render(request, 'myplace/assignment.html')
