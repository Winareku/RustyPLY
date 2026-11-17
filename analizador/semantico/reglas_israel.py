# ===================================================================
# Israel Romero — reglas semánticas: 2 reglas para Asignación de tipo
# ===================================================================

from typing import List, Optional

from ..comun.modelos import ErrorCompilador, FASE_SEMANTICA
from .arbol import (
    Asignacion,
    DeclaracionVariable,
    ExpresionBinaria,
    ExpresionUnaria,
    Identificador,
    InstanciacionStruct,
    Literal,
    LlamadaFuncion,
    NodoAST,
)
from .tabla_simbolos import Simbolo, TablaSimbolos
from .tipos import TIPO_DESCONOCIDO, TIPO_ERROR, TIPO_F64, TIPO_I32, son_tipos_compatibles

ENTEROS = {"i8", "i16", "i32", "i64", "i128", "isize",
           "u8", "u16", "u32", "u64", "u128", "usize"}
FLOTANTES = {"f32", "f64"}

_OPS_ARITMETICOS = {"+", "-", "*", "/", "%"}
_OPS_BOOLEANOS = {"==", "!=", "<", ">", "<=", ">=", "&&", "||"}


# ------------------------------------------------------------
# Utilidades
# ------------------------------------------------------------

def _error(errores: List[ErrorCompilador], nodo: NodoAST, mensaje: str) -> None:
    errores.append(ErrorCompilador(FASE_SEMANTICA, nodo.linea, nodo.columna, mensaje))


def _clase_numerica(tipo: str) -> Optional[str]:
    """'entero' / 'flotante' si el tipo es el que Rust asigna por defecto a un
    literal sin sufijo (i32 / f64); en ese caso el tipo aún puede "ajustarse"."""
    if tipo == TIPO_I32:
        return "entero"
    if tipo == TIPO_F64:
        return "flotante"
    return None


def _numerico_libre(nodo: Optional[NodoAST], tabla: TablaSimbolos) -> Optional[str]:
    """Devuelve 'entero' o 'flotante' si el valor es un número cuyo tipo concreto
    todavía no está fijado (literal sin sufijo, variable inferida de uno, o una
    operación entre ellos). En Rust, `let x: u64 = 5;` es válido porque el 5 se
    ajusta a u64; en cambio `let x: f64 = 5;` no lo es."""
    if isinstance(nodo, Literal):
        return _clase_numerica(nodo.tipo_literal)
    if isinstance(nodo, Identificador):
        simbolo = tabla.buscar(nodo.nombre)
        if simbolo is not None and getattr(simbolo, "tipo_inferido", False):
            return _clase_numerica(simbolo.tipo_dato)
        return None
    if isinstance(nodo, ExpresionUnaria) and nodo.operador == "-":
        return _numerico_libre(nodo.expresion, tabla)
    if isinstance(nodo, ExpresionBinaria) and nodo.operador in _OPS_ARITMETICOS:
        izq = _numerico_libre(nodo.izquierda, tabla)
        der = _numerico_libre(nodo.derecha, tabla)
        return izq if izq is not None and izq == der else None
    return None


def _tipo_confiable(nodo: Optional[NodoAST]) -> bool:
    """False si el tipo que calculó el verificador para este nodo no es fiable
    (por ejemplo &x o *x, que el visitante trata como el tipo interno)."""
    if nodo is None:
        return False
    if isinstance(nodo, (Literal, Identificador, LlamadaFuncion, InstanciacionStruct)):
        return True
    if isinstance(nodo, ExpresionUnaria):
        return nodo.operador in ("-", "!") and _tipo_confiable(nodo.expresion)
    if isinstance(nodo, ExpresionBinaria):
        if nodo.operador in _OPS_BOOLEANOS:
            return True  # el resultado siempre es bool
        return _tipo_confiable(nodo.izquierda) and _tipo_confiable(nodo.derecha)
    return False


def _compatible_referencias(esperado: str, recibido: str) -> bool:
    e_mut = esperado.startswith("&mut ")
    r_mut = recibido.startswith("&mut ")
    if e_mut and not r_mut:
        return False  # &T no sirve donde se espera &mut T
    e = esperado[5:] if e_mut else esperado[1:]
    r = recibido[5:] if r_mut else recibido[1:]
    return e == r or (e == "str" and r == "String")  # &String se acepta como &str


def _compatible(esperado: str, recibido: str,
                clase_valor: Optional[str] = None,
                clase_esperado: Optional[str] = None) -> bool:
    """True si un valor de tipo `recibido` puede guardarse en un `esperado`.
    clase_valor / clase_esperado: 'entero' o 'flotante' cuando ese lado es un
    número sin tipo concreto fijado (ver _numerico_libre)."""
    if TIPO_ERROR in (esperado, recibido):
        return True  # otra categoría ya reportó el problema
    if son_tipos_compatibles(esperado, recibido):
        return True
    if clase_valor == "entero" and esperado in ENTEROS:
        return True
    if clase_valor == "flotante" and esperado in FLOTANTES:
        return True
    if clase_esperado == "entero" and recibido in ENTEROS:
        return True
    if clase_esperado == "flotante" and recibido in FLOTANTES:
        return True
    if esperado.startswith("&") and recibido.startswith("&"):
        return _compatible_referencias(esperado, recibido)
    return False


# ------------------------------------------------------------
# Declaración de variables
# ------------------------------------------------------------

def registrar_variable(nodo: DeclaracionVariable, tabla: TablaSimbolos,
                       tipo_valor: str, errores: List[ErrorCompilador]) -> None:
    tiene_valor = nodo.valor_inicial is not None
    clase_valor = _numerico_libre(nodo.valor_inicial, tabla) if tiene_valor else None
    confiable = _tipo_confiable(nodo.valor_inicial)

    if tiene_valor and nodo.tipo_declarado is not None and confiable:
        if not _compatible(nodo.tipo_declarado, tipo_valor, clase_valor):
            _error(errores, nodo,
                   f"Se esperaba {nodo.tipo_declarado} pero se encontró {tipo_valor}.")

    if nodo.tipo_declarado is not None:
        tipo_variable, inferido = nodo.tipo_declarado, False
    elif not confiable or tipo_valor == TIPO_ERROR:
        tipo_variable, inferido = TIPO_DESCONOCIDO, False
    else:
        tipo_variable, inferido = tipo_valor, clase_valor is not None

    simbolo = Simbolo(
        nombre=nodo.nombre,
        tipo_dato=tipo_variable,
        categoria="variable",
        mutable=nodo.es_mutable,
        linea=nodo.linea,
        columna=nodo.columna,
    )

    simbolo.inicializado = tiene_valor
    simbolo.tipo_inferido = inferido

    if not tabla.declarar(simbolo):
        tabla.ambito_actual.simbolos[nodo.nombre] = simbolo


# ------------------------------------------------------------
# Acceso a variables (provisional)
# ------------------------------------------------------------

def validar_acceso_variable(nodo: Identificador, tabla: TablaSimbolos,
                            errores: List[ErrorCompilador]) -> str:
    """Tipo de la variable. No reporta errores: 'variable no declarada' y
    'fuera de ámbito' pertenecen a la categoría Identificadores."""
    simbolo = tabla.buscar(nodo.nombre)
    if simbolo is None or simbolo.categoria != "variable":
        return TIPO_DESCONOCIDO
    return simbolo.tipo_dato


# ------------------------------------------------------------
# Asignación
# ------------------------------------------------------------

def validar_asignacion_mutabilidad(nodo: Asignacion, tabla: TablaSimbolos,
                                   tipo_valor: str, errores: List[ErrorCompilador]) -> None:

    if not nodo.objetivo.isidentifier():
        return

    simbolo = tabla.buscar(nodo.objetivo)
    if simbolo is None or simbolo.categoria != "variable":
        return  # no declarada: la reporta la categoría Identificadores

    # Regla 1: una variable inmutable no puede reasignarse.
    if not simbolo.mutable and getattr(simbolo, "inicializado", True):
        _error(errores, nodo,
               f'No se puede asignar dos veces a la variable inmutable "{nodo.objetivo}".')

    # Regla 2: el valor asignado debe coincidir con el tipo de la variable.
    if nodo.operador == "=" and _tipo_confiable(nodo.valor):
        clase_valor = _numerico_libre(nodo.valor, tabla)
        clase_esperado = (_clase_numerica(simbolo.tipo_dato)
                          if getattr(simbolo, "tipo_inferido", False) else None)
        if not _compatible(simbolo.tipo_dato, tipo_valor, clase_valor, clase_esperado):
            _error(errores, nodo,
                   f"Se esperaba {simbolo.tipo_dato} pero se encontró {tipo_valor}.")
