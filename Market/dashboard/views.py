
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from item.models import item



@login_required
def dashb(request):

    
    items = item.objects.filter(created_by=request.user)
        
    return render(request, 'dashboard/dash.html',{'items':items})


