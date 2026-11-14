from ..comun.logs import cabecera, seccion_errores


def generar_reporte(resultado, ruta, usuario, ahora):
    lineas = cabecera("ANALIZADOR SINTÁCTICO - RUST (PLY)", ruta, usuario, ahora)
    lineas += seccion_errores("ERRORES LÉXICOS", resultado.errores_lexicos)
    lineas += seccion_errores("ERRORES SINTÁCTICOS", resultado.errores)
    lineas += ["", "=== RESUMEN ===",
               f"Errores léxicos    : {len(resultado.errores_lexicos)}",
               f"Errores sintácticos: {len(resultado.errores)}"]
    return "\n".join(lineas) + "\n"
