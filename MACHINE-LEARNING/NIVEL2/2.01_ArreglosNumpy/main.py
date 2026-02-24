# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 20:59:35 2025

@author: PC

Notas:
    * Los arreglos de numpy, pueden ejecutarse mucho más rápido que las listas.
    * Siempre usarlo como np
    * Con arange, nos genera los numeros, pero sin incluir el ultimo
    * comparte muchas funciones con la lista original
"""

import numpy as np

# Definimos unos arreglos
arreglo1 = np.array([1,2,3,4,5,6])
arreglo2 = np.arange(1,7)
lista = [1,2,3,4,5,6]
print(arreglo1)
print(arreglo2)
print(lista)

print(type(arreglo1))
print(type(lista))

# Comparte muchas funciones con las listas normales
print(arreglo1[1:4])
# esto no modifica el arrglo, solo el orden de impresión
print(arreglo1[::-1])  
# Tambien podemos usar size, pero no hay que poner '()'
print(arreglo1.size)
print(len(arreglo1))

# Ordenado
print(arreglo1.sort())

# Tipo de datos del arreglo, tampoco lleva parentesís
# Hay diferentes tipo de enteros, en este caso tenemos int32
print(arreglo1.dtype)

# Refefinir el tamaño del arreglo
# Aquí lo refinimos como 2x3
arreglo3 = arreglo1.reshape(2, 3)
print(arreglo3)

# Aquí agreamos un nuevo valor
# Pero no modifica al arreglo original, tenemos que asignarlo
arreglo3 = np.append(arreglo3,[7,8,9])
arreglo3 = arreglo3.reshape(3, 3)
print("Arreglo Append:\n",arreglo3)

# Insetar un valor en un index del arreglo, tenemos que asignarlos
# porque tampoco modifica al arreglo original
arreglo3 = np.insert(arreglo3,0,0)
print("Insert:\n",arreglo3)

# Sería mismo caso para el borrado por index
# aquí borramos el 9
arreglo3 = np.delete(arreglo3,9)
print("Insert:\n",arreglo3)

# Ahora busquemos un número en el arreglo
# esto nos devolverá un array con todos los index y su data type
arreglo3 = np.append(arreglo3,0)
results = np.where(arreglo3 == 0)
print("Results:\n",results)

# operaciones vectoriales
# Sumar 1 a todos los elementos
arreglo3 = arreglo3 + 1
print("Suma+1:\n",arreglo3)


"""
EJERCICIO
"""
# En Numpy todos los tipos de datos deben ser HOMOGENEOS (mismo tipo)
altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78])
peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6])

# Calcular el IMC
# al trabajar con Numpy, esto nos devolverá un solo arreglo
imc = peso/ (altura * altura)

print("\nIMC:", imc)

# Obtener el promedio
print("\nIMC Promedio:", imc.mean())
print("\nIMC Min:", imc.min())
print("\nIMC Max:", imc.max())






