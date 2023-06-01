from turtle import update
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import user_register, updateinfo, updatepic
from django.contrib.auth.forms import UserCreationForm
from.models import profile as prof
from Blog.models import posts
# Create your views here.

def register(request):

    if request.method == 'POST':
        form = user_register(request.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Acount created for {username}')
           return redirect('blog-home')

    else:
        form = user_register()

    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = updateinfo(request.POST, instance=request.user)
        u_pic = updatepic(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
        else:
            u_form = updateinfo

        if u_pic.is_valid():
            u_pic.save()
        else:
            u_pic = updatepic

    else:
        u_form = updateinfo(instance=request.user)
        u_pic = updatepic(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'u_pic': u_pic,
        'posts': posts.objects.all(),
        
    }
    return render(request,'users/profile.html', context)
