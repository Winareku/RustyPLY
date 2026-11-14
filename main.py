# ------------------------------------------------------------
# main.py - Punto de entrada. Ejecuta una fase y guarda su log.
# Uso: python main.py algoritmos/algoritmo1.rs Winareku [--fase lexico|sintactico]
# ------------------------------------------------------------

import argparse
import sys
from datetime import datetime

from analizador.comun import guardar_log
from analizador.lexico import analizar as analizar_lexico, generar_reporte as reporte_lexico
from analizador.sintactico import analizar as analizar_sintactico, generar_reporte as reporte_sintactico


# (codigo, ruta, usuario, ahora) -> texto
def fase_lexica(codigo, ruta, usuario, ahora):
    return reporte_lexico(analizar_lexico(codigo), ruta, usuario, ahora)


def fase_sintactica(codigo, ruta, usuario, ahora):
    return reporte_sintactico(analizar_sintactico(codigo), ruta, usuario, ahora)


FASES = {
    "lexico": fase_lexica,
    "sintactico": fase_sintactica,
    # "semantico": fase_semantica,
}


def main():
    ap = argparse.ArgumentParser(description="Analizador de Rust (subconjunto)")
    ap.add_argument("archivo", help="archivo .rs a analizar")
    ap.add_argument("usuario", help="usuario Git (se usa en el nombre del log)")
    ap.add_argument("--fase", choices=FASES, default="lexico")
    args = ap.parse_args()

    try:
        with open(args.archivo, encoding="utf-8") as f:
            codigo = f.read()
    except (FileNotFoundError, UnicodeDecodeError) as e:
        print(f"Error: no se pudo leer '{args.archivo}': {e}")
        sys.exit(1)

    ahora = datetime.now()
    texto = FASES[args.fase](codigo, args.archivo, args.usuario, ahora)
    destino = guardar_log(args.fase, args.usuario, texto, ahora)
    print(texto)
    print(f"Log guardado exitosamente en: {destino}")


if __name__ == "__main__":
    main()
