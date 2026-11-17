# Analizador para Rust - Lenguajes de Programación
> Grupo 11

| Integrante | Usuario Git | Fase 1: Léxico | Fase 2: Sintáctico | Fase 3: Semántico |
|---|---|---|---|---|
| Windsor Estrada | @Winareku | Delimitadores, comentarios, newline/espacios | `gramatica/windsor.py` · `algoritmo1_windsor.rs` | `reglas_windsor.py` · Tipos en aritmética y condiciones de control |
| Israel Romero | @Madakase | Identificadores, macros, reservadas, operadores | `gramatica/israel.py` · `algoritmo2_israel.rs` | `reglas_israel.py` · Inmutabilidad y compatibilidad de tipos |
| César Moreira | @MoreiraC18 | Literales, tipos de datos, errores | `gramatica/cesar.py` · `algoritmo3_cesar.rs` | `reglas_cesar.py` · Structs y funciones |

---

## Requisitos

```bash
pip install -r requirements.txt
```

---

## Uso

El analizador permite ejecutar individualmente cada una de las 3 fases del compilador usando la bandera `--fase`:

### 1. Fase Léxica
```bash
python main.py algoritmos/lexico/algoritmo1_windsor.rs Winareku --fase lexico
python main.py algoritmos/lexico/algoritmo2_israel.rs Madakase --fase lexico
python main.py algoritmos/lexico/algoritmo3_cesar.rs MoreiraC18 --fase lexico
```

### 2. Fase Sintáctica
```bash
# Algoritmos sintácticamente válidos
python main.py algoritmos/sintactico/algoritmo1_windsor.rs Winareku --fase sintactico
python main.py algoritmos/sintactico/algoritmo2_israel.rs Madakase --fase sintactico
python main.py algoritmos/sintactico/algoritmo3_cesar.rs MoreiraC18 --fase sintactico

# Casos de prueba de errores sintácticos
python main.py algoritmos/sintactico/ejemplo_errores.rs Winareku --fase sintactico
```

### 3. Fase Semántica
```bash
# Algoritmos semánticamente válidos
python main.py algoritmos/semantico/algoritmo1_windsor.rs Winareku --fase semantico
python main.py algoritmos/semantico/algoritmo2_israel.rs Madakase --fase semantico
python main.py algoritmos/semantico/algoritmo3_cesar.rs MoreiraC18 --fase semantico

# Casos de prueba de errores semánticos por integrante
python main.py algoritmos/semantico/ejemplo_errores_windsor.rs Winareku --fase semantico
python main.py algoritmos/semantico/ejemplo_errores_israel.rs Madakase --fase semantico
python main.py algoritmos/semantico/ejemplo_errores_cesar.rs MoreiraC18 --fase semantico

# Caso de prueba de errores semánticos integrado (Grupo 11)
python main.py algoritmos/semantico/ejemplo_errores.rs Winareku --fase semantico
```

> **Formato de logs generados en `logs/`:**
> - Léxico y sintáctico: `<fase>-<usuario>-DD-MM-AAAA-HHhMM.txt`
> - Semántico: `semantico-<usuario>-DDMMAAAA-HHhMM.txt`

---

## Estructura del Proyecto

```
├── algoritmos/
│   ├── lexico/                                 # Fase 1: Programas de prueba léxica
│   │   ├── algoritmo1_windsor.rs (algoritmo1.rs)
│   │   ├── algoritmo2_israel.rs  (algoritmo2.rs)
│   │   └── algoritmo3_cesar.rs   (algoritmo3.rs)
│   ├── sintactico/                             # Fase 2: Programas de prueba sintáctica
│   │   ├── algoritmo1_windsor.rs (algoritmo1.rs)
│   │   ├── algoritmo2_israel.rs  (algoritmo2.rs)
│   │   ├── algoritmo3_cesar.rs   (algoritmo3.rs)
│   │   └── ejemplo_errores.rs                  # Detección de errores sintácticos
│   └── semantico/                              # Fase 3: Programas de prueba semántica
│       ├── algoritmo1_windsor.rs (algoritmo1.rs)  # Pruebas válidas de Windsor
│       ├── algoritmo2_israel.rs  (algoritmo2.rs)   # Pruebas válidas de Israel
│       ├── algoritmo3_cesar.rs   (algoritmo3.rs)   # Pruebas válidas de César
│       ├── ejemplo_errores_windsor.rs             # Errores aritméticos y condiciones
│       ├── ejemplo_errores_israel.rs              # Errores de mutabilidad y asignación
│       ├── ejemplo_errores_cesar.rs               # Errores de structs y funciones
│       └── ejemplo_errores.rs                     # Caso integrado de errores semánticos
├── analizador/
│   ├── comun/                                  # Modelos compartidos, tokens y utilidades de log
│   │   ├── __init__.py
│   │   ├── logs.py
│   │   └── modelos.py
│   ├── __init__.py
│   ├── lexico/                                 # FASE 1: Analizador Léxico
│   │   ├── __init__.py
│   │   ├── reglas.py
│   │   ├── reporte.py
│   │   └── tokens.py
│   ├── sintactico/                             # FASE 2: Analizador Sintáctico
│   │   ├── gramatica/
│   │   │   ├── base.py                         # Esqueleto común: precedencia, AST base, p_error
│   │   │   ├── cesar.py                        # Reglas de César (structs, for, match)
│   │   │   ├── __init__.py                     # Integración de gramática en un solo parser PLY
│   │   │   ├── israel.py                       # Reglas de Israel (variables, while, funciones)
│   │   │   └── windsor.py                      # Reglas de Windsor (aritmética, if/else, arreglos)
│   │   ├── __init__.py
│   │   └── reporte.py
│   └── semantico/                              # FASE 3: Analizador Semántico
│       ├── arbol.py                            # Definición de nodos del AST
│       ├── __init__.py                         # Punto de entrada semántico: analizar()
│       ├── reglas_cesar.py                     # Reglas de César: Structs y funciones
│       ├── reglas_israel.py                    # Reglas de Israel: Asignación y mutabilidad
│       ├── reglas_windsor.py                   # Reglas de Windsor: Aritmética y condiciones
│       ├── reporte.py                          # Formato de reporte de logs semánticos
│       ├── tabla_simbolos.py                   # Tabla de símbolos jerárquica con ámbitos
│       ├── tipos.py                            # Representación de tipos y compatibilidad
│       └── verificador.py                      # Visitante del AST y orquestador semántico
├── logs/                                       # Registros generados en cada prueba
├── main.py                                     # CLI ejecutor multi-fase
├── README.md
└── requirements.txt
```

---

## Alcance por Fases

### Fase 1: Análisis Léxico (Avance 1)
- **Windsor:** Delimitadores, comentarios de una y varias líneas, caracteres de nueva línea y espacios en blanco.
- **Israel:** Identificadores, macros (`println!`, `vec!`), palabras reservadas, operadores aritméticos, relacionales y lógicos.
- **César:** Literales enteros, flotantes, cadenas, caracteres, booleanos, tipos de datos primitivos y gestión de errores léxicos.

### Fase 2: Análisis Sintáctico (Avance 2)
| Integrante | Estructuras de datos | Control de flujo | Funciones |
|---|---|---|---|
| Windsor | Arreglos, tuplas | `if` / `else if` / `else` | `fn main`, clausuras |
| Israel | Vec (`vec![]`) | `while`, `loop` | Funciones con parámetros y retorno, llamadas |
| César | `struct`, `HashMap` | `for`, `match` | Métodos con `self`, funciones asociadas |

**Decisiones de diseño sintáctico:**
- `read_line` se reconoce con la regla genérica de método (`expresion . ID ( args )`); no hay una regla rígida de teclado porque rompía `.expect()` y llamadas encadenadas.
- Conflicto conocido: `LESS_THAN` en `as T <` (resuelto como shift, igual que en el compilador oficial de Rust).
- En `match`, la coma tras un brazo es opcional si el brazo usa bloque `{ }` o si es el último brazo.

### Fase 3: Análisis Semántico (Avance 3)
Cada integrante contribuyó con 2 reglas semánticas, verificadas en el recorrido del AST:

1. **Windsor Estrada (@Winareku)** — `reglas_windsor.py`:
   - **Regla 1 (Aritmética):** Validación de compatibilidad de tipos en expresiones binarias aritméticas (`+`, `-`, `*`, `/`, `%`). Se asegura que ambos operandos sean numéricos del mismo tipo o reporta necesidad de conversión explícita.
   - **Regla 2 (Condiciones de control):** Validación estricta de condición booleana (`bool`) en estructuras `if` y bucles `while`, impidiendo condiciones enteras o flotantes.
   - **Pruebas:** `algoritmo1_windsor.rs` (válido) y `ejemplo_errores_windsor.rs` (errores).

2. **Israel Romero (@Madakase)** — `reglas_israel.py`:
   - **Regla 1 (Inmutabilidad):** Control de mutabilidad en asignaciones, impidiendo reasignar variables inmutables (no declaradas con `mut`).
   - **Regla 2 (Asignación y Declaración):** Verificación estricta de coincidencia de tipo en declaraciones con tipo explícito (`let x: T = val;`) y en reasignaciones (`x = val;`).
   - **Pruebas:** `algoritmo2_israel.rs` (válido) y `ejemplo_errores_israel.rs` (errores).

3. **César Moreira (@MoreiraC18)** — `reglas_cesar.py`:
   - **Regla 1 (Funciones):** Detección de funciones duplicadas en el mismo ámbito y validación en llamadas a funciones (existencia, cantidad de argumentos y tipos de argumentos).
   - **Regla 2 (Structs):** Detección de structs duplicados y validación en instanciaciones de structs (campos faltantes, campos no definidos y tipos de datos de campos).
   - **Pruebas:** `algoritmo3_cesar.rs` (válido) y `ejemplo_errores_cesar.rs` (errores).
