#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 29/06/2022
#   Grupo 75
#   Sesion N.14


def suma(a,b):
    s = a + b
    return s


def dato():
    s1 = int(input("Digite un numero: "))
    return s1

def principal():
    d1 = dato()
    d2 = dato()
    print("La suma de", d1, " y", d2, "es : ", suma(d1, d2))

principal()