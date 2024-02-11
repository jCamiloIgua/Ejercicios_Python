#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 25/06/2022
#   Grupo 75
#   Sesion N.12

#Copia por referencia
lista2 = [1,2,3,4,5,6,7,8]
lista4 = lista2

lista2[3] = 10 #cambiamos dato
print(lista4)

#copia por valor 
lista3 = list(lista4) #se copio la lista4 en otro espacio en memoria
print(lista3)