#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 29/06/2022
#   Grupo 75
#   Sesion N.14

diccionario1 = {'nombre': 'Juan','direccion': 'Calle 126D N 104 A 29', 'mascota': 'Perro','Edad': 14}
diccionario2 = {'nombre': 'Camilo','direccion': 'Calle 126D N 104 A 29', 'mascota': 'Gato','Edad': 18}
print(diccionario1)
print(diccionario2)
print(diccionario1['nombre']) #Imprimir valor de la clave

# get

diccionario1['nombre'] = 'Carlos' #actualiza el valor de la clave del diccionario
print(diccionario1['nombre'])

diccionario2.get('direccion') #trae el valor de la clave no crea un espacio nuevo

print(diccionario2.get('direccion'))   

diccionario2.get('color', 'No hay color')
print(diccionario2.get('color', 'No hay color')) #busca la clase si no la encuentra manda otra cosa sin crear nada sin remplazar nada

#Keys

uno = diccionario1.keys()
print(uno)

#values
dos = diccionario1.values()
print(dos)

#items
tres = diccionario1.items()
print(tres)

#valor cambiar
diccionario1['altura'] = 1.2  #crea la clave con su valor lo crea al final
print(diccionario1)

#cargar valor cpaturar
diccionario2['Profecion'] = input("Digite su profecio: ") #anadir valores a la clave
print(diccionario2)

#update actualiza los datos iguales del diccionario1 y diccionarip 2