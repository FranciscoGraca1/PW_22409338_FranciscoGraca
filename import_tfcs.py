import os
import sys
import json
import django

# 1. Configuração de caminhos e ambiente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# 2. Inicializar o Django
django.setup()

# 3. Importar o modelo (SÓ depois do django.setup)
from portfolio.models import TFC

def import_tfcs():
    # Caminho para o teu JSON na pasta data
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'tfcs.json')
    
    if not os.path.exists(json_path):
        print(f"Erro: Ficheiro {json_path} não encontrado!")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            for item in data:
                tfc, created = TFC.objects.get_or_create(
                    titulo=item.get('titulo'),
                    defaults={
                        'autor': item.get('autor', 'Desconhecido'),
                        'ano': item.get('ano', 2026),
                        'resumo': item.get('resumo', ''),
                    }
                )
                status = "Importado" if created else "Já existia"
                print(f"{status}: {tfc.titulo}")
        except Exception as e:
            print(f"Erro ao processar JSON: {e}")

if __name__ == '__main__':
    import_tfcs()