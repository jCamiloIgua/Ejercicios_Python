#   Segundo ejercicio reto 2
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 21/06/2022
#   Grupo 75

#Variables
fechaVenta = " "
nombreVendedor = " "
nombreComprador = " "
cantidadCamisas = 0  
VALORCAMISAS = 60.000     #constante
totalBrutoCa = 0.0
CINCOPORCIENTO = 5        #constante
DIEZPORCIENTO = 10        #constante
QUINCEPORCIENTO = 15      #constante
descuentoCa = 0.0
totalNetoCa = 0.0
IVA = 0.19                  #constante
descuento = 0
multiplicacionIva = 0.0
valorTotal = 0
#

fechaVenta = input("Ingrese la fecha de la venta: ")
nombreVendedor = input("Ingrese el nombre del vendedor: ")
nombreComprador = input("Ingrese el nombre del comprador: ")
cantidadCamisas = int(input("Ingresar la cantidad de camisas: "))

if(cantidadCamisas > 0):
    totalBrutoCa = (cantidadCamisas * VALORCAMISAS)
    if(totalBrutoCa <= 180.000):
        descuentoCa = (CINCOPORCIENTO * totalBrutoCa)/100
        totalNetoCa = totalBrutoCa - descuentoCa
        descuento = CINCOPORCIENTO
        multiplicacionIva = totalNetoCa * IVA
        valorTotal = totalNetoCa + multiplicacionIva
    else:
        if(totalBrutoCa <= 240.000):
            descuentoCa = (DIEZPORCIENTO * totalBrutoCa)/100
            totalNetoCa = totalBrutoCa - descuentoCa
            descuento = DIEZPORCIENTO
            multiplicacionIva = totalNetoCa * IVA
            valorTotal = totalNetoCa + multiplicacionIva
        else:
            if((totalBrutoCa > 240.000) and (totalBrutoCa <= 360.000)):
                totalNetoCa = totalBrutoCa
                descuento = 0
                multiplicacionIva = totalNetoCa * IVA
                valorTotal = totalNetoCa + multiplicacionIva

            else:
                descuentoCa = (QUINCEPORCIENTO * totalBrutoCa)/100
                totalNetoCa = totalBrutoCa - descuentoCa
                descuento = QUINCEPORCIENTO
                multiplicacionIva = totalNetoCa * IVA
                valorTotal = totalNetoCa + multiplicacionIva
    
    #Factura
    print("//////////////////////////////////////////////")
    print("\t\t\tFACTURA")
    print("Fecha: ", fechaVenta)
    print("Nombre vendedor: ", nombreVendedor)
    print("Nombre comprador: ", nombreComprador)
    print("----------------------------------------------")
    print("Cantidad de camisas: ", cantidadCamisas)
    print("Valor bruto: ", totalBrutoCa,"00")
    print("Valor descuento: ", descuento, "%")
    print("IVA: ", IVA,)
    print("Valor neto: ", totalNetoCa,"00")
    print("Valor Total pagar: ", valorTotal,"00")  #se agregaron dos ceros porque no aparecen para facilitar la lectura del valor
    print("//////////////////////////////////////////////")

else:

    print("Señor usuario recuerde colocar un numero de camisas valido \n (enteros positivos)")

print("Fin del programa...")

