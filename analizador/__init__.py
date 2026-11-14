"""Analizador de un subconjunto de Rust.

Fases (cada una en su subpaquete):
    comun/      -> clases compartidas (Token, ErrorCompilador) y utilidades de logs
    lexico/     -> texto  -> lista de tokens            (IMPLEMENTADO)
    sintactico/ -> tokens -> arbol sintactico (AST)     (pendiente)
    semantico/  -> AST    -> verificacion de significado (pendiente)
"""
