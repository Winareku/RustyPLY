from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class Simbolo:
    nombre: str
    tipo_dato: str
    categoria: str
    mutable: bool = False
    linea: int = 0
    columna: int = 0
    parametros: Optional[List[Tuple[str, str]]] = None
    tipo_retorno: Optional[str] = None
    campos: Optional[Dict[str, str]] = None


class Ambito:
    def __init__(self, nombre: str = "bloque", padre: Optional["Ambito"] = None):
        self.nombre = nombre
        self.padre = padre
        self.simbolos: Dict[str, Simbolo] = {}

    def insertar(self, simbolo: Simbolo) -> bool:
        if simbolo.nombre in self.simbolos:
            return False
        self.simbolos[simbolo.nombre] = simbolo
        return True

    def buscar_local(self, nombre: str) -> Optional[Simbolo]:
        return self.simbolos.get(nombre)

    def buscar(self, nombre: str) -> Optional[Simbolo]:
        if nombre in self.simbolos:
            return self.simbolos[nombre]
        if self.padre is not None:
            return self.padre.buscar(nombre)
        return None


class TablaSimbolos:
    def __init__(self):
        self.ambito_global = Ambito(nombre="global")
        self.ambito_actual = self.ambito_global

    def abrir_ambito(self, nombre: str = "bloque") -> Ambito:
        nuevo = Ambito(nombre=nombre, padre=self.ambito_actual)
        self.ambito_actual = nuevo
        return nuevo

    def cerrar_ambito(self) -> Optional[Ambito]:
        if self.ambito_actual.padre is not None:
            self.ambito_actual = self.ambito_actual.padre
        return self.ambito_actual

    def declarar(self, simbolo: Simbolo) -> bool:
        return self.ambito_actual.insertar(simbolo)

    def buscar(self, nombre: str) -> Optional[Simbolo]:
        return self.ambito_actual.buscar(nombre)

    def buscar_local(self, nombre: str) -> Optional[Simbolo]:
        return self.ambito_actual.buscar_local(nombre)
