# Analizador para Rust (PLY) - Lenguajes de Programación
> Grupo 11

| Integrante | Usuario Git | Aporte | Algoritmo de prueba |
|---|---|---|---|
| Windsor Estrada | @Winareku | Delimitadores, comentarios, newline/espacios | `algoritmos/algoritmo1.rs` |
| Israel Romero | @Madakase | Identificadores, macros, palabras reservadas, operadores | `algoritmos/algoritmo2.rs` |
| César Moreira | @MoreiraC18 | Literales, tipos de datos, tokens de error | `algoritmos/algoritmo3.rs` |

## Requisitos
```
pip install -r requirements.txt
```

## Uso
```
python main.py algoritmos/algoritmo1.rs Winareku
python main.py algoritmos/algoritmo1.rs Winareku --fase lexico
```
Genera `logs/<fase>-<usuario>-DD-MM-AAAA-HHhMM.txt` con tokens y errores.

## Estructura
```
main.py            Punto de entrada (elige la fase con --fase)
analizador/
  comun/           Token, ErrorCompilador y utilidades de logs (compartido)
  lexico/          FASE 1 (hecha)
    tokens.py      Palabras reservadas y lista de tokens
    reglas.py      Reglas PLY (separadas por integrante)
    reporte.py     Formato del log léxico
  sintactico/      FASE 2 (pendiente)
  semantico/       FASE 3 (pendiente)
algoritmos/        Programas Rust de prueba
logs/              Resultados de cada ejecución
```

## Cómo añadir una fase nueva
1. Crear `analizador/<fase>/` con una función `analizar(...)` que devuelva un resultado con `errores` (lista de `ErrorCompilador` con su `fase`) y un `reporte.py`.
2. El sintáctico usa `from analizador.lexico import tokens, construir_lexer`.
3. Registrar la fase en el diccionario `FASES` de `main.py`.
