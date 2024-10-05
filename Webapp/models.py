from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
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

class usermodel(AbstractBaseUser):
     username= models.CharField(max_length=30, unique=True)
     email= models.EmailField(unique=True)
     user_id = models.AutoField(primary_key= True)
     is_staff = models.BooleanField(default=False)
     is_superuser = models.BooleanField(default=False)

     objects = UserManager()

     USERNAME_FIELD = 'username'
     REQUIRED_FIELDS = ['email']
     def __str__(self):
          return self.username


class Post(models.Model):
    post_id = models.AutoField(primary_key= True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]