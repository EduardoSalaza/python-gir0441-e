'''
        Autor: jesus eduardo salazar
        Fecha: 24-ene-23
'''

from datetime import date, datetime

date - datetime(2020, 11, 4, 14, 53)

print (date.strftime("%Y/%m/%d %H:M:%S "))
print (date.strftime("%Y/%B/%d %H:M:%S %p"))
print (date.strftime("%a, %Y %b %d"))
print (date.strftime("%A, %Y %A %d"))
print (date.strftime("%A:%d"))
print (date.strftime("dia del año : %j"))
print (date.strftime("numero de la sema del año : %j"))
