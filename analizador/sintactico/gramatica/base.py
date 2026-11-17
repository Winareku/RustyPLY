from ...comun.modelos import ErrorCompilador, FASE_SINTACTICA
from ...lexico.tokens import tokens
from ...lexico.reglas import _columna
from ...semantico.arbol import (
    Bloque,
    ExpresionUnaria,
    Identificador,
    Literal,
    Programa,
)

start = "programa"
errores_sintacticos = []

precedence = (
    ("right", "CLAUSURA"),
    ("nonassoc", "RANGE", "RANGE_INCLUSIVE"),
    ("left", "OR"),
    ("left", "AND"),
    ("nonassoc", "EQUAL", "NOT_EQUAL", "LESS_THAN", "GREATER_THAN",
                 "LESS_EQUAL", "GREATER_EQUAL"),
    ("left", "PIPE"),
    ("left", "CARET"),
    ("left", "AMPERSAND"),
    ("left", "PLUS", "MINUS"),
    ("left", "MULTIPLY", "DIVIDE", "MODULO"),
    ("left", "AS"),
    ("right", "UMINUS", "UNOT"),
)


def p_programa(p):
    "programa : lista_sentencias"
    p[0] = Programa(sentencias=p[1] or [], linea=1, columna=1)


def p_lista_sentencias(p):
    """lista_sentencias : lista_sentencias sentencia
                        | empty"""
    if len(p) == 3:
        p[0] = (p[1] or []) + ([p[2]] if p[2] is not None else [])
    else:
        p[0] = []


def p_empty(p):
    "empty :"
    p[0] = None


def p_sentencia_valor(p):
    "sentencia : valor SEMICOLON"
    p[0] = p[1]


def p_sentencia_recuperacion(p):
    "sentencia : error SEMICOLON"
    p[0] = None


def p_bloque(p):
    """bloque : LBRACE lista_sentencias RBRACE
              | LBRACE lista_sentencias cola RBRACE"""
    col = _columna(p.lexer.lexdata, p.lexpos(1))
    sentencias = list(p[2] or [])
    if len(p) == 5 and p[3] is not None:
        sentencias.append(p[3])
    p[0] = Bloque(sentencias=sentencias, linea=p.lineno(1), columna=col)


def p_cola(p):
    "cola : expresion"
    p[0] = p[1]


def p_valor(p):
    "valor : expresion"
    p[0] = p[1]


def p_primaria_literal(p):
    """primaria : INTEGER_LITERAL
                | FLOAT_LITERAL
                | STRING_LITERAL
                | CHAR_LITERAL
                | TRUE
                | FALSE"""
    col = _columna(p.lexer.lexdata, p.lexpos(1))
    tok_tipo = p.slice[1].type
    if tok_tipo == "INTEGER_LITERAL":
        t = "i32"
    elif tok_tipo == "FLOAT_LITERAL":
        t = "f64"
    elif tok_tipo == "STRING_LITERAL":
        t = "&str"
    elif tok_tipo == "CHAR_LITERAL":
        t = "char"
    elif tok_tipo in ("TRUE", "FALSE"):
        t = "bool"
    else:
        t = "desconocido"
    p[0] = Literal(tipo_literal=t, valor=p[1], linea=p.lineno(1), columna=col)


def p_primaria_ruta(p):
    "primaria : ruta"
    p[0] = p[1]


def p_primaria_grupo(p):
    "primaria : LPAREN expresion RPAREN"
    p[0] = p[2]


def p_expresion_primaria(p):
    "expresion : primaria"
    p[0] = p[1]


def p_expresion_unaria(p):
    """expresion : MINUS expresion %prec UMINUS
                 | NOT expresion %prec UNOT"""
    col = _columna(p.lexer.lexdata, p.lexpos(1))
    p[0] = ExpresionUnaria(operador=p[1], expresion=p[2], linea=p.lineno(1), columna=col)


def p_ruta(p):
    """ruta : ID
            | DATA_TYPE
            | SELF_TYPE
            | SELF
            | CRATE
            | SUPER
            | ruta PATHSEP ID"""
    col = _columna(p.lexer.lexdata, p.lexpos(1))
    if len(p) == 2:
        p[0] = Identificador(nombre=str(p[1]), linea=p.lineno(1), columna=col)
    else:
        nombre_base = p[1].nombre if hasattr(p[1], "nombre") else str(p[1])
        p[0] = Identificador(nombre=f"{nombre_base}::{p[3]}", linea=p.lineno(1), columna=col)


def p_tipo(p):
    """tipo : ruta
            | ruta LESS_THAN lista_tipos GREATER_THAN
            | AMPERSAND tipo
            | AMPERSAND MUT tipo"""
    if len(p) == 2:
        p[0] = p[1].nombre if hasattr(p[1], "nombre") else str(p[1])
    elif len(p) == 3:
        p[0] = f"&{p[2]}"
    elif len(p) == 4:
        p[0] = f"&mut {p[3]}"
    elif len(p) == 5:
        nombre_base = p[1].nombre if hasattr(p[1], "nombre") else str(p[1])
        p[0] = f"{nombre_base}<{p[3]}>"


def p_lista_tipos(p):
    """lista_tipos : tipo
                   | lista_tipos COMMA tipo"""
    if len(p) == 2:
        p[0] = str(p[1])
    else:
        p[0] = f"{p[1]}, {p[3]}"


def p_error(t):
    if t is None:
        errores_sintacticos.append(ErrorCompilador(
            FASE_SINTACTICA, 0, 0, "Fin de archivo inesperado (¿falta cerrar algo?)"))
        return
    col = _columna(t.lexer.lexdata, t.lexpos)
    errores_sintacticos.append(ErrorCompilador(
        FASE_SINTACTICA, t.lineno, col, f"Token inesperado {t.value!r} ({t.type})"))
