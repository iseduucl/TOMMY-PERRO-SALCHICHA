# PRODUCTOS SUPER MERCADO

productos = []

def ingresos():
    name = input("Nombre del producto: ")
    price = int(input("Precio del producto: "))
    cantidad = int(input("Cantidad: "))
    total = price * cantidad

    ingreso  = {
        "nombre":name,
        "precio":price,
        "cantidad":cantidad,
        "total":total
    }

    productos.append(ingreso)

ingresos()

for ingreso in productos:
    print("nombre: ",ingreso["nombre"])
    print("precio: ",ingreso["precio"])
    print("cantidad: ",ingreso["cantidad"])
    print("total: ",ingreso["total"])