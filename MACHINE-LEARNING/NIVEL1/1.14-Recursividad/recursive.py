# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 18:01:59 2025

@author: PC
"""

"""
Función que imprime un  una serie de numeros
Desventaja: es muy lento ya que se manda a llamar así misma
"""

def printRecursive(minimo, maximo):
    if minimo <= maximo:
        minimo += 1;
        print("\n",minimo)
        printRecursive(minimo, maximo)

def printRecursiveToZero(maximo):
    if maximo > 0:
        print("\n",maximo)
        maximo -= 1;
        printRecursiveToZero(maximo)
    else:
        print("\n",maximo)

def recursiva(n):
    if n== 0:
        print(n)
    else:
        print(n)
        recursiva(n-1)

def factorial_iterativo(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n+1):
        resultado *= i
    return resultado

def factorial_r(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_r(n-1)
    


        

if __name__ == "__main__":
    printRecursive(0, 10)
    printRecursiveToZero(5)
    recursiva(3)
    print("Factorial: ",factorial_iterativo(5))
    print("Facto R: ",factorial_r(4))