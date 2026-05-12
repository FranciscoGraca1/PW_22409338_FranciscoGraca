import os
import sys
import django
import json

# Configura o ambiente do Django
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from portfolio.models import Licenciatura, UnidadeCurricular

def run():
    # 1. Garante que a Licenciatura existe
    lic, _ = Licenciatura.objects.get_or_create(
        sigla='LEI',
        defaults={
            'nome': 'Licenciatura em Engenharia Informática',
            'instituicao': 'Universidade Lusófona',
            'ano_inicio': 2022,
            'descricao': 'Curso oficial da Lusófona.',
            'link': 'https://www.ulusofona.pt'
        }
    )

    # 2. Caminho para o JSON (Verifica se a pasta data/files existe com o json lá)
    json_path = os.path.join('data', 'files', 'ULHT260-PT.json')
    
    if not os.path.exists(json_path):
        print(f"Erro: Ficheiro {json_path} não encontrado!")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        dados = json.load(f)

    # 3. Importar cada UC
    for uc_data in dados.get('courseFlatPlan', []):
        sigla = uc_data.get('curricularIUnitReadableCode')
        
        # --- CORREÇÃO DO ERRO DO SEMESTRE ---
        raw_semestre = uc_data.get('semester', 1)
        try:
            # Tenta converter para número (ex: "1" vira 1)
            semestre = int(raw_semestre)
        except (ValueError, TypeError):
            # Se for texto (ex: "Semestral"), define como 1 por padrão
            semestre = 1
        # ------------------------------------

        UnidadeCurricular.objects.update_or_create(
            sigla=sigla,
            licenciatura=lic,
            defaults={
                'nome': uc_data.get('curricularUnitName'),
                'ano': uc_data.get('studyYear', 1),
                'semestre': semestre, # Usa o valor tratado
                'ects': uc_data.get('ects', 6),
                'descricao': ''
            }
        )
        print(f"✓ UC {sigla} importada com sucesso")

if __name__ == '__main__':
    run()