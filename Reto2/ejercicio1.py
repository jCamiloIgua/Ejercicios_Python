#   Primer ejercicio reto 2
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 23/06/2022
#   Grupo 75


#Variables
numeroIngresado = 0
dosCifras = 0
centena = 0
unidad = 0
mil = 0
numeroMedio = 0
numeroDivisible = 0
#

numeroIngresado = int(input("Ingrese un numero entero: "))

if((numeroIngresado <= 9999) and (numeroIngresado >=0)):
    if((numeroIngresado >= 0) and (numeroIngresado <= 9)):
        print("El numero ",numeroIngresado," es palindrome")
    else:
        if((numeroIngresado >= 10)and (numeroIngresado <=99)):
            dosCifras = numeroIngresado % 11
            if(dosCifras == 0):
                print("El numero ",numeroIngresado," es palindrome")
            else:
                print("El numero ",numeroIngresado," NO es palindrome")
        else:
            if((numeroIngresado >=100)and (numeroIngresado <=999)):
                centena = numeroIngresado // 100
                unidad= numeroIngresado % 10
                if(centena == unidad):
                    print("El numero ",numeroIngresado," es palindrome")
                else:
                    print("El numero ",numeroIngresado," NO es palindrome")
            else:
                if((numeroIngresado >=1000) and (numeroIngresado <= 9999)):
                    unidad = numeroIngresado % 10
                    mil = numeroIngresado // 1000
                    numeroMedio = numeroIngresado - (mil * 1000)
                    numeroDivisible = (numeroMedio // 10) % 11
                    if(unidad == mil):
                        if(numeroDivisible == 0):
                            print("El numero ",numeroIngresado," es palindrome")
                        else:
                            print("El numero ",numeroIngresado," NO es palindrome")
                    else:
                        print("El numero ",numeroIngresado," NO es palindrome")


else:
        print("Señor usuario por favor solo ingrese numeros enteros de 1 a 4 cifras, positivos.")