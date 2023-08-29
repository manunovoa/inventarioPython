#MENU DE OPCIONES
#1. Ingresar producto bodega
#2. Verificar los productos en bodega
#3. Buscar un producto en la bodega
#4. Editar un producto en la bodega
#5. Retirar un producto
#6. Salir

#Producto: nombre, codigo, descripcion, foto, precio, cantidadEnBodega, fechaEntradaBodega

opcion=0
print("\n******** TIENDA EL GANGAZO ********")
print("***********************************")
print("1. Ingresar producto bodega")
print("2. Verificar los productos en bodega")
print("3. Buscar un producto en la bodega")
print("4. Editar un producto en la bodega")
print("5. Retirar un producto")
print("6. Salir")

productos = []
while (opcion != 6):
    producto={}
    opcion=int(input("Digita la opción deseada: "))
    if opcion == 1:
        print("\n****Ingresa nuevo producto****")
        producto["nombre"] = input("Ingresa nombre de producto: ")
        producto["codigo"] = int(input("Ingresa codigo del producto: "))
        producto["descripcion"] = input("Ingresa descripcion del producto: ")
        producto["foto"] = input("Ingresa la url de la foto del producto: ")
        producto["precio"] = float(input("Ingresa el precio del producto: "))
        producto["cantidadEnBodega"] = int(input("Ingresa la cantidad del producto: "))
        producto["fechaEntradaBodega"] = input("Ingresa la fecha de entrada del producto: ")
        productos.append(producto)
    elif opcion==2:
        print("\n****Mostrando inventario****")
        for productoSeleccinado in productos:
            print(f"Codigo = {productoSeleccinado['codigo']}")
            print(f"Nombre = {productoSeleccinado['nombre']}")
            print(f"Descripcion =  {productoSeleccinado['descripcion']}")
            print(f"Url de la foto = {productoSeleccinado['foto']}")
            print(f"Precio = $ {productoSeleccinado['precio']}")
            print(f"Cantidad de bodega = {productoSeleccinado['cantidadEnBodega']}")
            print(f"Fecha de entrada del producto = {productoSeleccinado['fechaEntradaBodega']}\n")         
    elif opcion==3:   
        pass
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    elif opcion == 6:
        print("Gracias, hasta pronto.")
    else:
        print("Opción inválida, vuelva a intentarlo")