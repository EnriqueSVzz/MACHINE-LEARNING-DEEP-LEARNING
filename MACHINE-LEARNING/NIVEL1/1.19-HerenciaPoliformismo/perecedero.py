# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 19:17:54 2025

@author: PC
"""

from producto import Producto

# Es una clase hija
class Perecedero(Producto):
    
    #definimos el constructor
    def __init__(self, id, description, costo, fecha_cad):
        #Hacemos que el apuntador apunte al init del padre
        super().__init__(id, description, costo)
        self.fecha_cad = fecha_cad
    
    # Sobreimprimos el método para imprimir
    def crear_etiqueta(self):
        return super().crear_etiqueta() + "%s \n" % self.fecha_cad