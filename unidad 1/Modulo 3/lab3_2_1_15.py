'''
Autor: jesus eduardo salazar
Fecha: 19-ene-23
Escribe un programa que lea un número natural y ejecute los pasos anteriores 
siempre que c0 sea diferente de 1.
'''
def Collatz(numero):
    pasos = 0
    while numero != 1:
        if numero%2==0:
            numero /= 2
            print(int(numero))
            pasos +=1
        else:
            numero = 3*numero + 1 
            print(int(numero))
            pasos+=1
    print("Pasos =",pasos)
    
    

numero = int(input("Ingrese un número: "))
Collatz(numero)