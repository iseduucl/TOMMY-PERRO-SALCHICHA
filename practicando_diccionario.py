
clientes = []
programa_activo = True

def guiones():
    print("-"*20)

def menu():
    guiones()
    print("Bienvenido al registro de clientes de Clean Day!")
    print("Elige una opción a realizar")
    print("1.- Registrar Clientre. ")
    print("2.- Mostrar Clientes. ")
    print("3.- Salir")


def errotext():
    guiones()
    print("Solo debe ingresar texto! ")

def erronum():
    guiones()
    print("Solo debe ingresar numeros! ")

def contiene_numero(texto):
    tiene_numero = False

    for caracter in texto:
        if caracter.isdigit():
            tiene_numero = True

    return tiene_numero

# Generar agenda y clientes de clanday

def inscribir_cliente():

    while True:
        guiones()
        nombre = input("Ingresar nombre del cliente: ")
        
        if contiene_numero(nombre):
            errotext()
        else:
            break
    
    while True:
        guiones()
        ciudad = input("Ingresar ciudad del cliente: ")

        if contiene_numero(ciudad):
            errotext()
        else:
            break

    while True:  
        guiones()  
        try:
            edad = int(input("Ingresa la edad del cliente: "))
            break
        except ValueError:
            erronum()
    
    while True:
        guiones()
        mail = input("Ingresar mail del cliente: ")

        if not (".com" or ".cl" or ".es" or "@") in mail:
            guiones()
            print("Ingrese un mail correcto! ")
        else:
            break
    
    while True:
        guiones()
        try:
            num_atenciones = int(input("Ingresa la cantidad de veces que a agendado: "))
            break
        except ValueError:
            erronum()

    if num_atenciones == 0:
        activo = False
    else:
        activo = True

    nuevo_cliente = {

        "nombre":nombre,
        "ciudad":ciudad,
        "edad":edad,
        "atenciones":num_atenciones,
        "mail":mail,
        "activo":activo
    }
    
    clientes.append(nuevo_cliente)
    print("Cliente inscrito correctamente")

def ver_cliente():

    if clientes == []:
            guiones()
            print("No hay clientes registrados")

    for cliente in clientes:
        guiones()
        print("Nombre: ",cliente["nombre"])
        print("Ciudad: ",cliente["ciudad"])
        print("Edad: ",cliente["edad"])
        print("Mail: ",cliente["mail"])
        print("Atenciones: ",cliente["atenciones"])

        if cliente["activo"] == False:
            print("Cliente sin actividad. ")
        else:
            print("Cliente activo. ")

        

def escape():
    guiones()
    print("Gracias por usar! ")
    

while programa_activo == True:
    menu()

    opciones = {

        1:"Incribir Cliente",
        2:"Ver Cliente",
        3:"Salir"
    }

    while True:
        try:
            op = int(input(":"))
            break
        except ValueError:
            erronum()

    if op not in opciones:
        print("La opción ingresada no es valida. ")
    elif op == 1:
        inscribir_cliente()
    elif op == 2:
        ver_cliente()
    elif op == 3:
        escape()
        programa_activo = False
    