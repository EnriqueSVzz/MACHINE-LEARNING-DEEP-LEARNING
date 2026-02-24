# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 19:19:30 2025

@author: PC

Description:
    Pide al usuario una lista de números separados por comas. Luego muestra:
        Promedio
        Mínimo
        Máximo
        Cantidad de números pares e impares

"""

# Mi solución
"""
def getAverage(lista):
    return sum(lista)/len(lista)

def countOddEvenNumbers(lista):
    odd = 0
    even = 0
    for number in lista:
        razon = (number // 2)
        if (number -  (razon* 2)) == 0:
            odd += 1
        else:
            even += 1
    
    print(f"Pares: {odd}, Impares: {even}")
            

# Pedimos la información
numeros = input("\n Ingrese su lista de números (seguidos por comas)\n>")

# Limpiar la cadena y separar por las comas.
numeros = numeros.strip().split(",")

# Verificamos todos sean números
lista = []
for numero in numeros:
    if numero.isnumeric():
        lista.append(float(numero))
    else:
        print("\n Se ingresó un número no númerico...",numero)
    
#Calculemos el promedio
print("\n Promedio: ", getAverage(lista))
print("\n Valor Minimo: ", min(lista))
print("\n Valor Máximo: ", max(lista))
print("\n Valor Minimo: ", min(lista))
countOddEvenNumbers(lista)
"""

"""
Analisis Solución
"""
# Pedimos al usuario la lista
entrada = input("Introduce números separados por comas: ")

# Transformamos todo los resultados a entero
numeros = list(map(int, entrada.split(",")))

# Calculamos los resultados
promedio = sum(numeros) / len(numeros)
minimo = min(numeros)
maximo = max(numeros)

# Contamos todos los impares
# Ojo que esto es una expresión, y cada que cumpla la solución irá sumando 1 en 1
pares = sum(1 for n in numeros if n % 2 == 0)
impares = sum(1 for n in numeros if n % 2 != 0)

# Mostramos los resultados
print(f"\nPromedio: {promedio:.2f}")
print(f"Mínimo: {minimo}")
print(f"Máximo: {maximo}")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
        



