from dataclasses import dataclass, field
from typing import List
import ply.yacc as yacc

from ..comun.modelos import ErrorCompilador
from ..lexico import construir_lexer
from . import gramatica
from .reporte import generar_reporte

# True = generar parser.out
DEBUG = False


@dataclass
class ResultadoSintactico:
    errores: List[ErrorCompilador] = field(default_factory=list)
    errores_lexicos: List[ErrorCompilador] = field(default_factory=list)


def analizar(codigo: str) -> ResultadoSintactico:
    gramatica.errores_sintacticos.clear()
    parser = yacc.yacc(module=gramatica, debug=DEBUG, write_tables=False)
    lexer = construir_lexer()
    parser.parse(codigo, lexer=lexer)
    return ResultadoSintactico(list(gramatica.errores_sintacticos), list(lexer.errores))


__all__ = ["analizar", "ResultadoSintactico", "generar_reporte"]
