'''
Autor: jesus eduardo salazar    
Fecha: 19-ene-23
Crear un programa que al ingrresar una palabra este la imprima sin las vocales 
'''


palabraSinVocal = ""
userWord = ""

#El usuario ingresa una palabra y se convierte a mayusculas
userWord = input("Ingrese una palabra: ")
userWord = userWord.upper()

#Entrea en un ciclo for que funciona con if y elif 
for letra in userWord:
    if letra == "A":
        continue
    elif letra == "E":
        continue
    elif letra == "I":
        continue
    elif letra == "O":
        continue
    elif letra == "U":
        continue
    else:
        palabraSinVocal += letra

#Se imprime la palabra sin vocales
print(palabraSinVocal)