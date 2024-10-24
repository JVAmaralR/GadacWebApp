from django import forms
from .models import usermodel
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm

from django import forms
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': ''}), 
        label='Senha'
    )
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Repita sua senha'}), 
        label='Confirmar Senha'
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'user_phoneNum', 'user_age', 'pref_adopt', 'cep']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Seu Nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'seuemail@email.com'}),
            'user_phoneNum': forms.TextInput(attrs={'placeholder': 'Ex: (11) 99999-9999'}),
            'user_age': forms.NumberInput(attrs={'placeholder': 'Sua Idade'}),
            'pref_adopt': forms.Textarea(attrs={'placeholder': 'Descreva suas preferências...', 'size':40, 'maxlength':200}),
            'cep': forms.TextInput(attrs={'placeholder': 'Ex: 12345-678'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
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
    

