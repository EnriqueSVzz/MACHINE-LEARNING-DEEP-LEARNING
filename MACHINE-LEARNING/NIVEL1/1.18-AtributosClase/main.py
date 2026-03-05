# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 18:35:01 2025

@author: PC
"""

from Vehiculo import Vehiculo 

# Vehiculo válido
vehiculo_a = Vehiculo(" Rojo ")

# Vehiculo inválido
vehiculo_b = Vehiculo(" Azul")

# Otro Auto
vehiculo_c = Vehiculo("Rosado")

print(vehiculo_a)
print(vehiculo_b)
print(vehiculo_c)

# Comparten folio pero no serie
print("Contador Estático: ", Vehiculo.folio)
print(f" Auto A: serie[{vehiculo_a.serie}], folio[{vehiculo_a.folio}]")
print(f" Auto A: serie[{vehiculo_b.serie}], folio[{vehiculo_b.folio}]")
print(f" Auto A: serie[{vehiculo_c.serie}], folio[{vehiculo_c.folio}]")