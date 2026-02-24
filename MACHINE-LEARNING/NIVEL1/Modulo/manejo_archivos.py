# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 17:40:51 2025

@author: PC
"""

#Función para escribir en un archivo
def escribir(nombre, texto):
    with open(nombre, "w") as archivo:
        archivo.write(texto)
        
# Función para leer el archivo.
def leer(nombre):
    texto =""
    with open(nombre, "r") as archivo:
        texto = archivo.read()
    return texto

"""
Probar funciones
Nota: si no agregamos esto, a la hora de importar, se ejecutará
"""
if __name__ == "__main__":
    escribir("prueba.txt", "Un texto cualquiera")
    print(leer("prueba.txt"))