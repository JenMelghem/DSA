import os
os.system('cls')
print("\t  SUCESION FIBONACCI")
print("\t**********************")
print()

def fib(n):
    a = 0
    b = 1
    total_vueltas = 0

    for f in range(n):
        c = a + b
        a = b
        b = c
        total_vueltas += 1

        # procedimiento en cada vuelta
        print(f"\tVuelta {f + 1}: a = b = {a}, b = c = {b}, c = {c}")

    print(f"\n\tValores finales: a = {a}, b = {b}")
    print(f"\nTotal de vueltas realizadas: {total_vueltas}")

    return 'Sucesion num:', b

for x in range(5):
    print(fib(x))
