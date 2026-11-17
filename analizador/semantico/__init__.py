from dataclasses import dataclass, field
from typing import List, Optional

from ..comun.modelos import ErrorCompilador
from .arbol import NodoAST
from .reporte import generar_reporte
from .verificador import VerificadorSemantico


@dataclass
class ResultadoSemantico:
    errores: List[ErrorCompilador] = field(default_factory=list)
    errores_sintacticos: List[ErrorCompilador] = field(default_factory=list)
    errores_lexicos: List[ErrorCompilador] = field(default_factory=list)


def analizar(codigo: str, ast: Optional[NodoAST] = None) -> ResultadoSemantico:
    from ..sintactico import analizar as analizar_sintactico

    resultado_sintactico = analizar_sintactico(codigo)

    if ast is None:
        ast = resultado_sintactico.arbol

    errores_semanticos: List[ErrorCompilador] = []
    if ast is not None and not resultado_sintactico.errores:
        verificador = VerificadorSemantico()
        errores_semanticos = verificador.verificar(ast)

    return ResultadoSemantico(
        errores=errores_semanticos,
        errores_sintacticos=resultado_sintactico.errores,
        errores_lexicos=resultado_sintactico.errores_lexicos,
    )


__all__ = ["analizar", "ResultadoSemantico", "generar_reporte"]
