#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 30/06/2022
#   Grupo 75
#   Sesion N.15

def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplica(a,b):
    return a*b

def divide(a,b):
    return a/b

def resto(a,b):
    return a%b


def menu():
    print("_________________________________________________")
    operador1 = int(input("Digite el primer operador: "))
    operador2 = int(input("Digite el segundo operador: "))
    print("             MENU")
    print("Elija la opción que desee: ")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Residuo")
    print("6. Salir")

    resp = int(input("Cual es su opción: "))
    if (resp >=1 and resp <=6):
        if(resp == 1):
            print("La suma de ", operador1, " y ", operador2, " es : ", suma(operador1,operador2))
        elif(resp == 2):
            print("La resta de ", operador1, " y ", operador2, " es : ", resta(operador1,operador2))
        elif(resp == 3):
            print("La multiplicacion de ", operador1, " y ", operador2, " es : ", multiplica(operador1,operador2))
        elif(resp == 4):
            print("La división de ", operador1, " y ", operador2, " es : ", divide(operador1,operador2))
        elif(resp == 5):
            print("El residuo de ", operador1, " y ", operador2, " es : ", resto(operador1,operador2))
        else:
            print("Gracias por utilizar esta calculadora!!!!!!")
    else:
        print("Eligió una opción no válida. BYE!!!") 

menu()

