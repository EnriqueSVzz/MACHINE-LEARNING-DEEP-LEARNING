# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 19:10:03 2025

@author: PC

Description:
    Escribe un programa que lea un archivo de texto (archivo.txt) 
    y muestre las 5 palabras más largas que contiene. 
    Ignora signos de puntuación.

"""

import string

"""
Solución en función
"""

def palabras_mas_largas(nombre_archivo, top=5):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()

    # 1. Eliminar puntuación usando translate
    texto_limpio = texto.translate(str.maketrans("", "", string.punctuation))

    # 2. Pasar todo a minúsculas (opcional) y dividir en palabras
    palabras = texto_limpio.lower().split()

    # 3. Eliminar duplicados si solo quieres una instancia por palabra
    palabras_unicas = list(set(palabras))

    # 4. Ordenar por longitud (descendente)
    palabras_ordenadas = sorted(palabras_unicas, key=len, reverse=True)

    # 5. Tomar las primeras `top` palabras más largas
    return palabras_ordenadas[:top]

"""
SOLUCIÓN 2
"""
def top_5_palabras_mas_largas(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        texto = archivo.read()

    # Quitar signos de puntuación
    texto = texto.translate(str.maketrans('', '', string.punctuation))

    # Convertir a minúsculas (opcional) y dividir en palabras
    palabras = texto.split()

    # Eliminar duplicados (si quieres que sean únicas)
    # Usamos los conjuntos para sacar los unicos, luego los convertimos a listas
    palabras_unicas = list(set(palabras))

    # Ordenar por longitud (de mayor a menor)
    palabras_unicas.sort(key=lambda x: len(x), reverse=True)

    # Mostrar las 5 más largas
    print(" Las 5 palabras más largas del archivo:")
    for palabra in palabras_unicas[:5]:
        print(f"{palabra} ({len(palabra)} caracteres)")



# Definimos nuestro diccionario con todas las palabras
palabras = {}
simbolosEliminar = (",", ".", "(", ")")

# Abrimos nuestro archivo
with open("BackLog.txt", "r", encoding="utf-8") as archivo:

    textos = archivo.readlines()
    
    for linea in textos:
        for simbolo in simbolosEliminar:
            linea = linea.replace(simbolo, "")
        
        linea = linea.upper()
        tokens = linea.split()
        
        for token in tokens:
            if token not in palabras:
                palabras[token] = len(token)

# Ordenar en base a la frecuencia
lista = list(palabras.items())

# Imprimimos de manera descendente
lista.sort(key=lambda palabra: palabra[1], reverse=True)

i = 1
for palabra, frecuencia in lista:
    if i <=5:
        print(f"{palabra}: {frecuencia}")
    i+=1
    
# Solución 1
resultado = palabras_mas_largas("BackLog.txt")
print("\n Las 5 palabras más largas son:")
for palabra in resultado:
    print(f"- {palabra} ({len(palabra)} letras)")

# Solución 2
print("\n Solución 2:")
top_5_palabras_mas_largas("BackLog.txt")





