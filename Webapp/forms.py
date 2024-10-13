from django import forms
from .models import usermodel
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(forms.ModelForm): #Criação do form de registro
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')
    
    class Meta:   #Classe que define os atributos do forms que seram setado no model
        model = get_user_model()
        fields = ['username', 'email', 'user_phoneNum', 'user_age', 'pref_adopt',  'cep']  
        widgets = {'pref_adopt':forms.TextInput(attrs={'size':40, 'maxlength':200})}
        
    def clean(self): #Função que verifa se os dados estão inseridos corretos e maneira limpa                                                  
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:           # condicional que verifica se as senhas digitas coincidem 
            raise forms.ValidationError("As senhas não coincidem")

        return cleaned_data  #retona os dados limpos

    def save(self, commit=True): #salva os dados
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])  
        if commit:
            user.save()  # Salva o usuário no banco de dados
        return user

class UserLoginForm(AuthenticationForm):     #criação do forms de login
    username = forms.EmailField(label="Email")
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'maxlength':60})
    
    def clean(self):   #verifica se os dados foram inseridos da forma correta e de forma limpa                    
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if email and password:
            try:
                user = usermodel.objects.get(email=email)
                self.cleaned_data.update({'username':user.username})
            except:
                raise forms.ValidationError("Usuario com este email não foi encontrado.")
        if not user.check_password(password):
            raise forms.ValidationError("Senha incorreta.")
    
        return self.cleaned_data #retonas o dado limpo e correto