#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 24/06/2022
#   Grupo 75
#   Sesion N.11

try:
    dividendo = int(input("Digite el dividendo: "))
    divisor = int(input("Digite el divisor: "))
    division = dividendo / divisor
    print(dividendo, " / ", divisor, " = ", division)
except:
    print("Hay errores en sus datos")

#Si dividimos entre cero envia el mensaje global
#Si no gresamos un numero entero si no en letras solo manda el error con ese mesaje global