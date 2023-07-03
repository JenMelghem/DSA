import os

def primos():
    os.system('cls')
    print()
    print("Ingresa el número del que deseas saber si es primo o no")
    print("********************************************************")
    print()
    pri = int(input("->\t"))

    es_primo = True

    if pri < 2:
        es_primo = False
    else:
        for i in range(2, pri):
            if pri % i == 0:
                es_primo = False
                break

    if es_primo:
        print("\nEl número", pri, "es primo")
        print()
    else:
        print("\nEl número", pri, "no es primo pero te mostrare sus factoriales")
        for i in range(1, pri + 1):
            if pri % i == 0:
                print(i)


preg_1 = True

while preg_1:
    
    primos()
    preg = int(input("\n¿Desea ingresar otro número?\n1. Sí\n2. No\n"))
    if preg != 1:
        preg_1 = False

os.system('cls')
print("Espero haberte ayudado")
