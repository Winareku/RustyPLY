from ...comun.modelos import ErrorCompilador, FASE_SINTACTICA
from ...lexico.tokens import tokens
from ...lexico.reglas import _columna

start = "programa"
errores_sintacticos = []

precedence = (
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


def p_lista_sentencias(p):
    """lista_sentencias : lista_sentencias sentencia
                        | empty"""


def p_empty(p):
    "empty :"


def p_sentencia_valor(p):
    "sentencia : valor SEMICOLON"


def p_sentencia_recuperacion(p):
    "sentencia : error SEMICOLON"


def p_bloque(p):
    """bloque : LBRACE lista_sentencias RBRACE
              | LBRACE lista_sentencias cola RBRACE"""


def p_cola(p):
    "cola : expresion"


def p_valor(p):
    "valor : expresion"


def p_primaria_literal(p):
    """primaria : INTEGER_LITERAL
                | FLOAT_LITERAL
                | STRING_LITERAL
                | CHAR_LITERAL
                | TRUE
                | FALSE"""


def p_primaria_ruta(p):
    "primaria : ruta"


def p_primaria_grupo(p):
    "primaria : LPAREN expresion RPAREN"


def p_expresion_primaria(p):
    "expresion : primaria"


def p_expresion_unaria(p):
    """expresion : MINUS expresion %prec UMINUS
                 | NOT expresion %prec UNOT"""


def p_ruta(p):
    """ruta : ID
            | DATA_TYPE
            | SELF_TYPE
            | SELF
            | CRATE
            | SUPER
            | ruta PATHSEP ID"""


def p_tipo(p):
    """tipo : ruta
            | ruta LESS_THAN lista_tipos GREATER_THAN
            | AMPERSAND tipo
            | AMPERSAND MUT tipo"""


def p_lista_tipos(p):
    """lista_tipos : tipo
                   | lista_tipos COMMA tipo"""


def p_error(t):
    if t is None:
        errores_sintacticos.append(ErrorCompilador(
            FASE_SINTACTICA, 0, 0, "Fin de archivo inesperado (¿falta cerrar algo?)"))
        return
    col = _columna(t.lexer.lexdata, t.lexpos)
    errores_sintacticos.append(ErrorCompilador(
        FASE_SINTACTICA, t.lineno, col, f"Token inesperado {t.value!r} ({t.type})"))
