from ninja import Schema
from typing import Optional
from datetime import date


class LutadorIn(Schema):
    nome: str
    nacionalidade: str
    peso: float
    categoria: str
    vitorias: int = 0
    derrotas: int = 0
    empates: int = 0
    ativo: bool = True


class LutadorOut(LutadorIn):
    id: int


class CombateIn(Schema):
    lutador1_id: int
    lutador2_id: int
    data: date
    rounds: int
    vencedor_id: Optional[int] = None
    metodo: str


class CombateOut(Schema):
    id: int
    lutador1: LutadorOut
    lutador2: LutadorOut
    data: date
    rounds: int
    vencedor: Optional[LutadorOut] = None
    metodo: str


class TituloIn(Schema):
    nome: str
    organizacao: str
    categoria: str
    campeao_id: Optional[int] = None


class TituloOut(Schema):
    id: int
    nome: str
    organizacao: str
    categoria: str
    campeao: Optional[LutadorOut] = None


class ErrorSchema(Schema):
    detail: str
