from django.contrib import admin
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
from authentic import views as authentic_view
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('login/', auth_view.LoginView.as_view(template_name='authentic/login.html') , name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='authentic/logout.html') , name='logout'),
    path('register/',authentic_view.register, name='register'),
    path('profile/',authentic_view.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
