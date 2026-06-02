
alumnos = {}

def error_nombre(texto):
    tiene_numero = False

    for caracter in texto:
        if caracter.isdigit():
            tiene_numero = True
    return tiene_numero


def agregar_alumnos(alumnos):
    acum_notas = 0
    lista_notas = []
    print("-"*35)
    print("   AGREGAR ALUMNOS   ")
    while True:
        alumno = input("Ingrese nombre del alumno: ").strip().title()

        if error_nombre(alumno):
            print("Solo ingresar letras en el nombre! ")
        elif alumno == "":
            print("Ingresar contenido en el nombre porfavor! ")
        else:
            break

    while True:
        try:
            cantidad_notas = int(input("Ingrese la cantidad de notas a registrar: "))
            if cantidad_notas < 1:
                print("La cantidad de notas debe ser mayor a 0!")
            else:
                break
        except ValueError:
            print("Ingresar solo numeros porfavor! ")
    
    
    for i in range(cantidad_notas):
        while True:
            try:
                notas = float(input("Ingresa una nota: "))

                if notas < 1.0 or notas > 7.0:
                    print("Ingresar una nota valida porfavor! ")
                else:
                    acum_notas = acum_notas + notas
                    lista_notas.append(notas)
                    break
            except ValueError:
                print("Ingresar solo numeros porfavor!")

    promedio = acum_notas / cantidad_notas

    alumnos[alumno] = [cantidad_notas,lista_notas,promedio]

def mostrar_alumnos(alumnos):
    
    if len(alumnos) == 0:
        print("No hay alumnos registrados! ")
        return

    for nombre,datos in alumnos.items():
            
        notitas = datos[1]

        print(f"Alumno: {nombre} / Notas: {notitas}")

def mostrar_promedios(alumnos):

    if len(alumnos) == 0:
        print("No hay promedios para mostrar! ")
        return
    
    for nombre,datos in alumnos.items():

        promedio = datos[2]

        print(f"Nombre: {nombre} / Promedio: {promedio:.1f}")

def mejor_alumno(alumnos):
    if len(alumnos) == 0:
        print("No hay promedios para mostrar! ")
        return

    mj_prom = 0
    mj_alumno = ""
    
    for nombre,datos in alumnos.items():
        promedio = datos[2]

        if promedio > mj_prom:
            mj_prom = promedio
            mj_alumno = nombre
    
    notas = alumnos[mj_alumno][1]

    print("Mejor alumno! ")
    print(f"Nombre: {mj_alumno}")
    print(f"Promedio: {mj_prom:.1f}")
    print(f"Notas: {notas}")

def cantidad_aprobados(alumnos):
    if len(alumnos) == 0:
        print("No hay promedios para mostrar! ")
        return
    
    reprobados = 0
    aprobados = 0

    for nombre,datos in alumnos.items():
        promedio = datos[2]

        if promedio < 4.0:
            reprobados = reprobados + 1
        else:
            aprobados = aprobados + 1 
        
    print(f"Cantidad de aprobados: {aprobados}")
    print(f"Cantidad de reprobados: {reprobados}")

def escape(alumnos):
    print("Saliendo del programa! ")
    exit()

def menu(alumnos):

    while True:
        print("    MENU NOTAS DE PROGRAMACIÓN     ")
        print("1.- Agregar alumno")
        print("2.- Mostrar alumnos")
        print("3.- Ver promedios")
        print("4.- Mejor alumno")
        print("5.- Cantidad de aprobados y reprobados")
        print("6.- Salir")

        opciones = {
            1:agregar_alumnos,
            2:mostrar_alumnos,
            3:mostrar_promedios,
            4:mejor_alumno,
            5:cantidad_aprobados,
            6:escape
        }

        while True:
            try:
                op = int(input("Ingresa una opción: "))
                if op not in opciones:
                    print("Ingrese una opción dentro de las opciones! ")
                else:
                    break
            except ValueError:
                print("Ingrese solo numeros porfavor! ")

        if op == 1:
            agregar_alumnos(alumnos)
        elif op == 2:
            mostrar_alumnos(alumnos)
        elif op == 3:
            mostrar_promedios(alumnos)
        elif op == 4:
            mejor_alumno(alumnos)
        elif op == 5:
            cantidad_aprobados(alumnos)
        elif op == 6:
            escape(alumnos)




menu(alumnos)