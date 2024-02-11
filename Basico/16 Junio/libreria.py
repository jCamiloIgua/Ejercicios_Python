#   Segundo Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 16/06/2022
#   Grupo 75
#   Sesion N.6

#Problema

"""Una libreria vende 2 tipos de libros, un libro vale 20.000 y
el otro libro vale 30.000, se deben vender cada uno con el
19% de IVA, crear un programa que permita realizar el pago"""

#

#variables

nombreCliente = " "
telefonoCliente = " "
cedulaCliente = " "
cantidadLibro1 = 0
cantidadLibro2 = 0
totalLibros1 = 0
totalLibros2 = 0
totalSuma = 0
iva = 0.0
totalFinal = 0.0

#

#Ingreso de datos

nombreCliente = input("Digite el nombre del cliente: ")
telefonoCliente = input("Digite el numero de telefono del cliente: ")
cedulaCliente = input("Digite el numero de cedula del cliente: ")
cantidadLibro1 = int(input("Digite la cantidad de libros rojos: "))
cantidadLibro2 = int(input("Digite la cantidad de libros negros: "))

#

#Procesos

totalLibros1 = cantidadLibro1 * 20000
totalLibros2 = cantidadLibro2 * 30000
totalSuma = totalLibros1 + totalLibros2

iva = totalSuma * 0.19
totalFinal = totalSuma + iva

#

#Salida

print("\n")
print("///////////////////////////////////////////////////////////////////////////")
print("\t\t\t\t Libreria don Camilo")
print(" Nit: 2157.27787 \n Telefono: 601-54577882 \n Direccion: Calle 4587 No 124" )
print("///////////////////////////////////////////////////////////////////////////")
print("Datos del Usuario")
print("  ")
print("Cliente: ", nombreCliente)
print("Telefono cliente: ", telefonoCliente)
print("Numero de documento: ", cedulaCliente)
print("---------------------------------------------------------------------------")
print("Datos de la Compra")
print("  ")
print("Item           Articulo              Cantidad                 Total")
print("1.            Libro Rojo              ",cantidadLibro1,"                    ",totalLibros1)
print("2.            Libro Negro             ",cantidadLibro2,"                    ",totalLibros2)
print("IVA:                                                         ", iva )
print("Total Compra:                                                ",totalFinal)
print("---------------------------------------------------------------------------")

#