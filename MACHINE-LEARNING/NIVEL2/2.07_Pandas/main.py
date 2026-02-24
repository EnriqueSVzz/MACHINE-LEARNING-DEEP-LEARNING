# -*- coding: utf-8 -*-
"""
Created on Sat May  3 16:47:11 2025

@author: PC

Notas:
    * Una Serie en pandas es una estructura de datos unidimensional 
    similar a un array de NumPy o a una lista de Python, pero con 
    etiquetas (índices) para cada elemento. 
    
    * Es uno de los tipos de datos fundamentales en pandas, junto 
    con el DataFrame.
    
    * Características principales de una Serie:
        - Unidimensional: contiene una sola columna de datos.
        - Indexada: cada valor tiene una etiqueta asociada (índice), 
            que puede ser numérico, texto u otro tipo.
        - Tipo de datos homogéneo: todos los elementos de 
            la serie suelen ser del mismo tipo (int, float, str, etc.).
    
    * Es como si fuera un super diccionario, una llave y un valors 

"""

# Lo más famosos de pandas, son sus series y dataframes
import pandas as pd

# Nuestros datos principales
indice = ["Juan", "Maria", "Francisco", "Pedro", "Luis"]
datos_listas = [40,20,36,34,20]

# Pasamos todo a un dataframe
edades = pd.Series(datos_listas, indice)

# Aquí se asume ue el tipo de datos es int64 bitss
print(edades)

# Estos datas frames, también pueden ser apartir de diccionarios
# el pandas ya lo transforma directo
datos = {"Rigo":1, "Gordo":2, "BebeBubi":3}
edades = pd.Series(datos)
print("\n",edades)


# Tipo de datos de pandas, más bien el contenido
print("\nTipo Pandas:", edades.dtype)
print("\nTamaño Pandas:", edades.size)

# Esto imprime la primera columna
print("\nIndex Pandas:", edades.index)

# Segunda columna
print("\nValores Pandas:", edades.values)


#Iteramos la serie, esto solo imprimió los values, no index
for elemento in edades:
    print(elemento)
    
# Ahora iteramos para los indices
for elemento in edades.index:
    print(elemento)
    
#Accedemos a los datos de esta serie
# inclusive si le pasamos una lista
print(edades[["Rigo", "Gordo"]]) 
print(edades[0:3])
#print(edades[[0,2]])   # error   

edades = pd.Series(datos_listas, indice)

"""
Métodos
"""

# con este podemos establecer los tipos de datos, ya que podamos
# tener muchisima información y ocupamos menos espacio
print("\n", edades.astype("i2"))

# Este cuenta las frecuencias de cada valor en la serie
print("\n", edades.value_counts())

# inclusive podríamos ordenar por values, pero no modifica
print("\n", edades.sort_values())

# si quisieramos que los meodifique tendría que ser algo así.
# es decir activar que la nueva salida tome el lugar
edades.sort_values(inplace=True)
print("\n", edades)

"""
Operaciones Vectoriales aritmeticas
"""
edades = pd.Series(datos_listas, indice)
edades = edades + 1
print("\n", edades)


print("\nMax:", edades.max(), " Posición:", edades.argmax())
print("\nMin:", edades.min(), " Posición:", edades.argmin())
print("\nSuma todo:", edades.sum())

print("\nModa:", edades.mode(), " Mean:", edades.mean())
print("\nMediana:", edades.median(), " Desviasión Estandar:", edades.std())
print("\nCuenta todo:", edades.count())

# ya hay algo que nos da todo esto
print("\nResumen:", edades.describe())

# calcular los cuantiles
print("\nCuantil 50%:", edades.quantile(0.5))    

# graficar
edades.plot()



