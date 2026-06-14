from ninja import NinjaAPI
from ninja.security import APIKeyHeader
from typing import List
from django.shortcuts import get_object_or_404
from .models import Lutador, Combate, Titulo, APIKey
from .schemas import (LutadorIn, LutadorOut, CombateIn, CombateOut,
                      TituloIn, TituloOut, ErrorSchema)


class AuthAPIKey(APIKeyHeader):
    param_name = "X-API-Key"

    def authenticate(self, request, key):
        try:
            api_key = APIKey.objects.get(key=key)
            if api_key.is_valid():
                return api_key.name
        except APIKey.DoesNotExist:
            pass
        return None


api = NinjaAPI(
    title="API RESTful de Boxe",
    description="API para gerir lutadores, combates e títulos de boxe.",
    version="1.0.0",
    auth=AuthAPIKey()
)


@api.get("lutadores/", response={200: List[LutadorOut]}, tags=["Lutadores"])
def list_lutadores(request, nome: str = None, categoria: str = None, limit: int = 10, offset: int = 0):
    lutadores = Lutador.objects.all()
    if nome:
        lutadores = lutadores.filter(nome__icontains=nome)
    if categoria:
        lutadores = lutadores.filter(categoria__icontains=categoria)
    return 200, lutadores[offset:offset+limit]


@api.get("lutadores/{lutador_id}/", response={200: LutadorOut, 404: ErrorSchema}, tags=["Lutadores"])
def get_lutador(request, lutador_id: int):
    return 200, get_object_or_404(Lutador, id=lutador_id)


@api.post("lutadores/", response={201: LutadorOut}, tags=["Lutadores"])
def post_lutador(request, data: LutadorIn):
    return 201, Lutador.objects.create(**data.dict())


@api.put("lutadores/{lutador_id}/", response={200: LutadorOut, 404: ErrorSchema}, tags=["Lutadores"])
def put_lutador(request, lutador_id: int, data: LutadorIn):
    lutador = get_object_or_404(Lutador, id=lutador_id)
    for attr, value in data.dict().items():
        setattr(lutador, attr, value)
    lutador.save()
    return 200, lutador


@api.delete("lutadores/{lutador_id}/", response={204: None, 404: ErrorSchema}, tags=["Lutadores"])
def delete_lutador(request, lutador_id: int):
    get_object_or_404(Lutador, id=lutador_id).delete()
    return 204, None


@api.get("combates/", response={200: List[CombateOut]}, tags=["Combates"])
def list_combates(request, metodo: str = None, limit: int = 10, offset: int = 0):
    combates = Combate.objects.select_related('lutador1', 'lutador2', 'vencedor').all()
    if metodo:
        combates = combates.filter(metodo__icontains=metodo)
    return 200, combates[offset:offset+limit]


@api.get("combates/{combate_id}/", response={200: CombateOut, 404: ErrorSchema}, tags=["Combates"])
def get_combate(request, combate_id: int):
    return 200, get_object_or_404(
        Combate.objects.select_related('lutador1', 'lutador2', 'vencedor'), id=combate_id)


@api.post("combates/", response={201: CombateOut}, tags=["Combates"])
def post_combate(request, data: CombateIn):
    combate = Combate.objects.create(**data.dict())
    return 201, get_object_or_404(
        Combate.objects.select_related('lutador1', 'lutador2', 'vencedor'), id=combate.id)


@api.put("combates/{combate_id}/", response={200: CombateOut, 404: ErrorSchema}, tags=["Combates"])
def put_combate(request, combate_id: int, data: CombateIn):
    combate = get_object_or_404(Combate, id=combate_id)
    for attr, value in data.dict().items():
        setattr(combate, attr, value)
    combate.save()
    return 200, get_object_or_404(
        Combate.objects.select_related('lutador1', 'lutador2', 'vencedor'), id=combate_id)


@api.delete("combates/{combate_id}/", response={204: None, 404: ErrorSchema}, tags=["Combates"])
def delete_combate(request, combate_id: int):
    get_object_or_404(Combate, id=combate_id).delete()
    return 204, None


@api.get("titulos/", response={200: List[TituloOut]}, tags=["Títulos"])
def list_titulos(request, organizacao: str = None, limit: int = 10, offset: int = 0):
    titulos = Titulo.objects.select_related('campeao').all()
    if organizacao:
        titulos = titulos.filter(organizacao__icontains=organizacao)
    return 200, titulos[offset:offset+limit]


@api.get("titulos/{titulo_id}/", response={200: TituloOut, 404: ErrorSchema}, tags=["Títulos"])
def get_titulo(request, titulo_id: int):
    return 200, get_object_or_404(Titulo.objects.select_related('campeao'), id=titulo_id)


@api.post("titulos/", response={201: TituloOut}, tags=["Títulos"])
def post_titulo(request, data: TituloIn):
    titulo = Titulo.objects.create(**data.dict())
    return 201, get_object_or_404(Titulo.objects.select_related('campeao'), id=titulo.id)


@api.put("titulos/{titulo_id}/", response={200: TituloOut, 404: ErrorSchema}, tags=["Títulos"])
def put_titulo(request, titulo_id: int, data: TituloIn):
    titulo = get_object_or_404(Titulo, id=titulo_id)
    for attr, value in data.dict().items():
        setattr(titulo, attr, value)
    titulo.save()
    return 200, get_object_or_404(Titulo.objects.select_related('campeao'), id=titulo_id)


@api.delete("titulos/{titulo_id}/", response={204: None, 404: ErrorSchema}, tags=["Títulos"])
def delete_titulo(request, titulo_id: int):
    get_object_or_404(Titulo, id=titulo_id).delete()
    return 204, None