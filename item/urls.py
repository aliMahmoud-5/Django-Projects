from django.urls import path, include
from .views import detail, additem, delitem, edititem, browse


app_name = 'item'

urlpatterns = [
    path('<int:pk>/detail', detail, name = 'detail'),
    path('additem/', additem, name = 'add-item'),
    path('<int:pk>/delete', delitem, name = 'del-item'),
    path('<int:pk>/edit', edititem, name = 'edit-item'),
    path('browse/', browse, name = 'browse'),
    path('<int:pk>/', detail, name = 'detail'),
    
    ]
