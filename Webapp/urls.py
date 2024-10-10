from django.urls import path
from .views import UserRegisterView
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.navbar)
]

urlpatterns = [
    path("", views.sobrenos)
]
