# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 19:45:42 2025

@author: PC

Description:
    Implementa una versión básica del juego del ahorcado:
        La palabra se guarda en una variable
        El usuario tiene 6 intentos
        Se muestra el progreso del jugador

Mi solución
    1. Tomar una palabra random de un archivo.
    2. Hacer un ciclo infinito hasta que atine la palabra
    3. Hacer inputs de letras
    4. Si el string final es igual al leido, que se detenga

Notas:
    La función enumerate() en Python te permite recorrer una lista (o cualquier iterable) 
    y obtener dos cosas al mismo tiempo:
        * El índice (posición) de cada elemento.
        * El valor del elemento.
    Equivalente
    for i in range(len(colores)):
        print(i, colores[i])
    
    "".join(msg) 
    pega todos los elementos de la lista en una sola cadena de texto, 
    sin espacios entre ellos porque pusiste "" (cadena vacía).

"""

FINAL = "PASARELLA"

# Esto devolverá un string ofuscado
def ofusca(FINAL):
    return "_" * len(FINAL)

# Validamos que la letra exista en el mensaje
def validaLetra(letra):
    global FINAL
    return letra in FINAL

#
def insertLetter(letra, msg):
    global FINAL
    for i, letter in enumerate(FINAL):
        if letra == letter:
            msg[i] = letra

run = True

# Transformamos en este caso el str a lista.
msg = list(ofusca(FINAL))  # <<< Cambiado aquí
vidas = 6
letras_usadas = []

while run:
    print("\nVIDAS:", vidas)
    print("\nLETRAS USADAS:", letras_usadas)
    print("\n", "".join(msg))  # <<< Formato para que salga todo pegado
    letra = input("\nIngresa una letra\n> ").upper().strip()

    if letra in letras_usadas:
        print("\n¡Ya usaste esa letra! Intenta otra.")
        continue

    letras_usadas.append(letra)

    if validaLetra(letra):
        insertLetter(letra, msg)
    else:
        print("\nLetra no forma parte de la palabra...")
        vidas -= 1

    # Validar si ya ganó
    if "_" not in msg:
        print("\n¡Felicidades, adivinaste la palabra!", FINAL)
        run = False

    # Validar si perdió
    if vidas <= 0:
        print("\nSe terminaron las vidas... La palabra era:", FINAL)
        run = False

        
    

