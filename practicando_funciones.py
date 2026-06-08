

def multiplicacion(a,b):
    multiplicar = a * b

    print(f"El resultado de la multiplicacion de {a} * {b} es {multiplicar}")
    
    return(multiplicar)

num1 = int(input("Ingrese un numero: "))
num2 = int(input("Ingrese otro numero: "))

multiplicacion(num1,num2)


def tiene_numero(texto):
    numerico = False
    for caracter in texto:
        if caracter.isdigit():
            numerico = True
    return(numerico)

nombre = input("Ingresa tu nombre sin numeros: ")

if tiene_numero(nombre) == True:
    print("Acceso denegado, el nombre no puede contener numeros! ")
else:
    print("Acceso concedido! ")




