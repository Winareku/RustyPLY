import sys
import ply.lex as lex

from ..comun.modelos import ErrorCompilador, FASE_LEXICA
from .tokens import tokens, RESERVADAS


def _columna(texto, pos):
    ultimo_salto = texto.rfind('\n', 0, pos)
    return pos - ultimo_salto


def _registrar_error(lexer, pos, mensaje):
    lexer.errores.append(
        ErrorCompilador(FASE_LEXICA, lexer.lineno, _columna(lexer.lexdata, pos), mensaje))


# =============================================================
# Windsor Estrada: Delimitadores, Comentarios y Saltos de línea
# =============================================================

t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACE    = r'\{'
t_RBRACE    = r'\}'
t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'
t_COMMA     = r','
t_SEMICOLON = r';'
t_COLON     = r':'
t_DOT       = r'\.'
t_HASH      = r'\#'
t_QUESTION  = r'\?'


def t_COMMENT_LINE(t):
    r'//.*'
    pass  # se descarta


def t_COMMENT_BLOCK(t):
    r'/\*'
    datos, pos, profundidad = t.lexer.lexdata, t.lexer.lexpos, 1
    while pos < len(datos) and profundidad:
        if datos.startswith('/*', pos):
            profundidad += 1
            pos += 2
        elif datos.startswith('*/', pos):
            profundidad -= 1
            pos += 2
        else:
            pos += 1
    if profundidad:
        _registrar_error(t.lexer, t.lexpos, "Comentario de bloque sin cerrar")
    t.lexer.lineno += datos.count('\n', t.lexpos, pos)
    t.lexer.lexpos = pos


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t\r'

# ===========================================================
# César: Literales (números, strings, char) y Tipos de datos.
# ===========================================================

def t_STRING_LITERAL(t):
    r'"([^"\\]|\\[\s\S])*"'
    t.lexer.lineno += t.value.count('\n')
    return t


def t_CHAR_LITERAL(t):
    r"""'([^'\\\n]|\\(?:u\{[0-9a-fA-F_]{1,6}\}|x[0-9a-fA-F]{2}|[^\n]))'"""
    return t


def t_FLOAT_LITERAL(t):
    r'(?:[0-9][0-9_]*\.[0-9][0-9_]*(?:[eE][+-]?[0-9][0-9_]*)?|[0-9][0-9_]*[eE][+-]?[0-9][0-9_]*)(?:f32|f64)?|[0-9][0-9_]*(?:f32|f64)|[0-9][0-9_]*\.(?![.a-zA-Z_0-9])'
    return t


def t_INTEGER_LITERAL(t):
    r'(?:0[xX][0-9a-fA-F_]+|0[oO][0-7_]+|0[bB][01_]+|[0-9][0-9_]*)(?:i8|i16|i32|i64|i128|isize|u8|u16|u32|u64|u128|usize)?'
    return t

# ==========================================================
# Israel: Identificadores, Palabras Reservadas y Operadores.
# ==========================================================

def t_RAW_ID(t):
    r'r\#[a-zA-Z_][a-zA-Z0-9_]*'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*(!(?!=))?'
    if t.value.endswith('!'):
        t.type = 'MACRO'
    else:
        t.type = RESERVADAS.get(t.value, 'ID')
    return t


t_LIFETIME = r"'[a-zA-Z_][a-zA-Z0-9_]*"

# Operadores compuestos
t_RANGE_INCLUSIVE = r'\.\.='
t_PLUS_ASSIGN     = r'\+='
t_MINUS_ASSIGN    = r'-='
t_MULTIPLY_ASSIGN = r'\*='
t_DIVIDE_ASSIGN   = r'/='
t_MODULO_ASSIGN   = r'%='
t_AND_ASSIGN      = r'&='
t_OR_ASSIGN       = r'\|='
t_XOR_ASSIGN      = r'\^='
t_EQUAL           = r'=='
t_NOT_EQUAL       = r'!='
t_LESS_EQUAL      = r'<='
t_GREATER_EQUAL   = r'>='
t_AND             = r'&&'
t_OR              = r'\|\|'
t_RANGE           = r'\.\.'
t_PATHSEP         = r'::'
t_ARROW           = r'->'
t_FAT_ARROW       = r'=>'

# Operadores simples
t_PLUS         = r'\+'
t_MINUS        = r'-'
t_MULTIPLY     = r'\*'
t_DIVIDE       = r'/'
t_MODULO       = r'%'
t_LESS_THAN    = r'<'
t_GREATER_THAN = r'>'
t_NOT          = r'!'
t_ASSIGN       = r'='
t_AMPERSAND    = r'&'
t_PIPE         = r'\|'
t_CARET        = r'\^'

# ============================
# César: errores léxicos
# ============================

def t_error(t):
    c = t.value[0]
    if c == '"':
        mensaje = "Cadena de texto sin cerrar"
    elif c == "'":
        mensaje = "Carácter o etiqueta mal formado"
    else:
        mensaje = f"Carácter no reconocido {c!r}"
    _registrar_error(t.lexer, t.lexpos, mensaje)
    t.lexer.skip(1)


def construir_lexer():
    lexer = lex.lex(module=sys.modules[__name__])
    lexer.errores = []
    return lexer
