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
except ValueError:
    print("Por favor debe digitar numeros no letras")
except ZeroDivisionError:
    print("El divisor debe ser diferente de 0")
except:
    print("Hay errores en sus datos") #Uno global si ocurre un error de evaluado
    