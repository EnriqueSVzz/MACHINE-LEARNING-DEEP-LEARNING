# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 18:38:42 2025

@author: PC
"""

"""
Parte una lista y se posiciona en la parte central de la lista
una recorre de izquierda al centro y del centro a la derecha

* tiene que estar ordenada
* tenemos que calcular la parte central
* centro = (bajo + alto)//2
*Si el valor es menor que el primero del rango de Alto, 
*nos vamos hacía bajo, caso contrario buscamos en Alto

* Tenemos que ir calculando de nuevo, acorralando más y 
* más hasta encontrar el valor

1) Establecemos bajo, centro y alto : Dato = 15
     - Este caso 14 es menor a 15, por lo que buscaremos en la derecha
[11         12      13      14      15      16      17]
bajo                        Centro                 Alto

2) Establecemos bajo, centro y alto : Dato = 15
    -Ahora nuestro bajo, será medio +1
    -ya que ya vimos que no es el mismo valor
    - centro = (15 + 17)/2 = 16
    - Como 16 es mayor a 15, nos vemos hacía la izquierda +1
    
[11         12      13      14      15      16      17]
                                    Bajo    Centro  Alto
3) Ya encontramos el valor
    
[11         12      13      14      15      16      17]
                                    Listo
"""

def busqueda_binaria(lista, dato):
    bajo = 0
    alto = len(lista)-1
    centro = (bajo + alto) // 2 # calculamos el centro
    
    while bajo <= alto:
        #Verificamos el centro
        if lista[centro] == dato:
            return centro
        # si el dato es mayor al centro nos movemos a la derecha
        elif lista[centro] < dato:
            bajo = centro + 1
        # Si no nos vemos a la izquierda
        else:
            # se ajusta para que alto ahora sea centro
            alto = centro -1
        centro = (bajo + alto) // 2
    return -1 #No existe el valor en la lista

def busqueda_recursiva(lista, bajo, alto, dato):
   #Detemos el ciclo
    if bajo > alto:
        return -1
    
    # Calculamos nuestro centro
    centro = (bajo + alto) // 2
    
    # Si el centro es igual  dato paramos
    if lista[centro] == dato:
        return centro
    
    # Si Dato mayor a Centro, entonces buscamos en la izquierda
    elif lista[centro] < dato:
        return busqueda_recursiva(lista, centro + 1, alto, dato)
    else:
        return busqueda_recursiva(lista, bajo, centro - 1, dato)
    


lista = [11, 12, 13, 14, 15, 16, 17]
for i in range(10,19):
    print(i, busqueda_binaria(lista, i))



