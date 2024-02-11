#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 29/06/2022
#   Grupo 75
#   Sesion N.14

#Funcion de suma

#parametros
#argumentos posicionales
def suma(a,b): #parametros
    s = a + b 
    return s

s1 = int(input("Digite el primer numero: "))
s2 = int(input("Digite el segundo numero: "))
print("La suma de ", s1, " y", s2, "es : ", suma(s1, s2))  #paso argumentos a la funcion  s1 = a  y s2 = b

#argumentos nominales
uno = int(input("Digite el primer numero: "))
dos = int(input("Digite el segundo numero: "))
print("La suma de ", s1, " y", s2, "es : ", suma(b = uno, a = dos))