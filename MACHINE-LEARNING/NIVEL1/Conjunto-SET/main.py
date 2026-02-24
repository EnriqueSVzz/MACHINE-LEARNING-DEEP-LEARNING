# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:28:16 2025

@author: PC
"""

#Definimos nombres de niños nacidos en el 2020
nombres2020 = {"Juan", "Pedro", "Luis", "Pedro"}
nombres2021 = {"Luis", "Maria", "Rosa"}

#En los conjuntos no existen elementos repetidos
# No hay garantia de orden.
print("\n Nacidos en 2020: ", nombres2020)

#Si agregamos un elemento ya existe, simplemente no lo agrega
nombres2021.add("Luis")
# No hay garantia de orden.
print("\n Después de Agregar a Luis (No hubo cambios): ", nombres2021)

#Agregar un nuevo elemento
nombres2021.add("Jose")
# No hay garantia de orden.
print("\n Después de Agregar a Jose (si hubo cambios): ", nombres2021)

#Remover un elemento del conjunto
nombres2021.remove("Jose")
print("\n Después de Borrar a Jose: ", nombres2021)

#Union de 2 Conjuntos
conjuntos = nombres2020.union(nombres2021)
print("\n Unión de los 2 Conjunto ", conjuntos)

#Intersección de 2 Conjuntos
conjuntos = nombres2020.intersection(nombres2021)
print("\n Intersección de los 2 Conjunto ", conjuntos)

# Mostrar todo lo que no esta A Intersección B
A_Union_B = nombres2020.union(nombres2021)
A_Interseccion_B = nombres2020.intersection(nombres2021)
Not_A_Interseccion_B = A_Union_B.difference(A_Interseccion_B)
print("\n Fuera la Interccion de A y B ", Not_A_Interseccion_B)

#Ver si un sunconjunto esta dentro de Otro
print("\n Nombres2020 es SubConjunto de A U B? ", nombres2020.issubset(A_Union_B))
print("\n A U B es SubConjunto de Nombres2020? ", A_Union_B.issubset(nombres2020))

# Preguntar por superConjunto
print("\n Nombres2020 es SuperConjunto de A U B? ", nombres2020.issuperset(A_Union_B))
print("\n A U B es SuperConjunto de Nombres2020? ", A_Union_B.issuperset(nombres2020))

