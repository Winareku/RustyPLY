"""Junta las reglas de todos los integrantes en UN solo módulo para yacc.

PLY exige una única gramática, por eso cada archivo hace `from .base import *`
y aquí se importan los cuatro. Al agregar un archivo nuevo, impórtalo aquí.
"""
from .base import *      # noqa: F401,F403
from .windsor import *   # noqa: F401,F403
from .israel import *    # noqa: F401,F403
from .cesar import *     # noqa: F401,F403
