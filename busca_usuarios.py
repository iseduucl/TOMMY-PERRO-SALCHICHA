# buscando usuarios ismael

usuarios = {}

def espacios():
    print("-"*35)

def error_numero(nombre):
    tiene_num = False

    for caracter in nombre:
        if caracter.isdigit():
            tiene_num = True
    return(tiene_num)

def error_letra(texto):
    tiene_letra = False

    for caracter in texto:
        if (caracter >= "a" and caracter <= "z") or (caracter >= "A" and caracter >= "Z"):
            tiene_letra = True
    return(tiene_letra)

def ingr_user(usuarios):
    while True:
        espacios()
        nombre = input("Ingrese nombre del usuario: ").strip()

        if nombre == "":
            print("El campo nombre no puede quedar vacio... ")
        else:
            print("Nombre de usuario ingresado con exito! ")
            break

    while True:
        espacios()
        sexo = input("Ingrese sexo del usuario ('M': Masculino o 'F': Femenino): ").upper().strip()

        if sexo != "M" and sexo != "F":
            print("Solo debe ingresar 'M' o 'F'...")
        elif sexo == "":
            print("El campo sexo no puede quedar vacio... ")
        else:
            break
    
    while True:
        espacios()
        contra = input("Ingrese una contraseña alfanumerica de al menos 8 caracteres: ")
        if contra == "":
            print("El campo contraseña no puede quedar vacio...")
        elif len(contra) < 8:
            print("Contraseña no puede tener menos de 8 caracteres")
        elif (error_numero(contra) == False or error_letra(contra) == False):
            print("La contraseña debe tener numeros y letras! ")     
        else:
            print("Contraseña ingresada correctamente! ")
            break


    
    usuarios[nombre] = [sexo,contra]
    espacios()
    print("Usuario registrado correctamente! ")

def buscar_user():

    while True:
        espacios()
        if usuarios == {}:
            print("No hay usuarios registrados... ")
            return
        
        busqueda = input("Ingrese nombre del usuario a buscar: ")

        if busqueda == '':
            print("No puede buscar un texto vacio! ")
        elif usuarios == {}:
            print("No hay usuarios registrados! ")

        
        if busqueda in usuarios:

            usuario = usuarios[busqueda]
            espacios()
            print("Usuario encontrado! ")
            print(f"Nombre: {busqueda}")
            print(f"Sexo: {usuario["sexo"]}")
            print(f"Contraseña: {usuario["contraseña"]}")
        else:
            print("Usuario no encontrado... ")

        break

def delete_user():
    
    while True:
        espacios()

        if usuarios == {}:
            print("No hay usuarios registrados... ")
            return

        busqueda = input("Ingrese nombre del usuario a buscar: ")

        if busqueda == '':
            print("No puede buscar un texto vacio! ")
        elif usuarios == {}:
            print("No hay usuarios registrados! ")

        if busqueda in usuarios:

            del usuarios[busqueda]
            print(f"Usuario {busqueda} eliminado con exito! ")
            break

        else:
            print("Usuario no encontrado... ")

        break

def escape():
    print("Saliendo..... ")
    exit()

while True:
    espacios()
    print("--- MENU DE USUARIO ---")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")
    
    opciones = {
        1:"ingresar",
        2:"buscar",
        3:"eliminar",
        4:"salir"
    }

    while True:
        try:
            op = int(input("Ingrese una opción: "))
            if op not in opciones:
                print("Ingresar una opcion valida! ")
            elif op == '':
                print("El campo no puede quedar vacio! ")
            else:
                break
        except ValueError:
            print("Solo ingresar numeros porfavor! ")

    if op == 1:
        ingr_user()
    if op == 2:
        buscar_user()
    if op == 3:
        delete_user()
    if  op == 4:
        escape