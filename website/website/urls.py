"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from . import views


# urlpatterns = [
#     path('',views.home , name='home'),
#     path("upload/",views.upload, name='upload'),
#     path("generate_summary/",views.generate_summary, name='generate_summary'),
#     path("settings/",views.settings, name='settings'),
#     path('help/',views.help, name='help'),
#     path('login/',views.login, name='name'),
    
#     path('admin/', admin.site.urls),
    
    
    
# ]
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    
    path('', views.home, name='home'),  # Redirects to the homepage.
    path('upload/', views.upload_view, name='upload'),
    path('help/', views.help_view, name='help'),
    path('generate_summary/', views.generate_summary_view, name='generate_summary'),
    path('settings/', views.settings_view, name='settings'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
   # path('accounts/', include('accounts.urls')),  # Accounts app URLs
    #path('summary/', include('apps.summary.urls')), 
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

