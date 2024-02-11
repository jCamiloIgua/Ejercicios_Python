#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 25/06/2022
#   Grupo 75
#   Sesion N.12

#Repetir el codigo despues de un error de digitacion 

flag = True #bandera

while(flag): #Entra verdadero
    try:
        n = int(input("Digite un numero: "))
        flag = False  #lo digita bien flase para salir del while
    except:
        print("Debe digitar un numero no una letra") #Si digita mal sigue en tru manda mensaje y repite

print("Digito: ", n)