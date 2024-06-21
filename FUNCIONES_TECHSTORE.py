import os
import msvcrt
import csv
inventario=[]

def inicio():
    print("<<PRESS ANY KEY>>")
    msvcrt.getch()
    os.system("cls")

def limpiar():
    os.system("cls")

def printR(texto):
    print(f"\033[31m{texto}\033[0m")

def printV(texto):
    print(f"\033[32m{texto}\033[0m")

def printAm(texto):
    print(f"\033[33m{texto}\033[0m")

def printAz(texto):
    print(f"\033[34m{texto}\033[0m")

def printM(texto):
    print(f"\033[35m{texto}\033[0m")

def menu():
    printM("═════════════════════════════════════════")
    printM("       SISTEMA DE VENTAS TECHSTORE       ")
    printM("═════════════════════════════════════════")
    print("1) AGREGAR NUEVO PRODUCTO AL INVENTARIO")
    print("2) MOSTRAR EL INVENTARIO")
    print("3) VENDER PRODUCTO")
    print("4) GUARDAR INVENTARIO EN CSV")
    print("5) CARGAR INVENTARIO DESDE CSV")
    print("0) SALIR")
    printM("═════════════════════════════════════════")

def validar_producto(nombre):
    for i in range(len(inventario)):
        if nombre==inventario[i][0]:
            return i
    return -1

def agregar_producto(nombre,precio,stock):
    if validar_producto(nombre)==-1:
        if precio>0:
            if stock>=0:
                inventario.append([nombre,precio,stock])
                printV("EL PRODUCTO SE HA AGREGADO CON EXITO")
            else:
                printR("EL STOCK DEL PRODUCTO DEBE SER MAYOR O IGUAL A 0")
        else:
            printR("EL PRECIO DEBE SER MAYOR A 0")
    else:
        printR("EL PRODUCTO YA SE ENCUENTRA REGISTRADO")

def mostrar_inventario():
    if len(inventario)>0:
        for i in range(len(inventario)):
            printAm(f"{i+1})\nNOMBRE: {inventario[i][0]}\nPRECIO: ${inventario[i][1]}\nSTOCK: {inventario[i][2]}")
            printAm("═════════════════")
    else:
        printR("ACTUALMENTE NO HAY PRODUCTOS REGISTRADOS")

def vender_producto(nombre,cantidad):
    if len(inventario)>0:
        centinela=False
        for i in range(len(inventario)):
            if nombre==inventario[i][0]:
                if cantidad<=inventario[i][2]:
                    total=0
                    precio=inventario[i][1]
                    total=cantidad*precio
                    printV(f"COMPRA REALIZADA CON ÉXITO. TOTAL A PAGAR POR {cantidad} PRODUCTOS: ${total}")
                    inventario[i][2]-=cantidad
                else:
                    printR("CANTIDAD NO DISPONIBLE")
                centinela=True
        if not centinela:
            printR("EL PRODUCTO NO SE ENCUENTRA REGISTRADO")
    else:
        printR("ACTUALMENTE NO HAY PRODUCTOS REGISTRADOS")

def generar_csv(nombre):
    if len(inventario)>0:
        with open(f'{nombre}.csv','w',newline='',encoding='utf-8') as a:
            escribir=csv.writer(a,delimiter=',')
            inventario.insert(0,["NOMBRE","PRECIO","STOCK"])
            escribir.writerows(inventario)
            inventario.pop(0)
            printV(f"EL REPORTE CON NOMBRE {nombre}.csv HA SIDO GENERADO CON EXITO")
    else:
        printR("NO HAY PRODUCTOS REGISTRADOS")

def cargar_csv(ruta):
    with open(f'{ruta}.csv','r',newline='',encoding='utf-8') as f:
        escribir=csv.reader(f,delimiter=",")
        for i in escribir:
            inventario.append(i)
        printV("INVENTARIO CARGADO CON EXITO")
