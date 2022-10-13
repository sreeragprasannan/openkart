from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Product
# Create your views here.

def index(request):
    
    li = ["Alllen","Sreerag","alwin","justin","allu"]
    
    context = {'names':li}
    
    return render(request, 'myapp/index.html',context=context)



def new_one(request):
    return render(request, 'listing/new_one.html')

def products(request):
    p = Product.objects.get(name='I Phone')
    
    
    return HttpResponse(p)

def my_place(request):
    
    return render(request, 'myplace/assignment.html')