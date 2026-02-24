# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 14:41:42 2025

@author: PC
"""

def suma(a,b):
    suma = a+b
    return suma

def addByList(lista):
    total = 0
    for i in lista:
        total +=i
    
    return total

# Sumar por 'N' cantidad de argumentos
# Se su pone que es una tupla
def addByArgs(*numeros): 
    total = 0
    for i in numeros:
        total +=i
    return total

#Función que da formato a los string
def getFormattedString(nombre, apePat, apeMat):
    formato = nombre.capitalize() + " "
    formato += apePat.capitalize() + " "
    formato += apeMat.capitalize()
    return formato

# Función que Calcula el RFC
def getRFC(nombre, fechaNac, codigo):
    nombre = nombre.upper()
    partes = nombre.strip().split()  # Divide en ['JUAN', 'PEREZ', 'LOPEZ']
    
    a_paterno = partes[1]
    a_materno = partes[2]
    nombre_persona = partes[0]

    # Buscar primera vocal interna del apellido paterno
    vocal = ''
    for letra in a_paterno[1:]:
        if letra in 'AEIOU':
            vocal = letra
            break

    RFC = a_paterno[0] + vocal
    RFC += a_materno[0]
    RFC += nombre_persona[0]

    # Agregar fecha en formato: AAMMDD
    RFC += fechaNac[8:]    # Año: "1988"
    RFC += fechaNac[3:5]   # Mes: "05"
    RFC += fechaNac[:2]    # Día: "14"

    RFC += codigo

    return RFC

print("Suma de 2 Números:", suma(4, 3))

#Sumar una lista
lista = [1,2,3,4,5,6,7,7,8,8,9,9,9,7,5,4]
print("\nSuma elementos de una Lista: ", addByList(lista))
print("\nSuma elementos de Args: ", addByArgs(1,2,3,4,5))

# Dado 3 String para un nombre en mayusculas, formatearlos
# Para que solo la primera letra sea Mayusculas
print("\n String formato: ", getFormattedString("JUAN", "PEREZ", "riGo") )

#Calcular el RFC de una persona
print("\n RFC: ", getRFC("Juan Perez Lopez", "14/05/1988", "123") )




