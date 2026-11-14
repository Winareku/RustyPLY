import ply.yacc as yacc
from analizador.lexico.tokens import tokens

# ------------------------------------------------------------
# Analizador Sintáctico para subconjunto de Rust
# ------------------------------------------------------------

# ============================================================
# Windsor Estrada
# ============================================================


# ============================================================
# Israel Romero
# ============================================================

# Declaración de variables

# FALTA LA REGLA DE expresion FAVOR AÑADIR

def p_declaracion_inmutable(p):
    'declaracion : LET ID ASSIGN expresion SEMICOLON'

def p_declaracion_mutable(p):
    'declaracion : LET MUT ID ASSIGN expresion SEMICOLON'

def p_declaracion_tipo(p):
    'declaracion : LET ID COLON tipo ASSIGN expresion SEMICOLON'

def p_declaracion_mutable_tipo(p):
    'declaracion : LET MUT ID COLON tipo ASSIGN expresion SEMICOLON'

def p_declaracion_constante(p):
    'declaracion : CONST ID COLON tipo ASSIGN expresion SEMICOLON'

def p_declaracion_tupla(p):
    'declaracion : LET LPAREN lista_id RPAREN ASSIGN expresion SEMICOLON'

# ============================================================
# Cesar Moreira
# ============================================================


# ============================================================
# Construcción del parser
# ============================================================

parser = yacc.yacc()