from django.contrib import admin
from .models import Licenciatura, Docente, UnidadeCurricular, Tecnologia, Projeto, TFC


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano', 'uc')
    search_fields = ('titulo', 'descricao')

@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'acronimo', 'preferencia')

admin.site.register(TFC)