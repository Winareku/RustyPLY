# ============================================================
# Israel Romero
# ============================================================

from .base import *

# Declaración de variables

def p_sentencia_declaracion(p):
    "sentencia : declaracion"


def p_declaracion_inmutable(p):
    "declaracion : LET ID ASSIGN valor SEMICOLON"


def p_declaracion_mutable(p):
    "declaracion : LET MUT ID ASSIGN valor SEMICOLON"


def p_declaracion_tipo(p):
    "declaracion : LET ID COLON tipo ASSIGN valor SEMICOLON"


def p_declaracion_mutable_tipo(p):
    "declaracion : LET MUT ID COLON tipo ASSIGN valor SEMICOLON"


def p_declaracion_constante(p):
    "declaracion : CONST ID COLON tipo ASSIGN valor SEMICOLON"


def p_declaracion_tupla(p):
    "declaracion : LET LPAREN lista_id RPAREN ASSIGN valor SEMICOLON"


def p_lista_id(p):
    """lista_id : ID
                | lista_id COMMA ID"""
