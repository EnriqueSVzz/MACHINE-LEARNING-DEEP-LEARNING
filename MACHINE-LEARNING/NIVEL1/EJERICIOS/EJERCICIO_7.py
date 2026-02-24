# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 21:07:13 2025

@author: PC

Description:
    Haz una función que determine si una palabra o frase es un palíndromo 
    (se lee igual al derecho y al revés). Ignora espacios, mayúsculas y signos.

    Ejemplo: "Anita lava la tina" ➝ es un palíndromo

"""

def isPalindrome(texto):
    # Pasamos todo a mayusculas y borramos espacios extras
    texto = texto.upper().strip()
    
    # Tenemos que borrar los espacios de envio
    simbolosEliminar = (",",".","(",")","'"," ","?")
    for simbolo in simbolosEliminar:
        texto = texto.replace(simbolo, "")
    
    # Inveritimos la cadena
    inv = texto[::-1]
    # Regresamos si son iguales
    return texto == inv


#texto = "Anita lava la tina"
#texto = "Madam, I'm Adam"
texto = "Borrow or rob?"
if(isPalindrome(texto)):
    print("\nSi es palindromo")
else:
    print("\nNo es palindromo")
