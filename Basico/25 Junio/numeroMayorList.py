#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 25/06/2022
#   Grupo 75
#   Sesion N.12

#Capturar cinco numeros y decir cual es el mayor
lista = []
contador = 0
while(contador < 5):
    num = int(input("Digite un numero :"))
    lista.append(num)
    contador = contador + 1

mayor = max(lista)
print("El numero mayor es: ", mayor)