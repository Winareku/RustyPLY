# ============================================================
# Israel Romero
# ============================================================

from .base import *
from .base import _columna
from ...semantico.arbol import (
    Asignacion,
    BucleWhile,
    DeclaracionVariable,
)

# Condiciones con conectores lógicos
def p_expresion_comparacion(p):
    """expresion : expresion EQUAL expresion
                 | expresion NOT_EQUAL expresion
                 | expresion LESS_THAN expresion
                 | expresion GREATER_THAN expresion
                 | expresion LESS_EQUAL expresion
                 | expresion GREATER_EQUAL expresion"""

def p_expresion_logica(p):
    """expresion : expresion AND expresion
                 | expresion OR expresion"""

# Declaración de variables

def p_sentencia_declaracion(p):
    "sentencia : declaracion"
    p[0] = p[1]

def p_declaracion_inmutable(p):
    "declaracion : LET ID ASSIGN valor SEMICOLON"
    col = _columna(p.lexer.lexdata, p.lexpos(2))
    p[0] = DeclaracionVariable(
        nombre=p[2],
        tipo_declarado=None,
        es_mutable=False,
        valor_inicial=p[4],
        linea=p.lineno(2),
        columna=col,
    )

def p_declaracion_mutable(p):
    "declaracion : LET MUT ID ASSIGN valor SEMICOLON"
    col = _columna(p.lexer.lexdata, p.lexpos(3))
    p[0] = DeclaracionVariable(
        nombre=p[3],
        tipo_declarado=None,
        es_mutable=True,
        valor_inicial=p[5],
        linea=p.lineno(3),
        columna=col,
    )

def p_declaracion_tipo(p):
    "declaracion : LET ID COLON tipo ASSIGN valor SEMICOLON"
    col = _columna(p.lexer.lexdata, p.lexpos(2))
    p[0] = DeclaracionVariable(
        nombre=p[2],
        tipo_declarado=p[4],
        es_mutable=False,
        valor_inicial=p[6],
        linea=p.lineno(2),
        columna=col,
    )

def p_declaracion_mutable_tipo(p):
    "declaracion : LET MUT ID COLON tipo ASSIGN valor SEMICOLON"
    col = _columna(p.lexer.lexdata, p.lexpos(3))
    p[0] = DeclaracionVariable(
        nombre=p[3],
        tipo_declarado=p[5],
        es_mutable=True,
        valor_inicial=p[7],
        linea=p.lineno(3),
        columna=col,
    )

def p_declaracion_constante(p):
    "declaracion : CONST ID COLON tipo ASSIGN valor SEMICOLON"

def p_declaracion_sin_valor(p):
    """declaracion : LET ID SEMICOLON
                   | LET MUT ID SEMICOLON
                   | LET ID COLON tipo SEMICOLON
                   | LET MUT ID COLON tipo SEMICOLON"""

def p_declaracion_tupla(p):
    "declaracion : LET LPAREN lista_id RPAREN ASSIGN valor SEMICOLON"

def p_lista_id(p):
    """lista_id : ID
                | lista_id COMMA ID"""


# Asignación

def p_sentencia_asignacion(p):
    "sentencia : asignacion"
    p[0] = p[1]

def p_asignacion(p):
    "asignacion : ID operador_asignacion valor SEMICOLON"
    col = _columna(p.lexer.lexdata, p.lexpos(1))
    p[0] = Asignacion(
        objetivo=p[1],
        operador=p[2],
        valor=p[3],
        linea=p.lineno(1),
        columna=col,
    )

def p_operador_asignacion(p):
    """operador_asignacion : ASSIGN
                           | PLUS_ASSIGN
                           | MINUS_ASSIGN
                           | MULTIPLY_ASSIGN
                           | DIVIDE_ASSIGN
                           | MODULO_ASSIGN"""
    p[0] = p[1]


# Estructura de datos: vector

def p_primaria_vector(p):
    "primaria : vector"

def p_vector(p):
    """vector : MACRO LBRACKET lista_args RBRACKET
              | MACRO LBRACKET RBRACKET
              | MACRO LBRACKET valor SEMICOLON expresion RBRACKET"""


# Estructuras de control: while y loop

def p_sentencia_while(p):
    "sentencia : WHILE expresion bloque"
    col = _columna(p.lexer.lexdata, p.lexpos(1))
    p[0] = BucleWhile(condicion=p[2], bloque=p[3], linea=p.lineno(1), columna=col)

def p_sentencia_loop(p):
    "sentencia : LOOP bloque"

def p_sentencia_break(p):
    "sentencia : BREAK SEMICOLON"

def p_sentencia_continue(p):
    "sentencia : CONTINUE SEMICOLON"


# Tipo de función: con parámetros y retorno

def p_sentencia_funcion_retorno(p):
    "sentencia : funcion_retorno"

def p_funcion_retorno(p):
    """funcion_retorno : FN ID LPAREN RPAREN ARROW tipo bloque
                       | FN ID LPAREN lista_parametros RPAREN ARROW tipo bloque"""

def p_sentencia_funcion_parametros(p):
    "sentencia : FN ID LPAREN lista_parametros RPAREN bloque"

def p_lista_parametros(p):
    """lista_parametros : parametro
                        | lista_parametros COMMA parametro"""

def p_parametro(p):
    """parametro : ID COLON tipo
                 | MUT ID COLON tipo"""

def p_sentencia_retorno(p):
    """sentencia : RETURN valor SEMICOLON
                 | RETURN SEMICOLON"""


# Llamadas a funciones
def p_primaria_llamada_funcion(p):
    "primaria : llamada_funcion"

def p_llamada_funcion(p):
    """llamada_funcion : ruta LPAREN lista_args RPAREN
                       | ruta LPAREN RPAREN"""

# ============================================================
# Reglas sintácticas faltantes
# ============================================================

# FAVOR REVISAR SI ENTRAN EN CONFLICTO CON LAS OTRAS

# Rangos

def p_expresion_rango(p):
    """expresion : expresion RANGE expresion
                 | expresion RANGE_INCLUSIVE expresion"""


# Referencia y desreferencia

def p_expresion_referencia(p):
    """expresion : AMPERSAND expresion %prec UMINUS
                 | AMPERSAND MUT expresion %prec UMINUS"""

def p_expresion_desreferencia(p):
    "expresion : MULTIPLY expresion %prec UMINUS"


# Asignación a campo, índice y desreferencia

def p_asignacion_lugar(p):
    "asignacion : lugar operador_asignacion valor SEMICOLON"

def p_lugar(p):
    """lugar : expresion DOT ID
             | expresion DOT INTEGER_LITERAL
             | expresion LBRACKET expresion RBRACKET
             | MULTIPLY expresion %prec UMINUS"""


# Variables globales con static

def p_declaracion_static(p):
    "declaracion : STATIC ID COLON tipo ASSIGN valor SEMICOLON"

def p_declaracion_static_mut(p):
    "declaracion : STATIC MUT ID COLON tipo ASSIGN valor SEMICOLON"
