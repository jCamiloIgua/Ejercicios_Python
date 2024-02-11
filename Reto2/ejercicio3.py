#   Tercer ejercicio reto 2
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 21/06/2022
#   Grupo 75

#Variables
numeroUno = 0
numeroDos = 0
caracter = ' '
operacionMatematica = 0

numeroUno = int(input("Ingrese el primer numero: "))
numeroDos = int(input("Ingrese el segundo numero: "))
caracter = input("Ingrese el caracter de la operacion: ")

if((caracter == '+') or (caracter == '-') or (caracter == '*') or (caracter == '/') or (caracter == '%') ):
    if(caracter == '+'):
        operacionMatematica = (numeroUno + numeroDos)   
        print("La suma de ",numeroUno, "y ",numeroDos, "es: ", operacionMatematica)
    else:
        if(caracter == '-'):
            operacionMatematica = (numeroUno - numeroDos)
            print("La resta de ",numeroUno, "y ",numeroDos, "es: ", operacionMatematica)
        else:
            if(caracter == '*'):
                operacionMatematica = (numeroUno * numeroDos)
                print("La multiplicacion de ",numeroUno, "y ",numeroDos, "es: ", operacionMatematica)
            else:
                if(caracter == '/'):
                    operacionMatematica = (numeroUno / numeroDos)
                    print("La division de ",numeroUno, "y ",numeroDos, "es: ", operacionMatematica)
                else:
                    operacionMatematica = (numeroUno % numeroDos)
                    print("El resto o el modulo de la division entre: ",numeroUno, "y ",numeroDos, "es: ", operacionMatematica)

else:
    print("No se especifico una operacion valida")
    
print("Fin del programa")

