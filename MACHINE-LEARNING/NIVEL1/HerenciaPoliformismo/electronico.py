# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 16:01:38 2025

@author: PC
"""

from producto import Producto

class Electronico(Producto):
    
    def __init__(self, id, description, costo, marca):
        super().__init__(id, description, costo)
        self.marca = marca
    
    # Sobreimprimos el método para imprimir
    def crear_etiqueta(self):
        return super().crear_etiqueta() + "%s \n" % self.marca