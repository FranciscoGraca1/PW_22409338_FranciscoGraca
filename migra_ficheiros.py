import os
from django.core.files import File
from portfolio.models import Tecnologia, Projeto

for obj in Tecnologia.objects.all():
    if obj.logo and obj.logo.name:
        local_path = os.path.join('media', obj.logo.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.logo.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado Tecnologia: {obj}")

for obj in Projeto.objects.all():
    if obj.imagem and obj.imagem.name:
        local_path = os.path.join('media', obj.imagem.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.imagem.save(os.path.basename(local_path), File(f), save=True)
            print(f"Migrado Projeto: {obj}")