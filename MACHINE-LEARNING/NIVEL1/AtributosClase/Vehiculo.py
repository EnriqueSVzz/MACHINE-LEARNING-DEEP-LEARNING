# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 18:35:46 2025

@author: PC
"""

"""
Clase del Tutorial
"""
class Vehiculo:
    
    # Definimos nuestra variable que llevara el conteo
    folio = 0
    COLORES = ("BLANCO", "ROJO", "VERDE")
    
    #Construstor
    def __init__(self, color):
        #Mandamos a llamar a nuestra variable estática
        Vehiculo.folio += 1
        self.serie = Vehiculo.folio
        self.set_color(color)
    
    # Sobrecargamos el método string
    def __str__(self):
        return str(self.serie) + " " + self.color
    
    #método set
    def set_color(self, color):
        # transformamos todo a mayus 
        # y borramos los espacios de los lados
        color = color.upper().strip()
        
        # verificamos que sea  un color válido
        if color in Vehiculo.COLORES:
            self.color = color
        else:
            # asignamos un valor válido
            self.color = Vehiculo.COLORES[0] 

"""
Mi Clase //pendiente
"""
class Carro:
    
    # Definimos nuestra variable que llevara el conteo
    folio = 0
    COLORES = ("BLANCO", "ROJO", "VERDE")
    
    
    #Construstor
    def __init__(self, color):
        #Mandamos a llamar a nuestra variable estática
        Vehiculo.folio += 1
        self.serie = Vehiculo.folio
        self.set_color(color)
    
    # Sobrecargamos el método string
    def __str__(self):
        return str(self.serie) + " " + self.color
    
    #método set
    def set_color(self, color):
        # transformamos todo a mayus 
        # y borramos los espacios de los lados
        color = color.upper().strip()
        
        # verificamos que sea  un color válido
        if color in Vehiculo.COLORES:
            self.color = color
        else:
            # asignamos un valor válido
            self.color = Vehiculo.COLORES[0] 






