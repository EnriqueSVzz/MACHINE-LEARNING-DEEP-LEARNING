# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 19:52:50 2025

@author: PC
"""

import numpy as np

# definimos nuestro array
arreglo = np.array([11,12,13,14,15])

# imprimimos nuestros valores mayor a 13
print(np.where(arreglo >= 13))

# también podemos establecer directamente un vector booleano
# la relación tiene que ser 1:1
filtro = [True, False, False, True, True]
print(arreglo[filtro])

"""
Ejercicio
"""

altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78])
peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6])
pais = np.array(["México", "USA", "Canadá", "China", "Perú"])

# aplicamos el siguiente filtro, todos los paises cuyos 
# pesos pasen de 90
# recordemos que estos valores, como si pusieran un vector booleano
# es decir apagar y prender los valores que no cumplen la condición
print(pais[peso>85], pais[peso>85].size)

print(pais[altura>1.75], pais[altura>1.75].size)



# multiplicaciónes vectoriales
# cada quien con el suyo
print(np.array([True, False]) & np.array([False, False]))

# dado lo anterior, ahora también podríamos hacer esto
# debemos poner los parentesis, sino marca error en las condiciones
print(pais[(peso>85) & (altura>1.75)], pais[(peso>85) & (altura>1.75)].size)

print(pais[(peso>85) | (altura>1.75)], pais[(peso>85) | (altura>1.75)].size)
