# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 20:14:03 2025

@author: PC
"""
"""
i = 0
while i < 10:
    print(f"Iteracion [{i+1}]")
    i+=1 #Incrementacion

total = 0
cant_sumas = 5
i = 0
# Cantidad a sumar
while i < cant_sumas:
    num = int(input("Ingrese un número: "))
    total+= num
    i+=1

print("\n La cantidad total de los número es: ", total)
"""
"""
#Validación de contraseña
isPasswordOk = False
respuesta = "admin1234"
while not isPasswordOk:
    password = input("\n Ingrese la contraseña: ")
    if respuesta == password:
        print("Su contraseña es correcta")
        isPasswordOk = True
        
"""
#Iterar sobre una lista
lista = [1,2,3,4,5,6,7,8,9,10,11]

for i in lista:
    print(f"Elemento {i}")

pollos = ("Rigo", "GordoLobo", "Motti")
i = 0
while i < len(pollos):
    print(f"Loro {i+1}: {pollos[i]}")
    i+=1
