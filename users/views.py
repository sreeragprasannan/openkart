from django.shortcuts import render,redirect
from users.forms import NewUserForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#login forms
def register(request):
    
    form = NewUserForm(request.POST)
    if request.method=='POST':
        print(f'form valid : {form.is_valid()}')
        if form.is_valid():
            form.save()
        return redirect('/myapp/products')
    
    context = {
        'form': form,
    }
     
    return render(request, 'users/register.html', context=context)

def profile(request):
    
    # context=('user')
    
    return render(request, 'users/profile.html')

def create_profile(request):
    
    if request.method=='POST':
        pass
    
    return render(request,'user/createprofile')
    
    