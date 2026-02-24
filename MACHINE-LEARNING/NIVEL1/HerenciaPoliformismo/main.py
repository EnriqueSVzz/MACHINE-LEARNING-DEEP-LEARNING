# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 19:10:39 2025

@author: PC
"""

from producto import Producto
from perecedero import Perecedero
from electronico import Electronico

pro = Producto("p", "Generico", 100)
per = Perecedero("p", "Jitomate", 200, "01/01/2022")
ele = Electronico("e", "Lavadora", 300, "Sony")

print(pro.crear_etiqueta())
print(per.crear_etiqueta())
print(ele.crear_etiqueta())