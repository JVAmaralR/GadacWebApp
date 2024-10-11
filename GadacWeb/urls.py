"""
URL configuration for TesteReunião project.

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
from django.contrib import admin
from django.urls import path, include
from Webapp.views import UserRegisterView, UserLoginView, HomePageView, custom_logout_view
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from . import urls
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('register/', UserRegisterView.as_view(), name='register'), #View para registrar o usuario
    path('login/', UserLoginView.as_view(), name='login'),          #View para fazer o login do usuario
    path('logout/', custom_logout_view, name='logout'),             #View de logout não tem um html proprio
    path('home/', HomePageView.as_view(), name='home'),             #View do index(pagina home)
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)







