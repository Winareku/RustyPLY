"""FASE SINTÁCTICA (pendiente).

Cómo conectarla con el léxico:
    from analizador.lexico import tokens, construir_lexer   # lista de tokens y lexer fresco
    # PLY yacc: yacc.yacc(); parser.parse(codigo, lexer=construir_lexer())

Contrato sugerido, igual que el léxico:
    def analizar(codigo: str) -> ResultadoSintactico   # (ast, errores)
Los errores deben ser analizador.comun.ErrorCompilador con fase=FASE_SINTACTICA.
Archivos sugeridos: gramatica.py (reglas p_*), ast.py (nodos), reporte.py.
"""
