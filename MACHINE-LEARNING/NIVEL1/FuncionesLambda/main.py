# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 15:54:08 2025

@author: PC
"""

"""
En escencia una función lambda, es una especie de función en una 
sola linea, creo que serían el equivalente a las funciones flecha 
en JS

Son más eficientes, pero debe resumirse en una sola expresión
"""

suma = lambda a,b : a + b;
multiplicacion = lambda a,b,c : a*b*c
constandate = lambda : 10

print("Suma: ", suma(1,2))
print("Multiplicacion: ", multiplicacion(4,3,2))
print("Constandate: ", constandate())

#Supongo que tenemos la siguiente:
# Tenemos unos datos de personas que solicitaron un crédito
# tenemos su nombre, edad y el plazo del crédito
# Procedamos a Ordenarlos
personas = [("Juan", 82, 5),("Luisa", 41, 10),("Arnulfo", 75, 20)]

print("\n Lista Desordenada: ", personas)

# La función sort, ordena en base al primer elemento que halla
# este caso usará "nombre", pero podemos espificar que debe ordenar
personas.sort()
print("\nLista Ordenada por Nombre: ", personas)

# Pasamos el segundo parametro
personas.sort(key = lambda personas : personas[1])
print("\nLista Ordenada por Edad: ", personas)

#Ordenando pero haciendo un lógica con la suma
personas.sort(key = lambda personas : personas[1] + personas[2])
print("\nLista Ordenada por Crédito + Edad: ", personas)



