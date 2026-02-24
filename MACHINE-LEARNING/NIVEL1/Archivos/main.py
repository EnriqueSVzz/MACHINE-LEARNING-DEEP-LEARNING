# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 19:25:27 2025

@author: PC
"""

#Función para leer y escribir en python.
# Sin el encoding, no imprime acentos ni otros caracteres especioales
archivo = open("datos.txt", encoding="utf-8")
texto = archivo.read()
print(texto)
archivo.close()

#Establecer donde debe leer el archivo
archivo = open("datos.txt", encoding="utf-8")
#--> Le decimos al punto que se mueva hasta la 5 pos
texto = archivo.read(5)
print("\n Primeros 5 posiciones:", texto)
texto = archivo.read(5)
print("\n Posiciones [6,10]:", texto)
archivo.close()

#Imprimir directamente una linea
archivo = open("datos.txt", encoding="utf-8")
texto = archivo.readline()
print("\n Linea leída 1:", texto)
texto = archivo.readline()
print("\n Linea leída 2:", texto)
texto = archivo.readline()
print("\n Linea leída 3:", texto)
texto = archivo.readline()
# Si no existe linea imprimirá vacio.
print("\n Linea leída 4:", texto)
archivo.close()


# Leer un archivo y guardarlo en una lista
archivo = open("datos.txt", encoding="utf-8")
# Nos regresa todo en listas separados pos un \n
texto = archivo.readlines()
#exto = texto.strip()
print("\n Lista", texto)
archivo.close()

# Abrir lo archivos como estructuras
# No es necesario poner la R, ya que ya la tiene por defecto
with open("datos.txt", "r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    print("\n Estructura", lineas)

#Escribir un archivo
# Con la pura 'w' crea y limpia el archivo cada vez que lo abre.
# Con la 'a', podemos seguir editando(append)
with open("personas.txt", "w", encoding="utf-8") as archivo:
    # Debemos agregar el salto de linea explicitamente
    archivo.write("Kiki López 20\n")
    archivo.write("Lola García 22\n")
    
"""
Procesar un archivo CSV
""" 
#Definimos nuestro diccionario
parajeros = {} 
with open("datos_metro.csv", "r", encoding="utf-8") as archivo:
    archivo.readline() #Saltamos nuestra primera linea
    estaciones = archivo.readlines() # Nos traemos toda la info
    for estacion in estaciones:
        #Limpiamos y separamos por ,
        lista = estacion.strip().split(",")
        #Creamos la llave y asignamos una lista del segundo elemento en adelante
        # De paso usamos la conversión a map
        parajeros[lista[0]] = list(map(int,lista[1:]))
    


print("\n Datos", parajeros) 
print("\n Total Zocalo: ", sum(parajeros["Zócalo"])) 
print("\n Total Bellas Artes: ", sum(parajeros["Bellas Artes"])) 
print("\n Total Juárez: ", sum(parajeros["Juárez"])) 
print("\n Total Hidalgo: ", sum(parajeros["Hidalgo"])) 

