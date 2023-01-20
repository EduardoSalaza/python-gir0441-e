'''
 Autor: jesus eduardo salazar
        Fecha: 6-ene-23
'''

#El space en el documento decia variable pero la puse como constante
space = " "
#Asignaciónd de valores por parte del usuario por proceso de pregunta
name = input("¿Cuál es su nombre? ")
lastname = input("¿Cuál es su apellido? ")
location = input("¿Donde vive? ")
age = input("¿Qué edad tiene usted? ")

#Impresion con concatenación
print("Hola!", name, lastname, "de", location, "y tiene", age, "años")
print("Hola!",space,name,space,lastname,space,"de",space,location,space,"y tiene",space,age,space,"años")