from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class NodoAST:
    linea: int = 0
    columna: int = 0


@dataclass
class Programa(NodoAST):
    sentencias: List[NodoAST] = field(default_factory=list)


@dataclass
class DeclaracionVariable(NodoAST):
    nombre: str = ""
    tipo_declarado: Optional[str] = None
    es_mutable: bool = False
    valor_inicial: Optional[NodoAST] = None


@dataclass
class Asignacion(NodoAST):
    objetivo: str = ""
    operador: str = "="
    valor: Optional[NodoAST] = None


@dataclass
class ExpresionBinaria(NodoAST):
    operador: str = ""
    izquierda: Optional[NodoAST] = None
    derecha: Optional[NodoAST] = None


@dataclass
class ExpresionUnaria(NodoAST):
    operador: str = ""
    expresion: Optional[NodoAST] = None


@dataclass
class Literal(NodoAST):
    tipo_literal: str = ""
    valor: Any = None


@dataclass
class Identificador(NodoAST):
    nombre: str = ""


@dataclass
class Bloque(NodoAST):
    sentencias: List[NodoAST] = field(default_factory=list)


@dataclass
class CondicionalIf(NodoAST):
    condicion: Optional[NodoAST] = None
    bloque_si: Optional[Bloque] = None
    bloque_sino: Optional[NodoAST] = None


@dataclass
class BucleWhile(NodoAST):
    condicion: Optional[NodoAST] = None
    bloque: Optional[Bloque] = None


@dataclass
class DefinicionFuncion(NodoAST):
    nombre: str = ""
    parametros: List[Tuple[str, str]] = field(default_factory=list)
    tipo_retorno: Optional[str] = None
    bloque: Optional[Bloque] = None


@dataclass
class LlamadaFuncion(NodoAST):
    nombre: str = ""
    argumentos: List[NodoAST] = field(default_factory=list)


@dataclass
class DefinicionStruct(NodoAST):
    nombre: str = ""
    campos: Dict[str, str] = field(default_factory=dict)


@dataclass
class InstanciacionStruct(NodoAST):
    nombre: str = ""
    valores_campos: Dict[str, NodoAST] = field(default_factory=dict)


@dataclass
class AccesoCampo(NodoAST):
    objeto: str = ""
    campo: str = ""
