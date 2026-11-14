# ============================================================
# Windsor Estrada
#   Impresión (println! / print!), expresiones aritméticas (+ - * / % y `as`; el negativo ya está en base.py),
#   arreglos y tuplas, if / else if / else, fn main y clausuras.
# ============================================================

from .base import *

def p_impresion(p):
    """expresion : MACRO LPAREN lista_args RPAREN
                 | MACRO LPAREN RPAREN"""

def p_lista_args(p):
    """lista_args : valor
                  | lista_args COMMA valor"""

def p_aritmetica(p):
    """expresion : expresion PLUS expresion
                 | expresion MINUS expresion
                 | expresion MULTIPLY expresion
                 | expresion DIVIDE expresion
                 | expresion MODULO expresion
                 | expresion AS tipo"""

def p_arreglo_literal(p):
    """expresion : LBRACKET lista_args RBRACKET
                 | LBRACKET RBRACKET
                 | LBRACKET valor SEMICOLON expresion RBRACKET"""

def p_indice(p):
    "expresion : expresion LBRACKET expresion RBRACKET"

def p_tipo_arreglo(p):
    """tipo : LBRACKET tipo RBRACKET
            | LBRACKET tipo SEMICOLON expresion RBRACKET"""

def p_tupla_literal(p):
    """expresion : LPAREN RPAREN
                 | LPAREN valor COMMA RPAREN
                 | LPAREN valor COMMA lista_args RPAREN"""

def p_tupla_acceso(p):
    "expresion : expresion DOT INTEGER_LITERAL"

def p_tipo_tupla(p):
    "tipo : LPAREN lista_tipos RPAREN"

def p_if(p):
    """if_expr : IF expresion bloque
               | IF expresion bloque ELSE bloque
               | IF expresion bloque ELSE if_expr"""

def p_if_sentencia(p):
    "sentencia : if_expr"

def p_if_valor(p):
    "valor : if_expr"

def p_sentencia_bloque(p):
    "sentencia : bloque"

def p_sentencia_funcion(p):
    "sentencia : FN ID LPAREN RPAREN bloque"

def p_clausura(p):
    """expresion : PIPE lista_params_clausura PIPE expresion %prec CLAUSURA
                 | PIPE lista_params_clausura PIPE bloque %prec CLAUSURA
                 | OR expresion %prec CLAUSURA
                 | OR bloque %prec CLAUSURA
                 | MOVE PIPE lista_params_clausura PIPE expresion %prec CLAUSURA
                 | MOVE PIPE lista_params_clausura PIPE bloque %prec CLAUSURA
                 | MOVE OR expresion %prec CLAUSURA
                 | MOVE OR bloque %prec CLAUSURA"""

def p_params_clausura(p):
    """lista_params_clausura : param_clausura
                             | lista_params_clausura COMMA param_clausura"""

def p_param_clausura(p):
    """param_clausura : ID
                      | ID COLON tipo"""
