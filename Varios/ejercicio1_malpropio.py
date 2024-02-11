#   Primer ejercicio reto 2
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 22/06/2022
#   Grupo 75

#Variables

primerDigito = ' '
segundoDigito = ' '
tercerDigito = ' '
cuartoDigito = ' '
numeroIngresado = " "

print("Este programa le permitira saber si un numero de cuatro cifras enteras es palindrome")
primerDigito = input("Ingrese el primer digito de una sola cifra: ") #cada digito se captura como texto
segundoDigito = input("Ingrese el segundo digito de una sola cifra: ")
tercerDigito = input("Ingrese el tercer digito de una sola cifra: ")
cuartoDigito = input("Ingrese el cuarto digito de una sola cifra: ")

numeroIngresado = (primerDigito + segundoDigito + tercerDigito + cuartoDigito) # Une los numeros ingresados ya que son una cadena
numeroIngresado = int(numeroIngresado) #se convirtio de string a entero para evaluar que el numero sea positivo y menor o igual a 9999

if((numeroIngresado <= 9999) and (numeroIngresado >=0)):

    if(primerDigito == cuartoDigito):
        if(segundoDigito == tercerDigito):
            print("El numero ", numeroIngresado," es palindrome")
        else:
            print("El numero ", numeroIngresado," NO es palindrome")
    else:
        print("El numero ", numeroIngresado," NO es palindrome")

else:
    print("Señor usuario por favor solo ingrese un numero entero de cuatro digitos , en cada espacio")

print("Fin del programa...")