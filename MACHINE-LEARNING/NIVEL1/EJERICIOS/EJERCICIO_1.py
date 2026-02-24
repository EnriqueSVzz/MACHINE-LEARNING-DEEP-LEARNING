# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 16:30:03 2025

@author: PC

Description

Escribe una función que reciba una cadena y devuelva un 
diccionario con la cantidad de veces que aparece 
cada vocal (a, e, i, o, u). Ignora mayúsculas/minúsculas.

Ejemplo:
contar_vocales("Hola Mundo") 
➝ {'a': 1, 'e': 0, 'i': 0, 'o': 2, 'u': 1}

"""
# Constante tupla con todas las vocales que tenemos
VOCALES = ('A', 'E', 'I', 'O', 'U')

def contar_vocales(texto):
    # Inicializamos nuestro diccionario
    results = { 'A': 0,
                'E': 0,
                'I': 0,
                'O': 0,
                'U': 0}
    # Iteramos por cada vocal existente
    for vocal in VOCALES:
       results[vocal] = texto.count(vocal)
    
    return results

def contar_vocales_GPT(cadena):
    # Inicializamos el diccionario con las vocales en 0
    vocales = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0}

    # Recorremos cada carácter y si es una vocal, sumamos
    for letra in cadena:
        
        # Verificamos que este dentro del diccionario
        if letra in vocales:
            vocales[letra] += 1

    return vocales

runLoop = True
while(runLoop):
    # Leemos nuestra cadena
    texto = input("Ingrese la cadena que busca procesar\n>")
    
    # transformamos a mayusculas y limpiamos nuestra cadena
    texto = texto.upper().strip()
    results = contar_vocales(texto)
    
    # Imprimos el diccionario (se desempaqueta la tupla)
    for llave, valor in results.items():
        print(llave,valor)
    
    opcion = int(input("Desea procesar otra cadena\n1) Si \n2)Terminar\n>"))
    
    if(opcion == 2):
        runLoop = False
    
        