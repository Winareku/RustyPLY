"""Fase léxica: texto -> tokens.

Uso:
    from analizador.lexico import analizar
    resultado = analizar(codigo)      # resultado.tokens, resultado.errores
Para el sintáctico: `tokens` (lista de nombres) y `construir_lexer()`.
"""
from dataclasses import dataclass, field
from typing import List

from ..comun.modelos import Token, ErrorCompilador
from .tokens import tokens
from .reglas import construir_lexer, _columna
from .reporte import generar_reporte


@dataclass
class ResultadoLexico:
    tokens: List[Token] = field(default_factory=list)
    errores: List[ErrorCompilador] = field(default_factory=list)


def analizar(codigo: str) -> ResultadoLexico:
    lexer = construir_lexer()
    lexer.input(codigo)
    encontrados = []
    for tok in lexer:  # PLY permite iterar el lexer
        encontrados.append(Token(tok.type, tok.value, tok.lineno, _columna(codigo, tok.lexpos)))
    return ResultadoLexico(encontrados, lexer.errores)


__all__ = ["analizar", "ResultadoLexico", "tokens", "construir_lexer", "generar_reporte"]
