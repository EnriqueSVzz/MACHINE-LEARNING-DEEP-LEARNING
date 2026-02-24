# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 16:51:47 2025

@author: PC
"""

persona = { "nombre" : "Juan",
           "Edad": 33,
           "Direccion": "Reforma 333"}

print("\n Diccionario: ", persona)
print("\n Persona.Edad: ", persona["Edad"])
print("\n Persona.get(Edad): ", persona.get("Edad"))

"""
Iterar sobre un diccionario
"""
# Imprimir solo los valores
for valor in persona.values():
    print(valor)

# Imprimir solo los diccionarios
for llave in persona.keys():
    print(llave)
    
# Imprimir los elementos, pero en forma de tupla
for elemento in persona.items():
    print(elemento)

# Imprimir pero desempaquetando la tupla
for llave, valor in persona.items():
    print(llave,valor)
    

"""
Modificando Tuplas
"""

persona["Direccion"] = "Reforma 400"
print("\n Diccionario: ", persona)

"""
Actualizando contenido
"""
persona.update({"Direccion": "Reforma 500", "Altura" : 1.70})
print("\n Diccionario: ", persona)

#Agregar una llave inexistente
persona["peso"] = 90
print("\n Diccionario: ", persona)

#Borrando un valor de un diccionario
persona.pop("peso")
print("\n Diccionario: ", persona)


# Contar la diferentes palabras que aparecen en un texto
texto = "Hola soy programador, ser programador es muy interesante"

simbolosEliminar = (",",".","(",")")

for simbolo in simbolosEliminar:
    texto = texto.replace(simbolo, "")
    
texto = texto.upper()

#Sacamos todas las palabras en una lista y creamos nuestro diccionario
vocablos = texto.split()
palabras = {}

for vocablo in vocablos:
    # Si ya existe la llave, sumamos 1 a su valor
    if vocablo in palabras.keys():
        palabras[vocablo] = palabras[vocablo] + 1
    else:
        palabras[vocablo] = 1

print("\n Palabras: ", palabras)

#Ordenar en base a la frecuencia
lista = list(palabras.items()) #nos regresa una lista de tuplas
lista.sort(key = lambda palabra : palabra[1])
print("\n Palabras Ordenada Desc: ", lista)

lista.sort(key = lambda palabra : palabra[1], reverse = True)
print("\n Palabras Ordenada Asc: ", lista)

