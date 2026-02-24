# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 20:04:40 2025

@author: PC
"""

#No podemos modificar las tuplas, pero es mucho más rápida y 
#protege los datos
# En si es lo mismo que una lista, pero estatica
tupla = ("Juan", 22)
print("\n Tupla[0]", tupla[0])

# tupla[0] = "Juana"

#Pero podemos transformar una tupla a lista.
lista = list(tupla)
print("\n lista", lista)

# E igualmente regresar a una tupla 
lista.append("México")
tupla1 = tuple(lista)
print("\n Tupla1: ", tupla1)

# Igualmente podemos convertirla en conjunto.
# Recordemos que en el conjunto no hay garantía de orden
conjunto = set(tupla1)
print("\n Conjunto: ", conjunto)

