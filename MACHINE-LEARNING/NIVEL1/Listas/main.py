# -*- coding: utf-8 -*-
"""
Created on Tue Apr  1 20:24:08 2025

@author: PC
"""

edades = [13, 14,34,45,65]
print("Edad[2]", edades[2])

edades[2] = 23
print("Nuevo Edad[2]", edades[2])

#Sublista (el ultimo no esta considerado)
print("Edad {0,2}", edades[0:2])
print("Edad {:4}", edades[:4])
print("Len de Edad: ", len(edades))
print("Edad Maxima ", max(edades))
print("Edad Mimina ", min(edades))
print("Suma de todas las edades ", sum(edades))
print("Promedio las edades ", sum(edades)/len(edades))

#Modicando Listas
edades.insert(2, 50)
print("Nueva Lista", edades)

edades.append(45)
print("Agregando con Append al Final: ", edades)

edades.extend([12,8,24,50,66])
print("Concatenando Listas:", edades)

#Borrando un dato
del edades[1]
edades.remove(12)
print("Borrando:", edades)

#Pop
print("Pop:", edades.pop())

#Frecuencias
print("Frencuencia de 50:", edades.count(50))

#Buscar un index
print("Index de 50:", edades.index(50))

#Lista Ordenada (Mayor a menor)
# Default es de menor a mayor
print("Lista Ordenada:", edades.sort(reverse=True))
print("Lista Ordenada:", edades.reverse())



