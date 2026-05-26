# MENU NOTAS

notas = []

def merror1():
    print("Ingrese solo numeros porfavor")

def menu():
    print("1. Agregar notas. ")
    print("2. Mostrar notas. ")
    print("3. Calcular promedio. ")
    print("4. Salir")

def ingreso_notas():
    while True:
        try:
            nota = float(input("Ingrese una nota a agregar: "))
            break
        except ValueError:
            merror1()
    
    if (nota > 7.0 or nota < 0):
        print("Ingrese un valor correcto! ")
    else:
        notas.append(nota)
        
def muestra_nota():
    print("Mostrando lista de notas: ")
    for listado in notas:
        print(listado)

def calculo_prom():
    acum = 0
    cont = 0

    for nota in notas:
        acum = acum + nota
        cont = cont + 1

    if cont > 0:
        promedio = acum / cont
        print(f"el promedio es: {promedio}")
    else:
        print("no hay notas ingresadas. ")

def salida():
    print("Saliendo \n Gracias por usar!")
    exit()

opciones = {

    1: ingreso_notas,
    2: muestra_nota,
    3: calculo_prom,
    4: salida
}

while True:
    menu()

    while True:
        try:
            op = int(input("Ingresa una opción: "))
            break
        except ValueError:
            merror1()
    
    if op in opciones:
        opciones[op]()
    else:
        print("opción no valida! ")
    

