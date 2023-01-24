



import os
clear = lambda: os.system('cls')
clear()
# Diccionario de (número:7-segmento-hash)
dict1 = {
    '0':('###','# #','# #','# #','###'),
    '1':('#####'),
    '2':('###','  #','###','#  ','###'),
    '3':('###','  #','###','  #','###'),
    '4':('# #','# #','###','  #','  #'),
    '5':('###','#  ','###','  #','###'),
    '6':('###','#  ','###','# #','###'),
    '7':('###','  #','  #','  #','  #'),
    '8':('###','# #','###','# #','###'),
    '9':('###','# #','###','  #','###')
}

#  Función para imprimir números en formato de 7 segmentos.
def fun_PrintNums(num):
    if num < 0 or num % 1 > 0 or type(num)!=int:   # si num NO es un entero positivo.
        return "Invalid entry, please try again"
    else: 
        display = [' ']
        for i in str(num):      # convierte 'num' en STRING; para cada "número" en string 'num'


#'''Opción 1: funciona, pero imprime los números verticalmente en lugar de uno al lado del otro; Return=None '''' #
            for char in dict1[i]:
                print(*char)
print(fun_PrintNums(int(input("Enter any string of whole numbers: "))))


#''' Opción 2: El retorno funciona, pero sigue siendo vertical y no espaciado ''' #''
# for char in dict1[i]:
# display.append(char)
# return display
# print('œ'.join(fun_PrintNums(int(input("Introduzca cualquier cadena de números enteros:")))))
#---------------------------------------------------------------------#

#''' Opción 3: 'display' fila1 offset; espaciado como se desee, pero vertical; Return=None'''''' #
# for char in dict1[i]:                
# display += char
# display += '\n'
# a = print(*display,end='')
# return a
# print(fun_PrintNums(int(input("Introduzca cualquier cadena de números enteros:"))))
#---------------------------------------------------------------#