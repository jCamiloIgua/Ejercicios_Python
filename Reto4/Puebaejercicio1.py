#resumen = []
palabras = " "

#Captura del resumen
#palabras = input("Escriba su resumen No se sobre pase de las 50 palabras: ")
#resumen.append(palabras)

#print(resumen)

#lista = 'camilo el feo, del turno; del avion. picado'
#ingnorar
#resumenCorrecto = len(lista.split(','))

#print("Son " , str(resumenCorrecto), " palabras")


#resumen = " Los animes son feos, porque cada vez; son mas largod. No hay tiempo"
contador = 0
resumenLista = []
resumen = input("Escriba su resumen No se sobre pase de las 50 palabras: ")
while(contador <= 50):
    resumenLista.append(resumen)
    palabras = resumen.split()
    contador = contador + 1

while contador < len(palabras):
    palabra = palabras[contador]
    
    contador = contador + 1
print(contador)
print(resumenLista[0])

"""texto = input("Digite el resumen: ")

simbolos = ['¿','?','.','.',';',':','¡','!']
numpalabras = 0

for linea in texto:
    for simbolo in simbolos:
        linea = linea.replace(simbolo,' ')
    palabras = linea.split()
    for palabra in palabras:
        numpalabras += 1
print('El texto contiene %s palabras' %numpalabras)"""