# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 17:25:26 2025

@author: PC
"""

# Todos los paquetes que tengo instalados
# Inclusive los caducados
#help("modules")
#import math as m#Modulo de mátematicas.

from math import floor, ceil #Esto es muy eficiente
# Tambien podemos hacer esto
# from math import *

"""
importamos nuestros funciones
"""
from manejo_archivos import leer, escribir

# Nos trae todo lo cargado en este modulo.
#help(math)

# Función piso y cielo
# Piso nos trae el número entero más cercano hacía abajo
# Techo nos trae el número entero más cerano hacía arriba
"""
print("Redondeo techo:", m.ceil(2.1))
print("Redondeo techo:", m.ceil(2.9))
print("Redondeo piso:", m.floor(2.1))
print("Redondeo piso:", m.floor(2.9))
"""

print("Redondeo techo:", ceil(2.1))
print("Redondeo techo:", ceil(2.9))
print("Redondeo piso:", floor(2.1))
print("Redondeo piso:", floor(2.9))


# Usamos nuestras funciones
escribir("main.txt", "Hola desde el main!\n")
print(leer("main.txt"))



