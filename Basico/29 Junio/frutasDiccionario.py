#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 29/06/2022
#   Grupo 75
#   Sesion N.13



frutas = {'Platano': 1.35,'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
fruta = input("Digite el nombre de la fruta que desea comprar: ")
kilos = float(input("Digite la cantidad de kilos a comprar: "))

if(fruta in frutas):
    valor = kilos * frutas[fruta]
    print("El valor de ",kilos, "kilos de ",fruta," es: ", valor)
else:
    print("la fruta no existe")