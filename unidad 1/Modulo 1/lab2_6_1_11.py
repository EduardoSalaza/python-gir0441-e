'''
Autor: jesus eduardo salazar
Fecha: 19-ene-23
'''

hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

 

# calcula los minutos y los convierte a una cadena

minutos=str((min+dura) %60)

# calcula los minutos totales y luego lo convierte a horas y despues a una cadena

horas= str( ((hora*60 + min + dura)//60) % 24)

 

 

print("Hora: " +horas +":" +minutos)