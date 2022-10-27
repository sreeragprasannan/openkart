from django.shortcuts import render
# Create your views here.

def register(request):
    
    form = NewUserForm(request.POST)
    
    context = {
        'form': form,
    }
    
    return render(request, 'users/register.html', context)