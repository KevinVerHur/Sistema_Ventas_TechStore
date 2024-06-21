from FUNCIONES_TECHSTORE import inicio,limpiar,printR,printV,printAz,menu,mostrar_inventario,agregar_producto,vender_producto,generar_csv,cargar_csv
inicio()
while True:
    menu()
    opcion=input("SELECCIONE: ")
    if opcion=="0":
        break
    elif opcion=="1":
        limpiar()
        printAz("AGREGAR NUEVO PRODUCTO AL INVENTARIO")
        nombre=input("INGRESE NOMBRE DEL PRODUCTO: ").upper()
        precio=int(input("INGRESE PRECIO DEL PRODUCTO: $"))
        stock=int(input("INGRESE STOCK DEL PRODUCTO: "))
        agregar_producto(nombre,precio,stock)
    elif opcion=="2":
        limpiar()
        printAz("MOSTRAR EL INVENTARIO")
        mostrar_inventario()
    elif opcion=="3":
        limpiar()
        printAz("VENDER PRODUCTO")
        mostrar_inventario()
        nombre=input("INGRESE NOMBRE DEL PRODUCTO QUE DESEA COMPRAR: ").upper()
        catidad=int(input("INGRESE CANTIDAD QUE DESEA COMPRAR: "))
        vender_producto(nombre,catidad)
    elif opcion=="4":
        limpiar()
        printAz("GUARDAR INVENTARIO EN CSV")
        nombre=input("INGRESE NOMBRE DEL REPORTE (ASEGURESE DE NO USAR ESPACIOS): ").upper()
        generar_csv(nombre)
    elif opcion=="5":
        limpiar()
        printAz("CARGAR INVENTARIO DESDE CSV")
        nombre=input("INGRESE NOMBRE DEL ARCHIVO QUE DESEA CARGAR: ").lower()
        cargar_csv(nombre)