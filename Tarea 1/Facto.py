import os
def facto ():
    os.system('cls')
    print ()
    print("Ingresa el número del que deseas saber su factorial")
    print("********************************************************")
    print ()

    num= int(input("->\t"))
    print ()

    fact=1
    if num <0:
        print("El factorial no está definido")
    else: 
        for i in range (1, num+1):
            fact *= i

    print("El factorial de", num, "es", fact)
   
    preg = int(input("\nDesea ingresar otro numero?\n1. Sí\n2. No\n"))
    if preg == 1:
        facto()

facto()

os.system('cls')
print("Espero haberte ayudado")