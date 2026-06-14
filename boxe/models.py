from django.db import models
from django.utils import timezone
import secrets


def generate_api_key():
    return secrets.token_urlsafe(32)


class Lutador(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50)
    peso = models.FloatField(help_text="Peso em kg")
    categoria = models.CharField(max_length=50)
    vitorias = models.IntegerField(default=0)
    derrotas = models.IntegerField(default=0)
    empates = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Combate(models.Model):
    lutador1 = models.ForeignKey(Lutador, on_delete=models.CASCADE, related_name='combates_como_lutador1')
    lutador2 = models.ForeignKey(Lutador, on_delete=models.CASCADE, related_name='combates_como_lutador2')
    data = models.DateField()
    rounds = models.IntegerField()
    vencedor = models.ForeignKey(Lutador, on_delete=models.SET_NULL, null=True, blank=True, related_name='vitorias_combates')
    metodo = models.CharField(max_length=50, help_text="KO, TKO, Decisão, Empate")

    def __str__(self):
        return f"{self.lutador1} vs {self.lutador2}"


class Titulo(models.Model):
    nome = models.CharField(max_length=100)
    organizacao = models.CharField(max_length=20, help_text="WBC, WBA, IBF, WBO")
    categoria = models.CharField(max_length=50)
    campeao = models.ForeignKey(Lutador, on_delete=models.SET_NULL, null=True, blank=True, related_name='titulos')

    def __str__(self):
        return f"{self.organizacao} {self.nome}"


class APIKey(models.Model):
    name = models.CharField(max_length=100, help_text="Nome de quem vai usar a chave")
    key = models.CharField(max_length=255, unique=True, default=generate_api_key)
    is_active = models.BooleanField(default=True)
    expiration_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {'Ativa' if self.is_active else 'Inativa'}"

    def is_valid(self):
        return self.is_active and self.expiration_date > timezone.now()
