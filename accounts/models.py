import uuid
from django.db import models
from django.utils import timezone
from datetime import timedelta


class MagicToken(models.Model):
    email = models.EmailField()
    token = models.UUIDField(default=uuid.uuid4, unique=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    usado = models.BooleanField(default=False)

    def is_valido(self):
        """Token válido por 15 minutos."""
        return not self.usado and timezone.now() < self.criado_em + timedelta(minutes=15)

    def __str__(self):
        return f"Token para {self.email}"
