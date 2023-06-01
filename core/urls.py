from pipes import Template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import loginform
from dashboard.views import dashb


urlpatterns = [
    path('', views.home, name = 'home'),
    path('signup/', views.signup, name = 'signup'),
    #path('login/',auth_views.LoginView.as_view(template_name= 'core/login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name= 'core/home.html'),name='logout'),
    path('dash/', dashb, name='dash'),
    ]
