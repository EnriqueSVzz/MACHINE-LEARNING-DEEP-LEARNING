# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 19:22:13 2025

@author: PC

Description:
    1. Crea una clase CuentaBancaria con métodos para:
        * Depositar
        * Retirar
        * Mostrar saldo
        * Transferir a otra cuenta
    
    2. Crea varias cuentas y simula algunas operaciones entre ellas.

Ideas:
    1. Crear una clase "CuentaBancaria"
    2. Guardar la información en un archivo.
    3. La clase tiene que ser capaz de acceder y cargar el dinero y modificiarlo
    4. Validar que la cuenta exista y que si tenga fondos.
"""

class CuentaBancaria:
    
    info = "SQL.txt"
    
    #definimos nuestro constructor
    def __init__(self, folio, titular, saldo):
        self.__folio = folio    # atributo privado
        self.__titular = titular    # atributo privado
        self.__saldo = saldo        # atributo privado

   # Getter/Setter para el titular
    def get_folio(self):
        return self.__folio 
    def set_folio(self, newFolio):
        self.__folio =  newFolio

    # Getter/Setter para el titular
    def get_titular(self):
        return self.__titular
    def set_titular(self, newTitular):
        self.__titular =  newTitular

    # Getter/Setter para el saldo
    def get_saldo(self):
        return self.__saldo
    def set_saldo(self, newSaldo):
        self.__saldo =  newSaldo

    # Funciones de la clase
    def guardarInfo(self):
        log = self.__folio + "," + self.__titular + "," + str(self.__saldo) +"\n"
        with open(CuentaBancaria.info, 'a', encoding='utf-8') as archivo:
            archivo.write(log)

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("No se puede depositar cantidades 0 o menores valores")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes o cantidad inválida")
    
    # Imprimir mensaje
    def __str__(self):
        return "ID:" + self.__folio + " Titular:" + self.__titular + " Saldo:" + str(self.__saldo) 
    
    def transferir(self, cantidad, cuenta destino):
        if cantidad > 0:
            self.__saldo += cantidad
    


"""
MAIN
"""

# Supongamos que ya partimos que ahora tenemos que empezar a cargar la info
cuentas = []
with open("SQL.txt", "r", encoding="utf-8") as archivo:
    # Nos traemos toda la info
    lineas= archivo.readlines()
    
    # tenemos que recorrer toda la info
    for linea in lineas:
        #Limpiamos y separamos por ,
        lista = linea.strip().split(",")
        cTmp = CuentaBancaria(lista[0], lista[1], float(lista[2]))
        cuentas.append(cTmp)

# Aperturamos nuestras cuentas
c1 = CuentaBancaria("123454321", "Pedro Perez", 10000.00)
c2 = CuentaBancaria("987656789", "Martha Perez", 30000.00)

cuentas.append(c1)
cuentas.append(c2)

for cuenta in cuentas:
    print(cuenta)

# Empezamos a realizar operaciones
cuentas[0].depositar(500.00)
cuentas[0].depositar(-100.00)
cuentas[2].retirar(3000.00)
cuentas[2].retirar(40000.00)

print("\n Post Actualizaciones")
for cuenta in cuentas:
    print(cuenta) 




