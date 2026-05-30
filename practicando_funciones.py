

def suma(a,b):

    sumar = a + b

    print(f"La suma de {a} + {b} es = {sumar}")

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

suma(num1,num2)

# SIN ARGUMENTO Y SIN RETORNO

def suma():
    num1 = 5
    num2 = 8

    return(num1 + num2)

print(f"La suma es: ",suma())

def suma(a,b):
    sumar = a + b
    return(sumar)

num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))

print("El resultado es: ",suma(num1,num2))


