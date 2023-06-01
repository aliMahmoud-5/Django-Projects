
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import item, category
from .forms import add, edit
from django.db.models import Q


def detail(request, pk):
    
    context = {
        'item': get_object_or_404(item,pk=pk),
        #'related_items': item.objects.filter(categ = item.categ, sold = False).exclude(pk=pk)[0:6]
        }
    return render(request,'item/detail.html',context)


@login_required
def additem(request):
    if request.method == 'POST':
        form = add(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
          
            return redirect('item:detail', pk=item.id)
    form = add()
    return render(request, 'item/additem.html', {'form':form})


@login_required
def delitem(request, pk):
    context = {
        'item': get_object_or_404(item,pk=pk, created_by=request.user)
        }
    context['item'].delete()
    return render(request,'dashboard/dash.html')


@login_required
def edititem(request, pk):

    Item = get_object_or_404(item,pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = edit(request.POST, request.FILES,instance= Item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=Item.id)
    form = edit(instance= Item)
    return render(request, 'item/edititem.html', {'form':form})


def browse(request):
    category_id = request.GET.get('category',0)
    context = {
    'items': item.objects.filter(sold=False),
    'query': request.GET.get('query',''),
    'category_id':request.GET.get('category',0),
    'category': category.objects.all,
        }
    if category_id:
        category_id = context['items'].filter(categ_id=category_id)
    if context['query']:
        context['items'] = context['items'].filter(Q(name__icontains=context['query']) | Q(description__icontains=context['query']))
    category_id = int(category_id)
    context['category_id']=category_id 
    return render(request,'item/browse.html',context)