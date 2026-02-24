# -*- coding: utf-8 -*-
"""
Created on Thu May  1 17:56:17 2025

@author: PC
"""

import numpy as np

# Un Array de 5x2
altura_pesos = np.array([
    [1.74,91.40],
    [1.80,88.70],
    [1.78,87.30],
    [1.68,62.70],
    [1.78,81.60]
    ])

# Este busca entre todos los valores y saca el mimino
print("Minimo:", altura_pesos.min())
# Igualmente pero este saca el máximo
print("Max:", altura_pesos.max())

# Te devuelven el valor minimo de todos estos valores
print("Posición Minimo:", altura_pesos.argmin())
print("Posición Maximo:", altura_pesos.argmax())

# Literal suma todos los valores
print("Suma:", altura_pesos.sum())
# Promedio de todos los valores
print("Promedio:", altura_pesos.mean())

# Lo anterior no nos sirve para el procesamiento de datos, 
# tenemosque hacerlo por eje
print("\n\nMinimo por Fila:", altura_pesos.min(axis=0))
print("Max por Fila:", altura_pesos.max(axis=0))
print("Posición Minimo por Fila :", altura_pesos.argmin(axis=0))
print("Posición Maximopor Fila:", altura_pesos.argmax(axis=0))
print("Suma por Fila:", altura_pesos.sum(axis=0))
print("Promedio por Fila:", altura_pesos.mean(axis=0))

# Transponer el arreglo
altura_pesos = altura_pesos.transpose()
print("\n\n",altura_pesos)
