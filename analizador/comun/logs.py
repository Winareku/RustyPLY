import os
from datetime import datetime


def cabecera(titulo, ruta, usuario, ahora):
    return [
        titulo,
        f"Archivo analizado : {ruta}",
        f"Usuario Git       : {usuario}",
        f"Fecha y hora      : {ahora.strftime('%d/%m/%Y %H:%M:%S')}",
        "",
    ]


def seccion_errores(titulo, errores):
    lineas = ["", f"=== {titulo} ==="]
    lineas += [str(e) for e in errores] if errores else ["(ninguno)"]
    return lineas


def guardar_log(fase, usuario, texto, ahora=None, carpeta="logs"):
    ahora = ahora or datetime.now()
    os.makedirs(carpeta, exist_ok=True)
    nombre = f"{fase}-{usuario}-{ahora.strftime('%d-%m-%Y-%Hh%M')}.txt"
    destino = os.path.join(carpeta, nombre)
    with open(destino, "w", encoding="utf-8") as f:
        f.write(texto)
    return destino
