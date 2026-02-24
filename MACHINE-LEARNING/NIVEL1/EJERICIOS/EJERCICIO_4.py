# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 20:15:52 2025

@author: PC

Description:
    Crea un mini sistema de tareas que permita:
        *Agregar tareas
        *Listar tareas
        *Marcar una tarea como completada
        *Eliminar tareas
        
    Usa un diccionario para guardar las tareas (id: {"tarea": "...", "completada": False})
"""

# Diccionario de tareas
tareas = {}
ID = 0

def printMenu():
    print("\n== SISTEMA ADMINISTRADOR DE TAREAS ==")
    print(" 1) Agregar tarea")
    print(" 2) Listar tareas")
    print(" 3) Marcar una tarea como completada")
    print(" 4) Eliminar tarea")
    print(" 5) Salir")
    
    try:
        return int(input("\n > "))
    except ValueError:
        print("⚠️ Entrada inválida. Ingresa un número.")
        return 0

def addTask():
    # Tenemos que usar Global para poder acceder a ID
    global ID
    tarea = {}
    nombre = input("\n📝 Nombre de la tarea: ")
    
    try:
        completada = bool(int(input("¿Está completada? (1 = Sí, 0 = No): ")))
    except ValueError:
        print("⚠️ Entrada inválida. Se asumirá que la tarea no está completada.")
        completada = False
    
    tarea["tarea"] = nombre
    tarea["completada"] = completada
    
    # Tareas no necesita que sea global
    tareas[ID] = tarea
    print(f"✅ Tarea agregada con ID {ID}")
    ID += 1

def showTask():
    print("\n📋 Lista de tareas:")
    
    # Validamos si esta vacía
    if not tareas:
        print("No hay tareas registradas.")
        return

    # Imprimimos estos datos que comforman el diccionario de diccionarios
    for id, datos in tareas.items():
        
        # Esta sintaxis no la conocia
        status = "✅ Completada" if datos["completada"] else "❌ Pendiente"
        print(f"ID {id}: {datos['tarea']} → {status}")

def checkTask():
    
    # Validamos la entrada de datos
    try:
        checkId = int(input("\n🔍 ID de la tarea a marcar como completada: "))
    except ValueError:
        print("⚠️ ID inválido.")
        return
    
    # Revisamos que la tarea este en el diccionario
    if checkId in tareas:
        if not tareas[checkId]["completada"]:
            tareas[checkId]["completada"] = True
            print("✔️ Tarea marcada como completada.")
        else:
            print("ℹ️ Esta tarea ya está completada.")
    else:
        print("❌ ID no encontrado.")

def deleteTask():
    try:
        checkId = int(input("\n🗑️ ID de la tarea a eliminar: "))
    except ValueError:
        print("⚠️ ID inválido.")
        return
    
    if checkId in tareas:
        tareas.pop(checkId)
        print("🧹 Tarea eliminada correctamente.")
    else:
        print("❌ ID no encontrado.")

# Bucle principal
run = True
while run:
    op = printMenu()
    
    if op == 1:
        addTask()
    elif op == 2:
        showTask()
    elif op == 3:
        checkTask()
    elif op == 4:
        deleteTask()
    elif op == 5:
        print("👋 Saliendo del sistema. ¡Hasta luego!")
        run = False
    else:
        print("⚠️ Opción inválida. Intenta de nuevo.")

    
    
