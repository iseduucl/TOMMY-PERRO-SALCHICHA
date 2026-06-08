# NOISE MARINES ISMAEL GUARDIA

vinilos = {}

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
    print("3.- Buscar vinilo ")
    print("4.- Actualizar stock ")

def registro_vinilo():
    espacios()
    print(" REGISTRO DE VINILO ")

    while True:
        try:
            codigo_vin = int(input("Ingrese código de vinilo: "))
            
            if codigo_vin in vinilos:
                print("Codigo ya registrado! ")
                return
            else:
                print("Registrando codigo")
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
        "artista":ingreso_art,
        "album":ingreso_alb,
        "genero":ingreso_gen,
        "precio":precio_vin,
        "stock":stock_vin
    }

    vinilos[codigo_vin] = vinilo
    print("Vinilo registrado correctamente... ")

def ver_vinilo():
    espacios()
    print("     VER VINILOS     ")
    if vinilos == {}:
        print("No hay vinilos registrados! ")
    
    for codigo, vinilo in vinilos.items():
        espacios()
        print("Codigo: ",codigo)
        print("Artista: ",vinilo["artista"])
        print("Álbum: ",vinilo["album"])
        print("Género: ",vinilo["genero"])
        print("Precio: $",vinilo["precio"])
        print("Stock: ",vinilo["stock"])

def buscar_vinilo():
    espacios()

    while True:
        try:
            busqueda = int(input("Ingresa el codigo del vinilo que buscas para ver su información: "))

            if busqueda <= 0:
                print("Ingresar un codigo mayor a 0! ")

            if busqueda in vinilos:
                vinilo = vinilos[busqueda]
                espacios()
                print("Codigo: ",busqueda)
                print("Artista: ",vinilo["artista"])
                print("Álbum: ",vinilo["album"])
                print("Género: ",vinilo["genero"])
                print("Precio: $",vinilo["precio"])
                print("Stock: ",vinilo["stock"])
            else:
                print("Vinilo no encontrado! ")

            break
        except ValueError:  
            print("Solo ingresar numeros porfavor! ")

def actualizar_stock():
    print("---- ACTUALIZACIÓN DE STOCK ----")
    
    if vinilos == {}:
        print("No hay vinilos registrados...")
        return

    while True:
        try:
            busqueda2 = int(input("Ingresa el código del vinilo que deseas actualizar: "))
            if busqueda2 <= 0:
                print("Ingrese un codigo mayor a 0 porfavor!")
            else:
                break
        except:
            errornum()

    if busqueda2 in vinilos:
        vinilo = vinilos[busqueda2]
        espacios()
        print("Codigo: ",busqueda2)
        print("Artista: ",vinilo["artista"])
        print("Álbum: ",vinilo["album"])
        print("Género: ",vinilo["genero"])
        print("Precio: $",vinilo["precio"])
        print("Stock: ",vinilo["stock"])
        
        espacios()
        
        print(f"Stock disponible: {vinilo["stock"]}")
        while True:
            try:
                opcion = int(input("\n 1.- Agregar stock  \n 2.- Quitar stock \nIngrese opción: "))
                if opcion < 1 or opcion > 2:
                    print("Ingrese una opción valida! ")
                else:
                    break
            except ValueError:
                errornum()

        if opcion == 1:
            while True:
                try:
                    suma = int(input("Ingrese la cantidad a agregar: "))
                    if suma < 0:
                        print("Ingrese un número mayor o igual a 0... ")
                    else:
                        break
                except ValueError:
                    errornum()

            vinilo["stock"] = (vinilo["stock"] + suma)
            
            vinilos[busqueda2] = vinilo

            print(f"Nuevo stock: {vinilo["stock"]}")
        
        if opcion == 2:
            while True:
                try:
                    resta = int(input("Ingrese la cantidad a quitar: "))
                    if resta < 0:
                        print("Ingrese un número mayor o igual a 0... ")
                    elif resta > vinilo["stock"]:
                        print("El stock no puede quedar en negativo! ")
                        return
                    else:
                        break
                except ValueError:
                    errornum()

                

            vinilo["stock"] = (vinilo["stock"] - resta)
            
            vinilos[busqueda2] = vinilo

            print(f"Nuevo stock: {vinilo["stock"]}")
            
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
        3:"Buscar vinilo",
        4:"Actualizar stock"
    }

    if op not in opciones:
        print("Selecciona una opción correcta! ")
    elif op == 1:
        registro_vinilo()
    elif op == 2:
        ver_vinilo()
    elif op == 3:
        print("---- BUSQUEDA DE VINILOS ----")
        buscar_vinilo()
    elif op == 4:
        actualizar_stock()
    elif op == 5:
        escape()

