#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 25/06/2022
#   Grupo 75
#   Sesion N.12

#Devuelve el numero de elementos de la lista
listaUno = [1,2,3,4,5,6,7,8,9,10]
print("La longitud de la lista es: ", len(listaUno))
#

#El minimo elemento de la lista 
listaDos = [8,9,3,1,2,4,78,8]
print("El numero menor de la lista es: ", min(listaDos))
listaTres = ['a','f','t','w']
print("La letra menor de la lista es: ", min(listaTres))
#

#El maximo elemento de la lista
listaCuatro = [10,25,1,4,8,45]
print("El numero mayor de la lista es: ", max(listaCuatro))
#

#Suma de los elementos de la lista
listaCinco = [1,24,57,8,9]
print("La suma de los elementos es: ", sum(listaCinco))

#Buscar si existe elemento en  la lista

print("f" in listaTres)

#Capturar la busqueda
busqueda = "t" in listaTres
print(busqueda)

#

#Buscar posicion del elemento en la lista
print(listaCuatro.index(10))

#Buscar las veces que esta un elemento en una lista
print(listaDos.count(8))