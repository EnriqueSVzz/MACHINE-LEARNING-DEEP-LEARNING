# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 19:10:51 2025

@author: PC
"""
# Clase Padre
class Producto:
    
    # Constructor
    def __init__(self, id, description, costo):
        self.id = id
        self.description = description
        self.costo = costo
        
    # Función para imprimir datos
    def crear_etiqueta(self):
        return " %s \n %s \n %0.2f \n" % (
            self.id,
            self.description,
            self.costo)

if __name__ == "__main__":
    p = Producto("pro", "Producto", 100.10)
    print(p.crear_etiqueta())