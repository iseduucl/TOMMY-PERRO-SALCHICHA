# NOISE MARINES ISMAEL GUARDIA

vinilos = [] 

def espacios():
    print("="*35)

def errorvacio():
    print("Porfavor rellenar el nombre ")

def errornum():
    print("Ingrese solo numeros porfavor! ")

def menu():
    print("-"*35)
    print("        NOISE MARINES STORE       ")
    print("-"*35)
    print("1.- Registrar vinilos ")
    print("2.- Ver vinilos ")
    print("3.- Salir ")

def registro_vinilo():
    espacios()
    print(" REGISTRO DE VINILO ")

    while True:
        try:
            codigo_vin = int(input("Ingrese código de vinilo: "))
            break
        except ValueError:
            errornum()

    while True:
        ingreso_art = input("Ingrese artista: ").strip()

        if ingreso_art:
            print(f"Artista {ingreso_art} ingresado correctamente... ")
            break
        else:
            errorvacio()
    
    while True:
        ingreso_alb = input("Ingrese álbum: ").strip()
        
        if ingreso_alb:
            print(f"Álbum {ingreso_alb} ingresado correctamente... ")
            break
        else:
            errorvacio()
    
    while True:
        ingreso_gen = input("Ingrese género : ").strip()
        
        if ingreso_gen:
            print(f"Género {ingreso_gen} ingresado correctamente... ")
            break
        else:
            errorvacio()

    while True:
        try:
            precio_vin = int(input("Ingrese precio de vinilo: "))
            break
        except ValueError:
            errornum()
    
    while True:
        try:
            stock_vin = int(input("Ingrese stock de vinilo: "))
            break
        except ValueError:
            errornum()

    vinilo = {
        "codigo":codigo_vin,
        "artista":ingreso_art,
        "album":ingreso_alb,
        "genero":ingreso_gen,
        "precio":precio_vin,
        "stock":stock_vin
    }

    vinilos.append(vinilo)
    print("Vinilo registrado correctamente... ")

def ver_vinilo():
    espacios()
    print("     VER VINILOS     ")
    if vinilos == []:
        print("No hay vinilos registrados! ")
    
    for vinilo in vinilos:
        espacios()
        print("Codigo: ",vinilo["codigo"])
        print("Artista: ",vinilo["artista"])
        print("Álbum: ",vinilo["album"])
        print("Género: ",vinilo["genero"])
        print("Precio: $",vinilo["precio"])
        print("Stock: ",vinilo["stock"])

def escape():
    espacios()
    print("Gracias por usar! ")
    exit()


while True:
    menu()

    while True:
        try:
            op = int(input("Ingresa una opción: "))
            break
        except ValueError:
            errornum()
    
    opciones = {

        1:"Registrar vinilo",
        2:"Ver vinilos",
        3:"Salir"
    }

    if op not in opciones:
        print("Selecciona una opción correcta! ")
    elif op == 1:
        registro_vinilo()
    elif op == 2:
        ver_vinilo()
    elif op == 3:
        escape()


        



