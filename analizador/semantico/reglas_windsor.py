from typing import List

from ..comun.modelos import ErrorCompilador, FASE_SEMANTICA
from .arbol import ExpresionBinaria, NodoAST
from .tipos import (
    TIPO_BOOL,
    TIPO_DESCONOCIDO,
    TIPO_ERROR,
    es_tipo_numerico,
)


def _agregar_error(nodo: NodoAST, mensaje: str, errores: List[ErrorCompilador]) -> None:
    errores.append(
        ErrorCompilador(
            fase=FASE_SEMANTICA,
            linea=nodo.linea,
            columna=nodo.columna,
            mensaje=mensaje,
        )
    )


# Regla semántica 1: Compatibilidad de tipos en expresiones aritméticas
def validar_expresion_aritmetica(
    nodo: ExpresionBinaria,
    tipo_izq: str,
    tipo_der: str,
    errores: List[ErrorCompilador],
) -> str:
    if tipo_izq == TIPO_ERROR or tipo_der == TIPO_ERROR:
        return TIPO_ERROR

    if tipo_izq == TIPO_DESCONOCIDO:
        return tipo_der if es_tipo_numerico(tipo_der) else TIPO_DESCONOCIDO
    if tipo_der == TIPO_DESCONOCIDO:
        return tipo_izq if es_tipo_numerico(tipo_izq) else TIPO_DESCONOCIDO

    # Validar que ambos operandos sean numéricos
    if not es_tipo_numerico(tipo_izq) or not es_tipo_numerico(tipo_der):
        _agregar_error(
            nodo,
            f"No se puede aplicar el operador '{nodo.operador}' entre tipos no numéricos ('{tipo_izq}' y '{tipo_der}')",
            errores,
        )
        return TIPO_ERROR

    if tipo_izq != tipo_der:
        _agregar_error(
            nodo,
            f"Tipos incompatibles en operación aritmética '{nodo.operador}': '{tipo_izq}' y '{tipo_der}' (se requiere conversión explícita)",
            errores,
        )
        return TIPO_ERROR

    return tipo_izq


# Regla semántica 2: Validación de condición booleana en estructuras de control
def validar_condicion_control(
    nodo: NodoAST,
    tipo_condicion: str,
    errores: List[ErrorCompilador],
) -> None:
    if tipo_condicion in (TIPO_ERROR, TIPO_DESCONOCIDO):
        return

    if tipo_condicion != TIPO_BOOL:
        _agregar_error(
            nodo,
            f"La condición en la estructura de control debe ser de tipo '{TIPO_BOOL}', pero se encontró '{tipo_condicion}'",
            errores,
        )
