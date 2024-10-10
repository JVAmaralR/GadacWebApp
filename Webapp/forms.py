from django import forms
from .models import usermodel
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'user_phoneNum', 'user_age', 'pref_adopt',  'cep']  
        widgets = {'pref_adopt':forms.TextInput(attrs={'size':40, 'maxlength':200})}
        
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
            user.save()  # Salva o usuário no banco de dados
        return user

class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    
    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        
        if email and password:
            try:
                user = usermodel.objects.get(email=email)
            except:
                raise forms.ValidationError("Usuario com este email não foi encontrado.")
        if not user.check_password(password):
            raise forms.ValidationError("Senha incorreta.")
    
        return self.cleaned_data