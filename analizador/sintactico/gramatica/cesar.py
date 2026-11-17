# ============================================================
# César Moreira
#   Ingreso por teclado (io::stdin().read_line(&mut s), .trim(), .parse::<i32>()),
#   struct / impl / instanciación / acceso a campos, HashMap, for y match,
#   métodos con self y funciones asociadas (Self::new).
# Pruebas: algoritmos/sintactico/algoritmo3.rs
# ============================================================
from .base import *
from .base import _columna
from ...semantico.arbol import DefinicionStruct, InstanciacionStruct

def p_expresion_metodo_sin_argumento(p):
    "expresion : expresion DOT ID LPAREN RPAREN"

def p_expresion_metodo_generico(p):
    "expresion : expresion DOT ID PATHSEP LESS_THAN tipo GREATER_THAN LPAREN RPAREN"

# Definición de structs
def p_sentencia_definicion_struct(p):
    "sentencia : definicion_struct"
    p[0] = p[1]


def p_definicion_struct(p):
    "definicion_struct : STRUCT ID LBRACE campos_struct RBRACE"
    col = _columna(p.lexer.lexdata, p.lexpos(1))

    p[0] = DefinicionStruct(
        nombre=p[2],
        campos=p[4],
        linea=p.lineno(1),
        columna=col,
    )


def p_campos_struct(p):
    """campos_struct : lista_campos_struct
                        | lista_campos_struct COMMA
                        | empty"""
    p[0] = p[1] or {}


def p_lista_campos_struct(p):
    """lista_campos_struct : campo_struct
                            | lista_campos_struct COMMA campo_struct"""
    if len(p) == 2:
        nombre, tipo = p[1]
        p[0] = {nombre: tipo}
    else:
        p[0] = dict(p[1])
        nombre, tipo = p[3]
        p[0][nombre] = tipo


def p_campo_struct(p):
    "campo_struct : ID COLON tipo"
    p[0] = (p[1], p[3])


# Instanciación de structs
def p_valor_instancia_struct(p):
    "valor : instancia_struct"
    p[0] = p[1]


def p_instancia_struct(p):
    "instancia_struct : ruta LBRACE campos_instancia_struct RBRACE"

    p[0] = InstanciacionStruct(
        nombre=p[1].nombre,
        valores_campos=p[3],
        linea=p[1].linea,
        columna=p[1].columna,
    )


def p_campos_instancia_struct(p):
    """campos_instancia_struct : lista_campos_instancia_struct
                                | lista_campos_instancia_struct COMMA
                                | empty"""
    p[0] = p[1] or {}


def p_lista_campos_instancia_struct(p):
    """lista_campos_instancia_struct : campo_instancia_struct
                                    | lista_campos_instancia_struct COMMA campo_instancia_struct"""
    if len(p) == 2:
        nombre, valor = p[1]
        p[0] = {nombre: valor}
    else:
        p[0] = dict(p[1])
        nombre, valor = p[3]
        p[0][nombre] = valor


def p_campo_instancia_struct(p):
    "campo_instancia_struct : ID COLON valor"
    p[0] = (p[1], p[3])


#Acceso a campos de una estructura
def p_expresion_acceso_campo(p):
    "expresion : expresion DOT ID"

# Bloque impl
def p_sentencia_impl(p):
    "sentencia : bloque_impl"


def p_bloque_impl(p):
    "bloque_impl : IMPL tipo LBRACE contenido_impl RBRACE"


# Contenido del bloque impl
def p_contenido_impl(p):
    """contenido_impl : lista_elementos_impl
                        | empty"""


def p_lista_elementos_impl(p):
    """lista_elementos_impl : elemento_impl
                            | lista_elementos_impl elemento_impl"""


# Funciones asociadas y métodos permitidos dentro de impl
def p_elemento_impl(p):
    """elemento_impl : funcion_retorno
                        | metodo_self"""


# Métodos con self, &self o &mut self
def p_metodo_self(p):
    """metodo_self : FN ID LPAREN receptor_self RPAREN bloque
                    | FN ID LPAREN receptor_self COMMA lista_parametros RPAREN bloque
                    | FN ID LPAREN receptor_self RPAREN ARROW tipo bloque
                    | FN ID LPAREN receptor_self COMMA lista_parametros RPAREN ARROW tipo bloque"""


# Formas permitidas para recibir self
def p_receptor_self(p):
    """receptor_self : SELF
                        | AMPERSAND SELF
                        | AMPERSAND MUT SELF"""


# Retorno de una instancia de struct al final de una función
def p_cola_instancia_struct(p):
    "cola : instancia_struct"


# Métodos con argumentos, usados en operaciones como HashMap.insert()
def p_expresion_metodo_con_argumentos(p):
    "expresion : expresion DOT ID LPAREN lista_args RPAREN"


# Estructura de control for
def p_sentencia_for(p):
    """sentencia : FOR ID IN expresion bloque
                 | FOR LPAREN lista_id RPAREN IN expresion bloque"""


# Estructura de control match
def p_sentencia_match(p):
    "sentencia : expresion_match"


def p_expresion_match(p):
    "expresion_match : MATCH expresion LBRACE brazos_match RBRACE"

# Brazos de match. Cada brazo termina en coma; la coma es opcional si el
def p_brazos_match(p):
    """brazos_match : lista_brazos_terminados
                    | lista_brazos_terminados brazo_final
                    | brazo_final"""


def p_lista_brazos_terminados(p):
    """lista_brazos_terminados : brazo_terminado
                                | lista_brazos_terminados brazo_terminado"""


def p_brazo_terminado(p):
    """brazo_terminado : patron_match FAT_ARROW valor COMMA
                        | patron_match FAT_ARROW bloque COMMA
                        | patron_match FAT_ARROW bloque"""


def p_brazo_final(p):
    "brazo_final : patron_match FAT_ARROW valor"


# Patrones permitidos en match
def p_patron_match(p):
    """patron_match : patron_simple
                    | patron_match PIPE patron_simple"""


def p_patron_simple(p):
    """patron_simple : INTEGER_LITERAL
                        | MINUS INTEGER_LITERAL
                        | FLOAT_LITERAL
                        | STRING_LITERAL
                        | CHAR_LITERAL
                        | TRUE
                        | FALSE
                        | UNDERSCORE
                        | ruta
                        | ruta LPAREN lista_patrones RPAREN
                        | INTEGER_LITERAL RANGE_INCLUSIVE INTEGER_LITERAL
                        | CHAR_LITERAL RANGE_INCLUSIVE CHAR_LITERAL"""


def p_lista_patrones(p):
    """lista_patrones : patron_match
                        | lista_patrones COMMA patron_match"""


# match como valor:  let r = match x { ... };
def p_valor_match(p):
    "valor : expresion_match"


# use std::io;  use std::collections::HashMap;
def p_sentencia_use(p):
    "sentencia : USE ruta SEMICOLON"


# Funciones asociadas sin retorno dentro de impl
def p_elemento_impl_sin_retorno(p):
    """elemento_impl : FN ID LPAREN RPAREN bloque
                        | FN ID LPAREN lista_parametros RPAREN bloque"""
