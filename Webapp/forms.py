from django import forms
from .models import usermodel
from django.contrib.auth.hashers import make_password

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')
    


    class Meta:
        model = usermodel
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

