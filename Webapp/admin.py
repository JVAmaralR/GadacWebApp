from django.contrib import admin
from .models import usermodel, Post, Animal

# Ação personalizada para marcar usuários como staff
def make_staff(modeladmin, request, queryset):
    queryset.update(is_staff=True)
make_staff.short_description = 'Marcar usuários como staff'

# Modelo de usuário
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'cep', 'user_phoneNum', 'user_age', 'pref_adopt', 'is_staff', 'is_superuser',)
    search_fields = ('username', 'email')  # Campos para pesquisa
    ordering = ('username',)  # Ordenar por username
    list_filter = ('is_staff', 'is_superuser', 'pref_adopt')  # Filtros para navegação
    readonly_fields = ('user_id',)  # Deixar o user_id como somente leitura
    actions = [make_staff]  # Ação personalizada para marcar usuários como staff

# Registrando o modelo de usuário
admin.site.register(usermodel, UserModelAdmin)

# Modelo de post
class PostAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'content', 'created_at', 'post_categ')
    search_fields = ('content', 'post_categ')  # Campos para pesquisa
    ordering = ('-created_at',)  # Ordenar por data de criação (mais recente primeiro)
    list_filter = ('post_categ', 'created_at')  # Filtros para navegação
    date_hierarchy = 'created_at'  # Navegação por data
    formfield_overrides = {
        # Tornar o campo content um TextArea no formulário de admin
        'content': {'widget': admin.widgets.AdminTextareaWidget},
    }

# Registrando o modelo Post
admin.site.register(Post, PostAdmin)

# Modelo de animal
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('animal_id', 'animal_name', 'animal_race', 'rescued_at')
    search_fields = ('animal_name', 'animal_race')  # Campos para pesquisa
    ordering = ('animal_name',)  # Ordenar por nome do animal
    list_filter = ('animal_race', 'rescued_at')  # Filtros para navegação
    date_hierarchy = 'rescued_at'  # Navegação por data de resgate

# Registrando o modelo Animal
admin.site.register(Animal, AnimalAdmin)
