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
from django.urls import path
from Webapp.views import UserRegisterView, UserLoginView, HomePageView, custom_logout_view, AdotePageView
from Webapp.forms import NewResetPasswordForm
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', HomePageView.as_view(), name='home'),                  #View do index(pagina home)
    path('register/', UserRegisterView.as_view(), name='register'), #View para registrar o usuario
    path('login/', UserLoginView.as_view(), name='login'),          #View para fazer o login do usuario
    path('logout/', custom_logout_view, name='logout'),             #View de logout não tem um html proprio
    path('adote/', AdotePageView.as_view(), name='adote'),
    
    #Rotas para redefinição de senha
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset_email_form.html', email_template_name='password_reset/email.html'), name='password_reset'), #Rota onde pede o email
    
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset/password_reset_email_enviado.html'), name='password_reset_done'), #Rota que confirma o envio do email
    
    path('password_reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset/password_reset_senha_nova_form.html', form_class=NewResetPasswordForm), name='password_reset_confirm'), #Rota para a tela de redefinir senha
    
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_senha_trocada.html'), name='password_reset_complete'), #Rota para a confirmação de senha trocada
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

