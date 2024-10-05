from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings

import os

# Create your models here.

class UserManager(BaseUserManager):
        def manager_user(self, username, password, email, **extra_fields):
            if not username:
                raise ValueError('The Username field must be set')
            user = self.model(username=username, email=email)
            user.set_password(password)
            user.save(using=self._db)
            return user
        
        def manage_superuser(self, username, password, email, **extra_fields):
             extra_fields.setdefault('is_staff', True)
             extra_fields.setdefault('is_superuser', True)
             if extra_fields.get('is_staff') is not True:
                  raise ValueError('Superuser must have is_staff = true.')
             if extra_fields.get('is_superuser') is not True:
                  raise ValueError('Superuser must have is_superuser=True.')
             return self.create_user(username, password, **extra_fields)

class Endereco(models.Model):
    rua = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    

    def __str__(self):
        return f"{self.rua}, {self.cidade} - {self.estado}, {self.cep}"

class usermodel(AbstractBaseUser):
     username= models.CharField(max_length=30, unique=True, null= False)
     user_email= models.EmailField(unique=True, null= False)
     user_id = models.AutoField(primary_key= True)
     is_staff = models.BooleanField(default=False)
     is_superuser = models.BooleanField(default=False)
     user_phoneNum = models.CharField(max_length=50)
     user_age = models.IntegerField(null= False)
     endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, null=True, blank=True)
     pref_adopt = models.TextField()

     objects = UserManager()

     USERNAME_FIELD = 'username'
     REQUIRED_FIELDS = ['email']
     def __str__(self):
          return self.username


class Post(models.Model):
    post_id = models.AutoField(primary_key= True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post_categ = models.CharField(max_length=20)

    def __str__(self):
        return self.content[:20]

class Animal(models.Model):
    animal_id = models.AutoField(primary_key= True)
    rescued_at = models.DateTimeField(auto_now_add = False)
    animal_name = models.CharField(max_length=30)
    animal_race = models.CharField(max_length= 100)
    animal_bio = models.TextField()
    def __str__(self):
        return self.name
    