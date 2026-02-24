# -*- coding: utf-8 -*-
"""
Created on Thu May  1 18:31:38 2025

@author: PC
"""

import numpy as np

altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78])
peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6])

# podemos agrupar por eje X (axis=0) o Y (axis=1)
# Para el stack por eje X, es como si se apilaran de arriba a abajo
# Por otro lado, con eje y, es como si los pararas y los pones a lado
# de izquiera a derecha
# El valor default siempre será axis=0
print(np.stack((altura,peso), axis=0))
print(np.stack((altura,peso), axis=1))

# o simplemente concatenar
print(np.concatenate((altura,peso)))

"""
EJE X
"""

# usemos el siguiente stack
union = np.stack((altura,peso), axis=0)
print("\n",union, "\n", type(union))

# separados, estonos va a separar en 2 varibles tipos array
# pero dentro de una lista
separados = np.split(union, 2)
print("\n",separados, "\n", type(separados))

"""
EJE Y
"""
union = np.stack((altura,peso), axis=1)
print("\n",union, "\n", type(union))

# Como ya tiene 2 columnas, nos marca error, entonces es mejor
# separarlos por 5
separados = np.split(union, 5)
print("\n",separados, "\n", type(separados))
