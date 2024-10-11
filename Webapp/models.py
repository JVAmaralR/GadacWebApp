from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings

import os

# Create your models here.

class UserManager(BaseUserManager):    #Criação do usermanager
        def create_user(self, username, password, email, **extra_fields):     #função de criação de usuario padrão
            if not username:
                raise ValueError('The Username field must be set')
            user = self.model(username=username, email=email, **extra_fields) #define os campos q serão inseridos
            user.set_password(password)       #seta  a senha do user
            user.save(using=self._db)        # salva os dados do user
            return user
        
        def create_superuser(self, username, password=None, email=None, **extra_fields): #função pra criaçãod e um suepr user(adm)
            extra_fields.setdefault('is_staff', True)          #define os atributos de um adm como true
            extra_fields.setdefault('is_superuser', True)

            # Verifica se os campos obrigatórios foram definidos
            if extra_fields.get('is_staff') is not True:
                raise ValueError('Superuser must have is_staff=True.')
            if extra_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must have is_superuser=True.')
            
            return self.create_user(username, password, email, **extra_fields) #retorna e salva os dados do user
        


class usermodel(AbstractBaseUser):      #Classe q define o user model
    username = models.CharField(max_length=30, unique=True, null=False) 
    email = models.EmailField(unique=True, null=False)
    user_id = models.AutoField(primary_key=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    user_phoneNum = models.CharField(max_length=50, null=True)
    user_age = models.IntegerField(null=True)
    cep = models.IntegerField(null=True)
    pref_adopt = models.TextField(null=True)

    objects = UserManager()     # chama a clase q define o user como adm ou não

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email'] 




class Post(models.Model): # criação do model de post
    post_id = models.AutoField(primary_key= True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post_categ = models.CharField(max_length=20)
    post_author = models.ForeignKey('usermodel', on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='posts/', blank=True, null=True)
    def __str__(self):
        return self.content[:20]

class Animal(models.Model): # definição do model pros pets
    animal_id = models.AutoField(primary_key= True)
    rescued_at = models.DateTimeField(auto_now_add = False)
    animal_name = models.CharField(max_length=30)
    animal_race = models.CharField(max_length= 100)
    animal_bio = models.TextField()
    animal_image = models.ImageField(upload_to='animals/', blank=True, null=True)  # Adicionando campo de imagem
    def __str__(self):
        return self.name
    