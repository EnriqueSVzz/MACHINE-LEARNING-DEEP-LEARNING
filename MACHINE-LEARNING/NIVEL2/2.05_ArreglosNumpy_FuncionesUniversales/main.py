# -*- coding: utf-8 -*-
"""
Created on Thu May  1 18:53:02 2025

@author: PC
"""

import numpy as np
from time import perf_counter #tomar tiempos

# Arreglos princiales
arreglo1 = np.array([1,2,-3,4,5])
arreglo2 = np.array([11,12,13,14,15])

#Funciones vectoriales, son super eficientes
print("\nSUMA:", np.add(arreglo1,arreglo2))
print("\nRESTA:", np.subtract(arreglo1,arreglo2))
print("\nDIVISON:", np.divide(arreglo1,arreglo2))
print("\nMULT:", np.multiply(arreglo1,arreglo2))
print("\nPOTENCIA:", np.power(arreglo1,2))
print("\nABSOLUTO:", np.absolute(arreglo1))

"""
Funciones Universales
"""

# Esto no es una función universal, pierde todo eso
def calcular_imc(peso,altura):
    return peso/(altura*altura)

# Detenemos que hacer que esa función sea nuevamente a ser vectorial
# Tenemos que pasarle el nombre de la función,
# la cantidad de parametros in yla cantidad de salida o return
calcular_imc = np.frompyfunc(calcular_imc, 2, 1)

# ahpra será una función universal
print("\n", type(calcular_imc))
print("\n", calcular_imc(arreglo1,arreglo2))

# tomamos el tiempo en el que empezó a contar
inicio = perf_counter()
# supones que son muchisimos datos
for i in range(10000):
    calcular_imc(arreglo1,arreglo2)

# tomamos captura final
final = perf_counter() 

print("\n Numpy %0.2f" % (final-inicio))

"""
Usando listas
"""
arreglo3 = [1,2,-3,4,5]
arreglo4 = [11,12,13,14,15]

def calcular_imc2(peso,altura):
    return peso/(altura*altura)

imc = []
inicio = perf_counter()
for i in range(10000):
    for j in range(len(arreglo3)):
        imc.append(calcular_imc2(arreglo3[j],arreglo4[j]))

final = perf_counter() 
print("\n Listas %0.2f" % (final-inicio))

