# ===================================================================
# César Moreira — reglas semánticas: 2 reglas para funciones y structs
# ===================================================================

from typing import Dict, List

from ..comun.modelos import ErrorCompilador, FASE_SEMANTICA
from .arbol import (DefinicionFuncion, DefinicionStruct, InstanciacionStruct, LlamadaFuncion)
from .tabla_simbolos import Simbolo, TablaSimbolos
from .tipos import (
    TIPO_ERROR,
    TIPO_VOID,
    son_tipos_compatibles,
)


# Agregar un error semantico usando la ubicación del nodo
def _agregar_error(nodo, mensaje: str, errores: List[ErrorCompilador]):
    errores.append(
        ErrorCompilador(
            FASE_SEMANTICA,
            nodo.linea,
            nodo.columna,
            mensaje,
        )
    )



# Regla semantica 1: funciones
# Registra una función y evita declaraciones duplicadas
def registrar_definicion_funcion(
    nodo: DefinicionFuncion,
    tabla: TablaSimbolos,
    errores: List[ErrorCompilador],
):
    tipo_retorno = nodo.tipo_retorno or TIPO_VOID
    simbolo = Simbolo(
        nombre=nodo.nombre,
        tipo_dato=tipo_retorno,
        categoria="funcion",
        linea=nodo.linea,
        columna=nodo.columna,
        parametros=list(nodo.parametros),
        tipo_retorno=tipo_retorno,
    )

    if not tabla.declarar(simbolo):
        _agregar_error(
            nodo,
            f"La función '{nodo.nombre}' ya fue declarada en este ámbito",
            errores,
        )

# Validar existencia, cantidad y tipos de argumentos de una llamada
def validar_llamada_funcion(
    nodo: LlamadaFuncion,
    tabla: TablaSimbolos,
    tipos_argumentos: List[str],
    errores: List[ErrorCompilador],
) -> str:
    simbolo = tabla.buscar(nodo.nombre)

    if simbolo is None:
        _agregar_error(
            nodo,
            f"La función '{nodo.nombre}' no está declarada",
            errores,
        )
        return TIPO_ERROR
    if simbolo.categoria != "funcion":
        _agregar_error(
            nodo,
            f"El identificador '{nodo.nombre}' no es una función",
            errores,
        )
        return TIPO_ERROR
    parametros = simbolo.parametros or []

    if len(parametros) != len(tipos_argumentos):
        _agregar_error(
            nodo,
            (
                f"La función '{nodo.nombre}' esperaba {len(parametros)} "
                f"argumentos, pero recibió {len(tipos_argumentos)}"
            ),
            errores,
        )

    for posicion, ((_, tipo_esperado), tipo_recibido) in enumerate(
        zip(parametros, tipos_argumentos),
        start=1,
    ):
        if not son_tipos_compatibles(tipo_esperado, tipo_recibido):
            _agregar_error(
                nodo,
                (
                    f"El argumento {posicion} de '{nodo.nombre}' debe ser "
                    f"'{tipo_esperado}', pero se recibió '{tipo_recibido}'"
                ),
                errores,
            )

    return simbolo.tipo_retorno or TIPO_VOID





# Regla semantica 2: structs
# Registrar un struct y evitar declaraciones duplicadas
def registrar_definicion_struct(
    nodo: DefinicionStruct,
    tabla: TablaSimbolos,
    errores: List[ErrorCompilador],
):
    simbolo = Simbolo(
        nombre=nodo.nombre,
        tipo_dato=nodo.nombre,
        categoria="struct",
        linea=nodo.linea,
        columna=nodo.columna,
        campos=dict(nodo.campos),
    )

    if not tabla.declarar(simbolo):
        _agregar_error(
            nodo,
            f"El struct '{nodo.nombre}' ya fue declarado en este ámbito",
            errores,
        )
# Validar la existencia del struct, sus campos y los tipos recibidos
def validar_instanciacion_struct(
    nodo: InstanciacionStruct,
    tabla: TablaSimbolos,
    tipos_campos: Dict[str, str],
    errores: List[ErrorCompilador],
) -> str:
    simbolo = tabla.buscar(nodo.nombre)

    if simbolo is None:
        _agregar_error(
            nodo,
            f"El struct '{nodo.nombre}' no está declarado",
            errores,
        )
        return TIPO_ERROR
    if simbolo.categoria != "struct":
        _agregar_error(
            nodo,
            f"El identificador '{nodo.nombre}' no es un struct",
            errores,
        )
        return TIPO_ERROR
    campos_esperados = simbolo.campos or {}
    nombres_esperados = set(campos_esperados)
    nombres_recibidos = set(tipos_campos)
    hay_error = False
    campos_faltantes = sorted(nombres_esperados - nombres_recibidos)
    if campos_faltantes:
        _agregar_error(
            nodo,
            (
                f"Faltan campos para instanciar '{nodo.nombre}': "
                f"{', '.join(campos_faltantes)}"
            ),
            errores,
        )
        hay_error = True
    campos_desconocidos = sorted(nombres_recibidos - nombres_esperados)
    if campos_desconocidos:
        _agregar_error(
            nodo,
            (
                f"Campos no definidos en '{nodo.nombre}': "
                f"{', '.join(campos_desconocidos)}"
            ),
            errores,
        )
        hay_error = True

    for campo in sorted(nombres_esperados & nombres_recibidos):
        tipo_esperado = campos_esperados[campo]
        tipo_recibido = tipos_campos[campo]
        if not son_tipos_compatibles(tipo_esperado, tipo_recibido):
            _agregar_error(
                nodo,
                (
                    f"El campo '{campo}' de '{nodo.nombre}' debe ser "
                    f"'{tipo_esperado}', pero se recibió '{tipo_recibido}'"
                ),
                errores,
            )
            hay_error = True
    if hay_error:
        return TIPO_ERROR
    return nodo.nombre