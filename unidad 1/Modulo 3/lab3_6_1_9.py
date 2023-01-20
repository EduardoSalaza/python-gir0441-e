'''
Autor: jesus eduardo salazar
Fecha: 19-ene-23
Escribir un programa que elimine todas las repeticiones de números de la lista.  
'''
miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

listaTemp = []

for numero in miLista:
    if numero not in listaTemp:
        listaTemp.append(numero)

miLista = listaTemp[:]

print("La lista solo con elementos únicos:")
print(miLista)