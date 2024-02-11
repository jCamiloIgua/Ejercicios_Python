#Ejercicio Mision Tic 2022
#   @Autor: Jonatan Camilo Igua Contreras
#   @Date: 29/06/2022
#   Grupo 75
#   Sesion N.14

x = 0
[x ** 2 for x in range(10)]

print([x])

notas ={'carmen': 5, 'Antonio': 4, 'Juan': 8, 'Monica': 9, 'Maria': 9, 'Pablo': 3}
[nombre for (nombre, nota) in notas.items() if nota >=5]