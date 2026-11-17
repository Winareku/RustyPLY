from typing import List, Optional
from ..comun.modelos import ErrorCompilador
from .arbol import (
    Asignacion,
    Bloque,
    BucleWhile,
    CondicionalIf,
    DeclaracionVariable,
    DefinicionFuncion,
    DefinicionStruct,
    ExpresionBinaria,
    ExpresionUnaria,
    Identificador,
    InstanciacionStruct,
    Literal,
    LlamadaFuncion,
    NodoAST,
    Programa,
)
from .reglas_cesar import (
    registrar_definicion_funcion,
    registrar_definicion_struct,
    validar_instanciacion_struct,
    validar_llamada_funcion,
)
from .reglas_israel import (
    registrar_variable,
    validar_acceso_variable,
    validar_asignacion_mutabilidad,
)
from .reglas_windsor import (
    validar_condicion_control,
    validar_expresion_aritmetica,
)
from .tabla_simbolos import TablaSimbolos
from .tipos import TIPO_BOOL, TIPO_DESCONOCIDO, TIPO_ERROR


class VerificadorSemantico:
    def __init__(self):
        self.tabla = TablaSimbolos()
        self.errores: List[ErrorCompilador] = []

    def verificar(self, nodo: Optional[NodoAST]) -> List[ErrorCompilador]:
        self.errores.clear()
        if nodo is not None:
            self.visitar(nodo)
        return list(self.errores)

    def visitar(self, nodo: Optional[NodoAST]) -> str:
        if nodo is None:
            return TIPO_DESCONOCIDO

        metodo = getattr(self, f"visitar_{type(nodo).__name__}", self.visitar_defecto)
        return metodo(nodo)

    def visitar_defecto(self, nodo: NodoAST) -> str:
        return TIPO_DESCONOCIDO

    def visitar_Programa(self, nodo: Programa) -> str:
        for sentencia in nodo.sentencias:
            self.visitar(sentencia)
        return TIPO_DESCONOCIDO

    def visitar_Bloque(self, nodo: Bloque) -> str:
        self.tabla.abrir_ambito(nombre="bloque")
        tipo_ultimo = TIPO_DESCONOCIDO
        for sentencia in nodo.sentencias:
            tipo_ultimo = self.visitar(sentencia)
        self.tabla.cerrar_ambito()
        return tipo_ultimo

    def visitar_DeclaracionVariable(self, nodo: DeclaracionVariable) -> str:
        tipo_val = self.visitar(nodo.valor_inicial) if nodo.valor_inicial else TIPO_DESCONOCIDO
        registrar_variable(nodo, self.tabla, tipo_val, self.errores)
        return tipo_val

    def visitar_Asignacion(self, nodo: Asignacion) -> str:
        tipo_val = self.visitar(nodo.valor) if nodo.valor else TIPO_DESCONOCIDO
        validar_asignacion_mutabilidad(nodo, self.tabla, tipo_val, self.errores)
        return tipo_val

    def visitar_ExpresionBinaria(self, nodo: ExpresionBinaria) -> str:
        tipo_izq = self.visitar(nodo.izquierda)
        tipo_der = self.visitar(nodo.derecha)

        if nodo.operador in {"+", "-", "*", "/", "%"}:
            return validar_expresion_aritmetica(nodo, tipo_izq, tipo_der, self.errores)
        elif nodo.operador in {"==", "!=", "<", ">", "<=", ">="}:
            return TIPO_BOOL
        elif nodo.operador in {"&&", "||"}:
            return TIPO_BOOL
        return TIPO_DESCONOCIDO

    def visitar_ExpresionUnaria(self, nodo: ExpresionUnaria) -> str:
        tipo_sub = self.visitar(nodo.expresion)
        if nodo.operador == "!":
            return TIPO_BOOL
        return tipo_sub

    def visitar_Identificador(self, nodo: Identificador) -> str:
        return validar_acceso_variable(nodo, self.tabla, self.errores)

    def visitar_Literal(self, nodo: Literal) -> str:
        return nodo.tipo_literal

    def visitar_CondicionalIf(self, nodo: CondicionalIf) -> str:
        tipo_cond = self.visitar(nodo.condicion)
        if nodo.condicion:
            validar_condicion_control(nodo.condicion, tipo_cond, self.errores)
        if nodo.bloque_si:
            self.visitar(nodo.bloque_si)
        if nodo.bloque_sino:
            self.visitar(nodo.bloque_sino)
        return TIPO_DESCONOCIDO

    def visitar_BucleWhile(self, nodo: BucleWhile) -> str:
        tipo_cond = self.visitar(nodo.condicion)
        if nodo.condicion:
            validar_condicion_control(nodo.condicion, tipo_cond, self.errores)
        if nodo.bloque:
            self.visitar(nodo.bloque)
        return TIPO_DESCONOCIDO

    def visitar_DefinicionFuncion(self, nodo: DefinicionFuncion) -> str:
        registrar_definicion_funcion(nodo, self.tabla, self.errores)
        self.tabla.abrir_ambito(nombre=f"fn_{nodo.nombre}")
        for param_nombre, param_tipo in nodo.parametros:
            from .tabla_simbolos import Simbolo

            self.tabla.declarar(
                Simbolo(
                    nombre=param_nombre,
                    tipo_dato=param_tipo,
                    categoria="variable",
                    mutable=False,
                    linea=nodo.linea,
                    columna=nodo.columna,
                )
            )
        if nodo.bloque:
            self.visitar(nodo.bloque)
        self.tabla.cerrar_ambito()
        return nodo.tipo_retorno or "()"

    def visitar_LlamadaFuncion(self, nodo: LlamadaFuncion) -> str:
        tipos_args = [self.visitar(arg) for arg in nodo.argumentos]
        return validar_llamada_funcion(nodo, self.tabla, tipos_args, self.errores)

    def visitar_DefinicionStruct(self, nodo: DefinicionStruct) -> str:
        registrar_definicion_struct(nodo, self.tabla, self.errores)
        return nodo.nombre

    def visitar_InstanciacionStruct(self, nodo: InstanciacionStruct) -> str:
        tipos_campos = {campo: self.visitar(val) for campo, val in nodo.valores_campos.items()}
        return validar_instanciacion_struct(nodo, self.tabla, tipos_campos, self.errores)
