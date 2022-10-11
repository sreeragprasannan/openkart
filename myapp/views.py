from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    
    li = ["Alllen","Sreerag","alwin","justin","allu"]
    
    context = {'names':li}
    
    return render(request, 'myapp/index.html',context=context)



def new_one(request):
    return render(request, 'listing/new_one.html')