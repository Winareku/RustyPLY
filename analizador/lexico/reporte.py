from ..comun.logs import cabecera, seccion_errores

def generar_reporte(resultado, ruta, usuario, ahora):
    lineas = cabecera("ANALIZADOR LÉXICO - RUST (PLY)", ruta, usuario, ahora)
    lineas += ["=== TOKENS RECONOCIDOS ===",
               f"{'LÍNEA':<7}{'COL':<6}{'TIPO':<18}VALOR", "-" * 55]
    for t in resultado.tokens:
        lineas.append(f"{t.linea:<7}{t.columna:<6}{t.tipo:<18}{t.valor!r}")
    lineas += seccion_errores("ERRORES LÉXICOS", resultado.errores)
    lineas += ["", "=== RESUMEN ===",
               f"Tokens reconocidos: {len(resultado.tokens)}",
               f"Errores léxicos   : {len(resultado.errores)}"]
    return "\n".join(lineas) + "\n"
