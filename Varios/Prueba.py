#Cree un programa que me permita registar usuarios el programa debe perdr lo siguiente:
#Nombre
#edad
#Cedula
#cargo

cantidadPersonas = 0
nombrePersona = ""
edadPersona = " "
cedulaPersona = " "
cargoPersona = " "

contadorRegistro = 1
contadorPantalla = 0
decision = ' '

decision = input("¿Desea ingresar un usuario?: (S / N): ")

while(decision == 'S'):
    cantidadPersonas = int(input("Ingrese la cantidad de personas a registar: "))
    while(contadorRegistro <= cantidadPersonas):
        contadorRegistro = contadorRegistro + 1
        contadorPantalla = contadorPantalla + 1 
        print("Ingrese la persona numero: ", contadorPantalla)
        nombrePersona = input("Ingrese el nombre completo: ")
        edadPersona = input("Ingrese la edad de la persona: ")
        cedulaPersona = input("Ingrese la cedula de la persona:")
        cargoPersona = input("Ingrese el cargo de la persona: ") 
        
    decision = input("¿Desea ingresar un usuario?: (S / N): ")
    contadorRegistro = 1   #Limpio variables
    contadorPantalla = 0

print("Fin del programa...")   



"""Aplique lo aprendido en JAVA EN phyton y funciona igual, es igual la logica, solo cambia la sintaxis"""


