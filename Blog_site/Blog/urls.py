from venv import create
from django.urls import path
from . import views
from .views import postlist, postdetail, createpost, updatepost, deletepost

urlpatterns = [
    path('',postlist.as_view(), name='blog-home'),
    path('post/<int:pk>/',postdetail.as_view(),name = 'post-detail'),
    path('post/new/',createpost.as_view(),name = 'post-create'),
    path('post/<int:id>/update/',updatepost.as_view(),name = 'post-update'),
    path('post/<int:id>/delete/',deletepost.as_view(),name = 'post-delete'),
]
