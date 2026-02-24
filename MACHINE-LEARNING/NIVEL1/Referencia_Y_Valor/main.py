# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 15:29:48 2025

@author: PC
"""

"""
Los Tipos de Datos primitivos se asumen que serán pequeños, por
consiguiente, se pasarán por valor, mientra que las estructuras
se espera que tengan un tamaño mucho más grande, por lo que serán
enviado por referencia
"""

def doblar(referencia, valor):
    referencia *=2
    valor *=2
    print("\n Dentro de la Función: ", referencia, valor)
    
    
struct = ["a", "b", "c"]
primi = "abc"

print("\n Antes: ", struct, primi)
doblar(struct, primi)
print("\n Despues: ", struct, primi)