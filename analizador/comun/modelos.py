from dataclasses import dataclass

FASE_LEXICA = "léxico"
FASE_SINTACTICA = "sintáctico"
FASE_SEMANTICA = "semántico"


@dataclass(frozen=True)
class Token:
    tipo: str
    valor: str
    linea: int
    columna: int


@dataclass(frozen=True)
class ErrorCompilador:
    fase: str
    linea: int
    columna: int
    mensaje: str

    def __str__(self):
        return f"[ERROR {self.fase}] Línea {self.linea}, Columna {self.columna}: {self.mensaje}"
