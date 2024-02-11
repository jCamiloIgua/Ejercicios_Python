#   Primer ejercicio reto 4
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 30/06/2022
#   Grupo 75

#Capturar 10 numeros y generar el maximo, minimo y el promedio, de cada uno de ellos

#Variables

numeros = []
numero = 0
contador = 1
sumaNumeros = 0
promedio = 0
contadorPantalla = 1

flag = True #bandero
while(flag):
    try:

        #Cargar lista
        while(contador <= 10):
            print("Numero: ", contadorPantalla)
            contadorPantalla = contadorPantalla + 1
            numero = int(input("Digite el numero: "))
            numeros.append(numero)
            contador = contador  + 1

        flag = False #si ingreso los 10 numeros enteros sale del while flag
  
        #maximo numero

        maximo = numeros[0] #guarda el pimer numero para comparar

        for contador in range(0,10):
            if((numeros[contador]) > maximo):
                maximo = numeros[contador]
        print("El maximo numero ingresado es: ", maximo)


        #minimo numero

        menor = numeros[0]  #guarda el pimer numero para comparar

        for contador in range(0,10):
            if((numeros[contador]) < menor):
                menor = numeros[contador]

        print("El minimo numero ingresado es: ", menor)

        #promedio de los numeros

        for contador in range(0,10): #posicion 0 a 10
            sumaNumeros = sumaNumeros + numeros[contador]
            contador = contador + 1
        promedio = (sumaNumeros / 10)

        print("El promedio de los numeros ingresados es: ", promedio)
        print("Fin del programa...")


    #Ingreso mal un numero
    except ValueError:
        print("Por favor debe digitar numeros enteros ( No letras ni numeros decimales )")
        contadorPantalla = 1 #limpio variales para si comete un error al ingresar numeros las variables no lleven basura
        numeros = []
        numero = 0
        contador = 1
        print("______________")
    except:
        print("Hay errores en sus datos") #Una global si ocurre un error no evaluado
        print("______________")
        