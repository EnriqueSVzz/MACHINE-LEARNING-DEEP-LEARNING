# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 21:02:34 2025

@author: PC
"""

import string
from collections import Counter

# Pedimos la frase al usuario
frase = input("Escribe una frase: ")

# Eliminamos signos de puntuación para contar palabras correctamente
sin_puntuacion = frase.translate(str.maketrans('', '', string.punctuation))

# Separamos las palabras
palabras = sin_puntuacion.split()

# Total de palabras
total_palabras = len(palabras)

# Promedio de longitud de palabra
promedio_longitud = sum(len(palabra) for palabra in palabras) / total_palabras if total_palabras > 0 else 0

# Contamos la frecuencia de cada palabra (en minúsculas para evitar distinciones)
frecuencia = Counter(palabra.lower() for palabra in palabras)
palabra_mas_frecuente, frecuencia_max = frecuencia.most_common(1)[0]

# Contamos signos de puntuación originales
cantidad_puntuacion = sum(1 for c in frase if c in string.punctuation)

# Mostramos resultados
print(f"\nTotal de palabras: {total_palabras}")
print(f"Promedio de longitud de palabra: {promedio_longitud:.2f}")
print(f"Palabra más frecuente: '{palabra_mas_frecuente}' ({frecuencia_max} veces)")
print(f"Cantidad de signos de puntuación usados: {cantidad_puntuacion}")
