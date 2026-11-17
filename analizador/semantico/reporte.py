from ..comun.logs import cabecera, seccion_errores


def generar_reporte(resultado, ruta, usuario, ahora):
    lineas = cabecera("ANALIZADOR SEMÁNTICO - RUST (PLY)", ruta, usuario, ahora)
    lineas += seccion_errores("ERRORES LÉXICOS", resultado.errores_lexicos)
    lineas += seccion_errores("ERRORES SINTÁCTICOS", resultado.errores_sintacticos)
    lineas += seccion_errores("ERRORES SEMÁNTICOS", resultado.errores)
    lineas += [
        "",
        "=== RESUMEN ===",
        f"Errores léxicos    : {len(resultado.errores_lexicos)}",
        f"Errores sintácticos: {len(resultado.errores_sintacticos)}",
        f"Errores semánticos : {len(resultado.errores)}",
    ]
    return "\n".join(lineas) + "\n"
