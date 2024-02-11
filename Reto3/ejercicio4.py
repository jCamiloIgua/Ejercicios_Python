#   Cuarto ejercicio reto 3
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 27/06/2022
#   Grupo 75
print("Figura numero 4 de asteriscos con n = 4")
N = 4
contadorRenglon= 1

while(contadorRenglon <= N):  #Ciclo externo
    contadorColumna = 1  
    linea = " " 

    while(contadorColumna <= N): #Ciclo interno

        if((contadorColumna <= 4) and (contadorRenglon == 1)):
            linea = linea + " * "
            contadorColumna = contadorColumna + 1
        else:
            if((contadorColumna <=3) and (contadorRenglon == 2)):
                linea = linea + " * "
                contadorColumna = contadorColumna + 1
            else:
                if((contadorColumna <= 2)and (contadorRenglon == 3)):
                    linea = linea + " * "
                    contadorColumna = contadorColumna + 1
                else:
                    if((contadorColumna ==1) and (contadorRenglon == 4)):
                        linea = linea + " * "
                        contadorColumna = contadorColumna + 1
                    else:
                        linea = linea + " _ "
                        contadorColumna = contadorColumna + 1

    #Fin del while
    print(linea) #termine ciclo imprime

    contadorRenglon = contadorRenglon + 1

print("Fin del programa...")