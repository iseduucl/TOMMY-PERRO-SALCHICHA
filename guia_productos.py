# Guia producto ismael :p

productos = {}

def ingresa_prod(productos):
    while True:
        nom_prod = input("Nombre del producto: ").strip().title()

        if nom_prod == "":
            print("debe ingresar un nombre valido! ")
        elif nom_prod in productos:
            print("Este producto ya existe! ")
        else:
            break
    
    while True:
        try:
            stock_prod = int(input("Stock: "))
            if stock_prod < 0:
                print("El numero de stock no puede ser menor a 0! ")
            else:
                break
        except ValueError:
            print("Porfavor ingresar solo numeros enteros! ")

    while True:
        try:
            precio_prod = float(input("Precio: "))
            if precio_prod <= 0:
                print("El numero de stock debe ser mayor a 0! ")
            else:
                break
        except ValueError:
           print("Porfavor ingresar solo numeros enteros! ") 

    productos[nom_prod] = [stock_prod,precio_prod]

    print(productos)

def mostrar_prod(productos):
    if len(productos) == 0:
        print("No hay productos registrados! ")
        return
    
    for nombre, datos in productos.items():
        stock = datos[0]
        precio = datos[1]
        print(f"Prducto: {nombre} | Stock: {stock} | Precio: ${precio}")

def buscar_prod(productos):
    if len(productos) == 0:
        print("No hay productos registrados! ")
        return
    
    busqueda = input("Ingrese el nombre del producto que desea buscar: ").strip().title()

    if busqueda in productos:
        stock = productos[busqueda][0]
        precio = productos[busqueda][1]
        print(" EL PRODUCTO QUE BUSCABA: ")
        print(f"Nombre: {busqueda}")
        print(f"Stock: {stock}")
        print(f"Precio: {precio}")
    else:
        print("El producto no existe")

def producto_caro(productos):
    if len(productos) == 0:
        print("No hay productos registrados! ")
        return
    
    mayor_nombre = ""
    mayor_precio = 0

    for nombre, datos in productos.items():
        precio = datos[1]

        if precio > mayor_precio:
            mayor_precio = precio
            mayor_nombre = nombre

    stock = productos[mayor_nombre][0]

    print("Producto mas caro: ")
    print(f"Nombre: {mayor_nombre}")
    print(f"Stock: {stock}")
    print(f"Precio: ${mayor_precio}")

def menu():
    while True:
        print("--- Inventario ---")
        print("1.- Agregar producto")
        print("2.- Mostrar productos")
        print("3.- Buscar producto")
        print("4.- Producto más caro")
        print("5.- Salir")

        while True:
            try:
                op = int(input("Ingrese una opción: "))
                break
            except ValueError:
                print("Porfavor solo ingrese numeros! ")

        if op == 1:
            ingresa_prod(productos)
        elif op == 2:
            mostrar_prod(productos)
        elif op == 3:
            buscar_prod(productos)
        elif op == 4:
            producto_caro(productos)
        elif op == 5:
            print("Saliendo del programa! ")
            exit()
        else:
            print("La opción ingresada no es valida... ")


menu()