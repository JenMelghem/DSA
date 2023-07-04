import os
from SimpleStack import *

#4.2 Metodo del palindromo


print ("EJEMPLO DE STACKS")
rango= int (input("Crearemos tu primer stack. ¿De que rango quieres que sea la pila?: "))
stack = Stack(rango)

try:
   os.system('cls') 
   print ("Pila por defecto")
   for word in ['radar', 'the', 'reconocer', 'be', 'somos', 'you']:
      stack.push(word)
   print (stack)

   new=input('Agrega otro elemento al arreglo: ')
   stack.push(new)
except Exception as e: 
   print("\nError:", str(e))

print('La pila final es:',stack)
      
#print('After pushing', len(stack), 
      #'words on the stack, it contains:\n', stack)


#print('Is stack full?', stack.isFull())

print("\nPresione una tecla para continuar...")
input()
os.system('cls')

#4.2
print("Verificando si las palabras son palíndromas:\n")
while not stack.isEmpty():
    word = stack.pop()
    if stack.es_palindroma(word):
        print(f"{word} es una palabra palíndroma.")
    else:
        print(f"{word} no es una palabra palíndroma.")

print("\nPresione una tecla para continuar...")
input()
os.system('cls')

try:
    print('Sacando elementos de la pila:')
    while not stack.isEmpty():
        print (stack)
        print('\n',stack.pop(), end=' fue el elemento eliminado. \nLos elementos restantes son: \t')
    stack.pop() 

except Exception as e:
    print()
    print("\nError:", str(e))



