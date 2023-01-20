'''
Autor: jesus eduardo salazar 
Fecha: 19-ene-23
El código debe mostrar uno de los dos mensajes posibles, que son Año Bisiesto o Año Común, 
según el valor ingresado.
'''

year = int(input("Introduce un año: "))

if year % 4 != 0: #No es divisble entre 
    print('Año común')
elif year % 100 != 0: #Año bisiesto
    print('Año bisiesto')
elif year % 400 != 0:
        print('Año común')
else:
    print("Es un año bisiesto")
