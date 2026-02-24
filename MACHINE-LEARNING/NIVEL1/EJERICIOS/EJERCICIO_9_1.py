# -*- coding: utf-8 -*-
"""
Created on Sat Apr 26 20:45:43 2025

@author: PC
"""

import os

def mostrar_progreso(palabra, letras_adivinadas):
    progreso = ""
    
    for letra in palabra:
        if letra in letras_adivinadas:
            progreso += letra + " "
        else:
            progreso += "_ "
    return progreso.strip()

# Palabra a adivinar
palabra_secreta = "python"

# usamos set para evitar palabras dividadas
letras_adivinadas = set()
intentos = 6

# Mientras nos queden intentos
while intentos > 0:
    
    # Limpiamos la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("¡Juego del Ahorcado!")
    print(f"Intentos restantes: {intentos}")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas))
    
    # convertimos la palabra secreta en conjunto y si son iguales terminamos.
    if set(palabra_secreta).issubset(letras_adivinadas):
        print("\n¡Felicidades, ganaste! 🎉")
        break

    letra = input("Adivina una letra: ").lower()
    
    if letra in palabra_secreta:
        letras_adivinadas.add(letra)
    else:
        intentos -= 1
        print("¡Fallaste!")
        input("Presiona Enter para continuar...")

else:
    print(f"\nPerdiste... La palabra era: {palabra_secreta}")
