from dataclasses import dataclass, field, replace
from typing import Any, List, Optional
import ply.yacc as yacc

from ..comun.modelos import ErrorCompilador
from ..lexico import construir_lexer
from ..lexico.reglas import _columna
from . import gramatica
from .reporte import generar_reporte

# True = generar parser.out
DEBUG = False


@dataclass
class ResultadoSintactico:
    errores: List[ErrorCompilador] = field(default_factory=list)
    errores_lexicos: List[ErrorCompilador] = field(default_factory=list)
    arbol: Optional[Any] = None


def analizar(codigo: str) -> ResultadoSintactico:
    gramatica.errores_sintacticos.clear()
    parser = yacc.yacc(module=gramatica, debug=DEBUG, write_tables=False)
    lexer = construir_lexer()
    arbol = parser.parse(codigo, lexer=lexer)
    errores = []
    for e in gramatica.errores_sintacticos:
        if e.linea == 0:
            e = replace(e, linea=lexer.lineno, columna=_columna(codigo, len(codigo)))
        errores.append(e)
    return ResultadoSintactico(errores, list(lexer.errores), arbol=arbol)


__all__ = ["analizar", "ResultadoSintactico", "generar_reporte"]
