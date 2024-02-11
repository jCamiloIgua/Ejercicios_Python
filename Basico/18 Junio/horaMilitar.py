#   Quinto Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 18/06/2022
#   Grupo 75
#   Sesion N.6

#Problema

#Capturar la hora entre las 0 y 24 y mandar un saludo

hora = int(input("Por favor digite una hora valida (0 a 24): "))
if(hora >= 0 and hora <= 24):
    if(hora > 0 and hora < 12):
        saludo = "Buenos dias"
    else:
        if(hora >= 12 and hora < 18):
            saludo = "Buenas tardes"
        else:
            saludo = "Buenas noches"
    print(saludo)

else:
    print("La hora digitada no es valida, se admiten numeros entre 0 y 24")