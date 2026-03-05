# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 20:24:24 2025

@author: PC
"""

from random import randint

class TragaMonedas:
    
    #definimos nuestro construsctor
    def __init__(self, id, premio):
        self.id = id
        self.premio = premio
        self.monedas = 0
        self.jackpots = 0
    
    # Sobrecarga de operadores
    def __str__(self):
        return "ID: " + str(self.id) + "s, Premio" + str(self.premio)
    
    # sobrecargar el operador de igual
    def __eq__(self, otro):
        return self.monedas = otro.monedas
    
    # sobrecargar operador menor que
    def __lt__(self, otro):
        return self.monedas < otro.monedas
    
    def __gt__(self, otro):
        return self.monedas > otro.monedas
    
    # Definimos el método jugar
    def jugar(self):
        self.monedas += 1
        # simulamos los 3 numeros de la maquina.
        numeros = randint(0, 9), randint(0, 9), randint(0, 9)
        mensaje = ""
        if numeros[0] == numeros[1] == numeros[2]:
            self.jackpots += 1
            mensaje = "Felicidades !!! Ganaste %0.2f" % self.premio
        else:
            mensaje = "Mejor suerte para la proxima"
        
        # regresamos una tupla
        return numeros, mensaje