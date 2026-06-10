usuarios = {}

def tiene_num(texto):
    numerico = False

    for caracter in texto:
        if caracter.isdigit():
            numerico = True
    
    return(numerico)
    
def tiene_letra(texto):
    letra = False

    for caracter in texto:
        if (caracter >= "a" and caracter <= "z" ) or (caracter >= "A" and caracter <= "Z" ):
            letra = True
    
    return(letra)



def ing_user(usuarios):
    while True:
        print("-"*35)
        nombre = input("Ingresa tu nombre de usuario: ").strip()

        if nombre == "":
            print("Porfavor no dejar el campo vacio...")
        else:
            break

    while True:
        print("-"*35)
        sexo = input("Ingresa tu sexo con 'M' o 'F': ").strip().upper()

        if sexo == "":
            print("Porfavor no dejar el campo vacio...")
        elif sexo != "M" and sexo != "F":
            print("Solo ingresar 'M' o 'F'...")
        else:
            break

    while True:
        print("-"*35)
        contra  = input("Ingresa una contraseña alfanumerica de al menos 8 caracteres: ").strip()

        if contra == "":
            print("Porfavor no dejar el campo vacio...")
        elif len(contra) < 8:
            print("La contraseña debe tener al menos 8 caracteres... ")
        elif tiene_num(contra) == False:
            print("La contraseña debe tener al menos un numero...")
        elif tiene_letra(contra) == False:
            print("La contraseña debe tener al menos una letra...")
        else:
            break

    usuarios[nombre] = [sexo,contra]
    print("-"*35)
    print("Usuario registrado con éxito! ")

def buscar_user(usuarios):
    while True:
        print("-"*35)
        if usuarios == {}:
            print("No hay usuarios registrados! ")
            return

        busqueda = input("Ingresa nombre del usuario a buscar: ").strip()

        if busqueda == "":
            print("Porfavor no dejar el campo vacio...")

        if busqueda in usuarios:
            usuario = usuarios[busqueda]
            print("-"*35)
            print(f"Sexo del usuario: {usuario[0]} y la contraseña es {usuario[1]}")
            break
        
        else:
            print("-"*35)
            print("usuario no encontrado...")

def delete_user(usuarios):

    while True:
        print("-"*35)
        if usuarios == {}:
            print("No hay usuarios registrados! ")
            return

        busqueda = input("Ingresa nombre del usuario a buscar: ").strip()

        if busqueda == "":
            print("Porfavor no dejar el campo vacio...")

        if busqueda in usuarios:
            del usuarios[busqueda]
            print("Usuario eliminado con exito! ")
            break
            
        
        else:
            print("-"*35)
            print("usuario no encontrado...")

while True:
    print(" ---    MENU DE USUARIO    --- ")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")
    
    print("-"*35)

    while True:
        try:
            op = int(input("Ingresa una opción: ").strip())
            break
        except ValueError:
            print("Solo ingresar números! ")

    if op == 1:
        ing_user(usuarios)
    elif op == 2:
        buscar_user(usuarios)
    elif op == 3:
        delete_user(usuarios)
    elif op == 4:
        print("-"*35)
        print("Saliendo del menu....")
        exit()