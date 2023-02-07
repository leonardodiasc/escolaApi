from django.contrib import admin
from escola.models import Aluno, Curso
# Register your models here.
class Alunos(admin.ModelAdmin):
    list_display = ('nome', 'rg', 'cpf', 'data_nascimento')
    list_display_links = ('nome',)
    search_fields = ['nome']
    list_per_page = 20

admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('codigo_curso', 'descricao')
    list_display_links = ('codigo_curso',)
    search_fields = ['codigo_curso']

admin.site.register(Curso, Cursos)