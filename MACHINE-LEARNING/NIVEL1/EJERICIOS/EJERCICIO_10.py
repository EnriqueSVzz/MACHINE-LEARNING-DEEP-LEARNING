# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 20:34:17 2025

@author: PC

Description:
    Pide al usuario una frase y muestra:
        Total de palabras
        Promedio de longitud de palabra
        Palabra más frecuente
        Cantidad de signos de puntuación usados
"""

import string

# Solicitamos la frase
frase = input("\n Ingrese una frase\n>")

# 1. Eliminar puntuación usando translate
texto_limpio = frase.translate(str.maketrans("", "", string.punctuation))

# 2. Pasar todo a mayusculas  y dividir en palabras
palabras = texto_limpio.upper().split()

# 3. Eliminar duplicados si solo quieres una instancia por palabra
palabras_unicas = list(set(palabras))

# 4. Ordenar por longitud (descendente)
palabras_ordenadas = sorted(palabras_unicas, key=len, reverse=True)



# Resultados
print("\n Total de palabras:", len(palabras_ordenadas))


