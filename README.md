# Analizador para Rust - Lenguajes de Programación
> Grupo 11

| Integrante | Usuario Git | Léxico | Sintáctico (avance 2) |
|---|---|---|---|
| Windsor Estrada | @Winareku | Delimitadores, comentarios, newline/espacios | `gramatica/windsor.py` · `algoritmos/sintactico/algoritmo1.rs` |
| Israel Romero | @Madakase | Identificadores, macros, reservadas, operadores | `gramatica/israel.py` · `algoritmos/sintactico/algoritmo2.rs` |
| César Moreira | @MoreiraC18 | Literales, tipos de datos, errores | `gramatica/cesar.py` · `algoritmos/sintactico/algoritmo3.rs` |

## Requisitos
```
pip install -r requirements.txt
```

## Uso
```
python main.py algoritmos/algoritmo1.rs Winareku                        # léxico (por defecto)
python main.py algoritmos/sintactico/algoritmo2.rs Madakase --fase sintactico
```
Genera `logs/<fase>-<usuario>-DD-MM-AAAA-HHhMM.txt` con tokens/errores.

## Estructura
```
main.py                     Punto de entrada (elige la fase con --fase)
analizador/
  comun/                    Token, ErrorCompilador y utilidades de logs
  lexico/                   FASE 1 (hecha)
  sintactico/               FASE 2 (en curso)
    __init__.py             analizar(codigo) -> errores sintácticos
    reporte.py              Formato del log sintáctico
    gramatica/
      base.py               Esqueleto común: precedencia, programa, bloque, tipo, p_error
      windsor.py israel.py cesar.py   Reglas de cada integrante
      __init__.py           Junta todo en una sola gramática (exigencia de PLY)
  semantico/                FASE 3 (pendiente)
algoritmos/                 Programas Rust de prueba (léxico)
algoritmos/sintactico/      Programas de prueba (sintáctico)
logs/                       Resultados de cada ejecución
```

## Reglas para escribir la gramática
1. Solo **añadir** alternativas; no redefinir símbolos de `base.py` (ver su docstring).
2. A la derecha de `=`, `return` y argumentos usar `valor`, no `expresion`.
3. Literales de struct solo en `valor` / `cola`, nunca en `expresion`.
4. Antes de hacer commit: `DEBUG = True` en `sintactico/__init__.py`, ejecutar y revisar `parser.out`.
   No debe haber conflictos nuevos.
5. Un archivo nuevo de reglas se importa en `gramatica/__init__.py`.
