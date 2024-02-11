#  Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 23/06/2022
#   Grupo 75
#   Sesion N.10

numero = int(input("Digite un valor entero: "))
suma = 0
for contador in range (1, numero + 1, 2):
    suma = suma + contador
print("La suma desde 1 hasta ", numero, "es ", suma)

#Inicia el contador inicia en uno y termina en cuatro osea menor igual y va incrementando elcontador en dos en dos