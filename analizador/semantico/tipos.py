TIPO_I32 = "i32"
TIPO_I64 = "i64"
TIPO_F64 = "f64"
TIPO_BOOL = "bool"
TIPO_STR = "&str"
TIPO_STRING = "String"
TIPO_CHAR = "char"
TIPO_VOID = "()"
TIPO_DESCONOCIDO = "desconocido"
TIPO_ERROR = "error"

TIPOS_NUMERICOS = {TIPO_I32, TIPO_I64, TIPO_F64, "u32", "u64", "f32"}


def es_tipo_numerico(tipo: str) -> bool:
    return tipo in TIPOS_NUMERICOS


def son_tipos_compatibles(tipo_esperado: str, tipo_recibido: str) -> bool:
    if tipo_esperado == TIPO_DESCONOCIDO or tipo_recibido == TIPO_DESCONOCIDO:
        return True
    if tipo_esperado == tipo_recibido:
        return True
    return False
