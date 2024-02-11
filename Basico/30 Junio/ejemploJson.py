#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 30/06/2022
#   Grupo 75
#   Sesion N.15

import json

datos = {"nombre":"Juan","edad":20, "NumeroMascotas":"2","NombreMascota":"Tribilin"}

with open('unab.json',"w") as miArchivo:

    json.dump(datos,miArchivo)

with open ("unab.json","r") as lectura:

    d = json.load(lectura)

    print (d["NombreMascota"])

    print(d)