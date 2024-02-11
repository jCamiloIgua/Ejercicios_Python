#  Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 24/06/2022
#   Grupo 75
#   Sesion N.11

#Hacer un programa que permita saber si un numero ingresado es primo o no primo

numero = int(input("Digite un numero entero: "))
if((numero == 1) or (numero == 2)):
    print("El numero ", numero, " es primo")
else:
    contador = 2
    bandera = False
    while(contador <= numero-1):
        residuo = numero % contador
        if(residuo == 0):
            bandera = True  #Si ya entro cambiamos la  bandera a true
            break # se usa para salir del ciclo
        contador = contador + 1
    if(bandera):
        print(numero, "No es primo") #Si es tru no es primo
    else:
        print(numero, " es primo") #Si es false es primo