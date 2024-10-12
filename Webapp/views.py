from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from .models import usermodel, Animal, Post
from .forms import UserRegisterForm, UserLoginForm

class UserRegisterView(CreateView): # criação da view de registro
    model = usermodel               # define o model usado na view
    form_class = UserRegisterForm   # define o form usado nessa view
    template_name = 'register.html' # define o arquivo html usado
    success_url = reverse_lazy('login')  # se for correto redirecioina para o login

    def form_valid(self, form):          #salva o form de forma correta
        user = form.save()  
        login(self.request, user)  
        return redirect(self.success_url)  #redireciona da forma correta

class UserLoginView(auth_views.LoginView): #criação da view de login
    template_name = "login.html"        # define o arquivo html usado
    success_url = reverse_lazy('index') #define para onde sera redirecionado caso seja concluido o login
    form_class = UserLoginForm           # define o form que sera usado

    def get_success_url(self):          #redireciona da forma correta
        return self.success_url

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Busca até 2 posts e 4 pets, incluindo mais campos se necessário
        context['posts'] = Post.objects.only('post_image')[:2]
        context['pets'] = Animal.objects.only('animal_image', 'animal_name')[:4]  # Adicione 'animal_name' se precisar

        return context

def custom_logout_view(request):#cria a view que desloga o user
    logout(request)  # Encerra a sessão do usuário
    return redirect('home')  # Redireciona para a página de login
