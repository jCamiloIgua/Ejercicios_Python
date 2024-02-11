#  Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 23/06/2022
#   Grupo 75
#   Sesion N.10

numero =int(input("Digite un numero entero: "))
columna = 1
while(columna <= numero):
    renglon = 1
    linea = " "
    while(renglon <= numero):
        linea = linea + " * "
        renglon = renglon + 1
    print(linea)
    columna = columna + 1

