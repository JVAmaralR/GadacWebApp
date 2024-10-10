from django.contrib import admin
from .models import usermodel, Post, Animal

# Modelo de usuário
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'cep', 'user_phoneNum', 'user_age', 'pref_adopt', 'is_staff', 'is_superuser',)
    search_fields = ('username', 'email')  # Campos para pesquisa
    ordering = ('username',)  # Ordenar por username

# Registrando o modelo de usuário
admin.site.register(usermodel, UserModelAdmin)

# Registrando o modelo Post
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'content', 'created_at', 'post_categ')
    search_fields = ('content', 'post_categ')  # Campos para pesquisa
    ordering = ('-created_at',)  # Ordenar por data de criação (mais recente primeiro)

admin.site.register(Post, PostAdmin)

# Registrando o modelo Animal
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('animal_id', 'animal_name', 'animal_race', 'rescued_at')
    search_fields = ('animal_name', 'animal_race')  # Campos para pesquisa
    ordering = ('animal_name',)  # Ordenar por nome do animal

admin.site.register(Animal, AnimalAdmin)
