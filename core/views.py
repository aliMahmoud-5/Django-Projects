
from django.shortcuts import render, redirect
from item.models import item, category
from .forms import register


def home(request):

    context = {
        'items': item.objects.filter(sold=False)[0:6],
        'category': category.objects.all,
        }
    return render(request,'core/home.html',context)


def signup(request):
    if request.method == 'POST':
        form = register(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form = register()

    return render(request, 'core/signup.html', {'form':form})

    

