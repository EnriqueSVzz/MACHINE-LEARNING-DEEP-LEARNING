# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 17:02:19 2025

@author: PC

Description
Pide al usuario que introduzca el nombre y las notas de varios estudiantes 
(por ejemplo, 3 notas por estudiante). Guarda todo en un diccionario. 

Luego muestra el promedio de cada uno, y si aprobó (>=6).

Temas: diccionarios, bucles, condicionales, funciones, entrada/salida

"""
    
"""
Mi funcion
"""

def getAvarege():
    # Hacemos in ciclo infinito hastaque se acabe se ingresar la calificacion
    notas = []
    subRun = True
    while(subRun):
            nota = int(input("Ingrese la nota (-1 para terminar): "))
            if nota >= 0 and nota <= 100:
                notas.append(nota)
            else:
                subRun = False
    total = 0
    i = 0
    for nota in notas:
        total += nota
        i += 1
    return total / i

"""
Código GPT
"""
def gestionar_estudiantes():
    estudiantes = {}
    cantidad = int(input("¿Cuántos estudiantes vas a registrar?: "))

    for _ in range(cantidad):
        nombre = input("Nombre del estudiante: ") 
        notas = []

        for i in range(1, 4): 
            nota = float(input(f"Ingrese la nota {i} de {nombre}: ")) 
            notas.append(nota)

        estudiantes[nombre] = notas

    print("\n📊 Resultados:")
    for nombre, notas in estudiantes.items():
        # Sacar el promedio
        promedio = sum(notas) / len(notas)
        estado = "Aprobado ✅" if promedio >= 6 else "Reprobado ❌"
        print(f"{nombre}: Promedio = {promedio:.2f} → {estado}")


# Declaramos nuestro arreglo variable
estudiantes = {}

run = True
while(run):
    nombre = input("Ingrese el nombre del Estudiante: ")
    if nombre not in estudiantes:
        estudiantes[nombre] = getAvarege()
    else:
        print("Este estudiante ya fue registrado, terminando proceso")
        run = False

print(estudiantes)




 
    

