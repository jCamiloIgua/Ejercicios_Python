#   Cuarto Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 17/06/2022
#   Grupo 75
#   Sesion N.6

#Problema

#Capturar tres numeros ty decir cual es el mayor

a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))
c = int(input("Digite el tercer numero: "))

if(a>b and a>c):
    mayor = a
else:
    if(b>a and b>c):
        mayor = b
    else:
        mayor = c

print("El numero mayor de los 3 ingresados es: ", mayor)