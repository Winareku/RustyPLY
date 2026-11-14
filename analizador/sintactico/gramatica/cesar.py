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