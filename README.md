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
python main.py algoritmos/sintactico/ejemplo_errores.rs Winareku --fase sintactico
```

Genera `logs/<fase>-<usuario>-DD-MM-AAAA-HHhMM.txt` (tokens y errores léxicos en la fase léxica; errores léxicos y sintácticos en la sintáctica).

## Estructura

```
├── algoritmos/                 # Programas Rust de prueba (léxico)
│   ├── algoritmo1.rs
│   ├── algoritmo2.rs
│   ├── algoritmo3.rs
│   └── sintactico/             # Programas de prueba (sintáctico)
│       ├── algoritmo1.rs
│       ├── algoritmo2.rs
│       ├── algoritmo3.rs
│       └── ejemplo_errores.rs  # Prueba de errores sintácticos
├── analizador/
│   ├── comun/                  # Token, ErrorCompilador y utilidades de logs
│   │   ├── **init**.py
│   │   ├── logs.py
│   │   └── modelos.py
│   ├── **init**.py
│   ├── lexico/                 # FASE 1 (hecha)
│   │   ├── **init**.py
│   │   ├── reglas.py
│   │   ├── reporte.py
│   │   └── tokens.py
│   ├── semantico/              # FASE 3 (pendiente)
│   │   └── **init**.py
│   └── sintactico/             # FASE 2 (hecha)
│       ├── gramatica/
│       │   ├── base.py         # Esqueleto común: precedencia, programa, bloque, tipo, p_error
│       │   ├── cesar.py        # Reglas de César
│       │   ├── **init**.py     # Junta todo en una sola gramática (exigencia de PLY)
│       │   ├── israel.py       # Reglas de Israel
│       │   └── windsor.py      # Reglas de Windsor
│       ├── **init**.py         # analizar(codigo) -> errores sintácticos
│       └── reporte.py          # Formato del log sintáctico
├── logs/                       # Resultados de cada ejecución
├── main.py                     # Punto de entrada (elige la fase con --fase)
├── README.md
└── requirements.txt
```

## Alcance del avance 2
| Integrante | Estructuras de datos | Control | Funciones |
|---|---|---|---|
| Windsor | arreglos, tuplas | if / else if / else | `fn main`, clausuras |
| Israel | Vec (`vec![]`) | while, loop | con parámetros y retorno, llamadas |
| César | struct, HashMap | for, match | métodos con `self`, funciones asociadas |

Decisiones:
- `read_line` se reconoce con la regla genérica de método (`expresion . ID ( args )`); no hay una regla rígida de teclado porque rompía `.expect()` y llamadas encadenadas.
- Conflicto conocido: `LESS_THAN` en `as T <` (resuelto como shift, igual que Rust).
- En `match`, la coma tras un brazo es opcional solo si el brazo usa bloque `{ }` o es el último.

## Reglas para escribir la gramática
1. Solo **añadir** alternativas; no redefinir símbolos de `base.py` (`programa`, `sentencia`, `bloque`, `valor`, `expresion`, `primaria`, `ruta`, `tipo`, `lista_tipos`, `lista_args`). Cada regla `p_*` debe existir una sola vez en todo el proyecto (PLY se queda con la última que se importe).
2. A la derecha de `=`, `return` y argumentos usar `valor`, no `expresion`.
3. Literales de struct solo en `valor` / `cola`, nunca en `expresion`. Por eso las condiciones de `if`, `while`, `for` y `match` usan `expresion`: así `if x {` no se confunde con `x { campo: 1 }`.
4. Antes de hacer commit: `DEBUG = True` en `sintactico/__init__.py`, ejecutar y revisar `analizador/sintactico/gramatica/parser.out` con `grep -n "conflict for" parser.out`. El único conflicto aceptado es `LESS_THAN` (el `as T <` de Rust). Volver a `DEBUG = False` y no subir `parser.out`.
5. Un archivo nuevo de reglas se importa en `gramatica/__init__.py`.
