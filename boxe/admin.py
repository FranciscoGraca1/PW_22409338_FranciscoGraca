from django.contrib import admin
from .models import Lutador, Combate, Titulo, APIKey

@admin.register(Lutador)
class LutadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade', 'categoria', 'vitorias', 'derrotas', 'empates', 'ativo')
    list_filter = ('categoria', 'ativo', 'nacionalidade')
    search_fields = ('nome',)

@admin.register(Combate)
class CombateAdmin(admin.ModelAdmin):
    list_display = ('lutador1', 'lutador2', 'data', 'vencedor', 'metodo', 'rounds')
    list_filter = ('metodo',)

@admin.register(Titulo)
class TituloAdmin(admin.ModelAdmin):
    list_display = ('nome', 'organizacao', 'categoria', 'campeao')
    list_filter = ('organizacao', 'categoria')

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('name', 'key', 'is_active', 'expiration_date', 'created_at')
    list_filter = ('is_active',)
    readonly_fields = ('key', 'created_at')
