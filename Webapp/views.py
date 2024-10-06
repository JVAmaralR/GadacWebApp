from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import CreateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login
from .models import usermodel
from .forms import UserRegisterForm

class UserRegisterView(CreateView):
    model = usermodel
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login') 

    def form_valid(self, form):
        user = form.save()  
        login(self.request, user)  
        return redirect(self.success_url)  
