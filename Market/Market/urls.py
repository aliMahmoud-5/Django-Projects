
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('login/',auth_views.LoginView.as_view(template_name= 'core/login.html'),name = 'login'),
    path('item/', include('item.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
