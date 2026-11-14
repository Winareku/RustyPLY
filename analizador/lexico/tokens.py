# Palabras reservadas
RESERVADAS = {
    'let': 'LET', 'mut': 'MUT', 'const': 'CONST', 'static': 'STATIC',
    'fn': 'FN', 'struct': 'STRUCT', 'enum': 'ENUM', 'union': 'UNION',
    'trait': 'TRAIT', 'impl': 'IMPL', 'type': 'TYPE', 'if': 'IF',
    'else': 'ELSE', 'match': 'MATCH', 'loop': 'LOOP', 'while': 'WHILE',
    'for': 'FOR', 'in': 'IN', 'break': 'BREAK', 'continue': 'CONTINUE',
    'return': 'RETURN', 'true': 'TRUE', 'false': 'FALSE', 'mod': 'MOD',
    'use': 'USE', 'crate': 'CRATE', 'super': 'SUPER', 'self': 'SELF',
    'Self': 'SELF_TYPE', 'pub': 'PUB', 'as': 'AS', 'ref': 'REF',
    'move': 'MOVE', 'dyn': 'DYN', 'where': 'WHERE', 'async': 'ASYNC',
    'await': 'AWAIT', 'unsafe': 'UNSAFE', 'extern': 'EXTERN',
    '_': 'UNDERSCORE',
    **{t: 'DATA_TYPE' for t in (
        'i8', 'i16', 'i32', 'i64', 'i128', 'isize',
        'u8', 'u16', 'u32', 'u64', 'u128', 'usize',
        'f32', 'f64', 'bool', 'char', 'str', 'String')},
}

# Tokens que NO son palabras reservadas.
TOKENS_BASE = (
    # Delimitadores
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET',
    'COMMA', 'SEMICOLON', 'COLON', 'DOT', 'HASH', 'QUESTION',
    # Identificadores
    'ID', 'RAW_ID', 'LIFETIME', 'MACRO',
    # Literales
    'STRING_LITERAL', 'CHAR_LITERAL', 'FLOAT_LITERAL', 'INTEGER_LITERAL',
    # Operadores compuestos
    'RANGE_INCLUSIVE', 'PLUS_ASSIGN', 'MINUS_ASSIGN', 'MULTIPLY_ASSIGN',
    'DIVIDE_ASSIGN', 'MODULO_ASSIGN', 'AND_ASSIGN', 'OR_ASSIGN', 'XOR_ASSIGN',
    'EQUAL', 'NOT_EQUAL', 'LESS_EQUAL', 'GREATER_EQUAL', 'AND', 'OR',
    'RANGE', 'PATHSEP', 'ARROW', 'FAT_ARROW',
    # Operadores simples
    'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'MODULO', 'LESS_THAN',
    'GREATER_THAN', 'NOT', 'ASSIGN', 'AMPERSAND', 'PIPE', 'CARET',
)

# Lista que exige PLY
tokens = TOKENS_BASE + tuple(sorted(set(RESERVADAS.values())))
