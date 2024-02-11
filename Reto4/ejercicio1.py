#   Segundo ejercicio reto 4
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 2/07/2022
#   Grupo 75

#Variables

resumenAutor = " " #guarda el resumen ingresado por consola
palabras = " " #guarda el resumen separado por espacios
palabra = " " # recorre el string de las palabras
caracteres = " " #guardara los caracteres especiales
palabrasEstablecidas = 50 #contiene una constante de 50 
lasPalabras = " " #guarda las palabras convertidas en un arreglo
repeticionPalabra = " "

#Se captura el resumen
resumenAutor = input("Digite el resumen de su obra: ") #captura resumen
palabras = resumenAutor.split() #separa las palabras en espacios en una list
#

#se cuentan la cantidad de palabas ingresadas
contador = 0  
while contador < len(palabras):
    palabra = palabras[contador] #recorre el string de las palabras y las cuenta
    contador = contador + 1  # contador contiene la cantidad de palabras que fueron contadas 
print("Palabras ingresadas del resumen:" , contador, " palabras") #imprime la cantidad de palabras ingresadas del contador de ese momento
#

#validacion de la cantidad de palabras ingresadas 
if(contador <= 50):
    caracteres = ",",";",":",".","(",")","¿","?" #se guardan los caracteres a quitar del resumen con replace (remplazar)

    for contador in caracteres:
        resumenAutor  = resumenAutor.replace(contador, "") #quitamos caracteres especiales y se remplazan con un espacio

    #convertimos todas las palbras a minusculas para evitar errores al contar las palabras
    #usamos lower
    resumenAutor = resumenAutor.lower()
    
    #convertimos las palbras en un arreglo sin espacios
    lasPalabras = resumenAutor.split(" ")

    #creamos diccionario
    palabraDiccionario = {} #vacio
    
    print("Numero de palabras repetidas del resumen")
    print("//////////////////////////////")
    for unaPalabra in lasPalabras: #unaPalabra sirve como contador y cuanta las pocisiones del lasPalabras

        if unaPalabra in palabraDiccionario: #si la palabra esta una vez en el diccionario se le suma un valor de 1
            palabraDiccionario[unaPalabra] = palabraDiccionario[unaPalabra]+ 1 #diccionario en la pocision en unapalbra palabra
        else:
            palabraDiccionario[unaPalabra] = 1

    for unaPalabra in palabraDiccionario:
        repeticionPalabra = palabraDiccionario[unaPalabra]
        print(f"La palabra '{unaPalabra}' se repite : {repeticionPalabra}") #impime la repeticion de cada palabra
        
    print("//////////////////////////////")

else:
    print("Señor autor sobre paso las 50 palabras del resumen, escribio ", contador, " palabras")
    contador = contador - palabrasEstablecidas #resta la cantidad de palabras establecidas con la cantidad de palabras ingresadas
    print("Se sobre paso de las 50 palabras por: ", contador)
print("Fin del programa..")