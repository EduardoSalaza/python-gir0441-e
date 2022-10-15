'''
Act:Utilizar la sentencia if-elif-else.
Autor: Jesus Eduardo Salazar Venegas 
'''

year = int(input("Introduce un año:"))

if year % 4 !=0: #No es divisible entre 4
   print('Año común')
elif year % 100 !=0: #año Bisiesto
   
   print('Año Bisiesto')
elif year % 400  !=0: 
    print('Año Común')
else:
   print('De lo contrario, es un año bisisesto')

    
#
# Escribe tu código aquí.
#	numero % 2 ==0: 