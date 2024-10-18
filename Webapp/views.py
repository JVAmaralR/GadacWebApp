from django.shortcuts import render
from django.contrib.auth import login
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.http import HttpResponseRedirect
from .models import usermodel, Animal, Post
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

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
    success_url = reverse_lazy('home') #define para onde sera redirecionado caso seja concluido o login
    form_class = UserLoginForm           # define o form que sera usado

    def post(self, request, *args, **kwargs):
        form = self.form_class(request, data=request.POST)

        if form.is_valid():
            # Autentica o usuário
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                if user.is_active:
                    # Faz login
                    login(request, user)
                    return HttpResponseRedirect(self.get_success_url())
                else:
                    # Usuário está inativo
                    form.add_error(None, "Esta conta está inativa.")
            else:
                # Usuário ou senha incorretos
                form.add_error(None, "Email ou senha incorretos.")
        
        # Se o formulário não for válido, renderiza a página de login com os erros
        return render(request, self.template_name, {'form': form})

    def get_success_url(self):          #redireciona da forma correta
        return self.success_url

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Corrigido de 'post_content' para 'content'
        context['post'] = Post.objects.only('post_image', 'content').last()  
        context['pets'] = Animal.objects.only('animal_image', 'animal_name').order_by('-animal_id')[:4]

        return context

def custom_logout_view(request):#cria a view que desloga o user
    logout(request)  # Encerra a sessão do usuário
    return redirect('home')  # Redireciona para a página de login


class AdotePageView(LoginRequiredMixin, TemplateView):
    template_name = 'adote.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['pets'] = Animal.objects.only('animal_id', 'rescued_at', 'animal_name', 'animal_race', 'animal_bio', 'animal_image', 'animal_gene').all()  
        return context

