# ============================================================
# César Moreira
#   Ingreso por teclado (io::stdin().read_line(&mut s), .trim(), .parse::<i32>()),
#   struct / impl / instanciación / acceso a campos, HashMap, for y match,
#   métodos con self y funciones asociadas (Self::new).
# Pruebas: algoritmos/sintactico/algoritmo3.rs
# ============================================================
from .base import *

def p_sentencia_entrada_teclado(p):
    "sentencia : entrada_teclado"

def p_entrada_teclado_read_line(p):
    "entrada_teclado : ruta LPAREN RPAREN DOT ID LPAREN AMPERSAND MUT ID RPAREN SEMICOLON"


def p_expresion_metodo_sin_argumento(p):
    "expresion : expresion DOT ID LPAREN RPAREN"

def p_expresion_metodo_generico(p):
    "expresion : expresion DOT ID PATHSEP LESS_THAN tipo GREATER_THAN LPAREN RPAREN"

def p_sentencia_definicion_struct(p):
    "sentencia : definicion_struct"

def p_definicion_struct(p):
    "definicion_struct : STRUCT ID LBRACE campos_struct RBRACE"

def p_campos_struct(p):
    """campos_struct : lista_campos_struct
                        | lista_campos_struct COMMA
                        | empty"""

def p_lista_campos_struct(p):
    """lista_campos_struct : campo_struct
                            | lista_campos_struct COMMA campo_struct"""


def p_campo_struct(p):
    "campo_struct : ID COLON tipo"


def p_valor_instancia_struct(p):
    "valor : instancia_struct"


def p_instancia_struct(p):
    "instancia_struct : ruta LBRACE campos_instancia_struct RBRACE"


def p_campos_instancia_struct(p):
    """campos_instancia_struct : lista_campos_instancia_struct
                                | lista_campos_instancia_struct COMMA
                                | empty"""


def p_lista_campos_instancia_struct(p):
    """lista_campos_instancia_struct : campo_instancia_struct
                                        | lista_campos_instancia_struct COMMA campo_instancia_struct"""


def p_campo_instancia_struct(p):
    "campo_instancia_struct : ID COLON valor"