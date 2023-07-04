import os
from SimpleStack import *

stack = Stack(10)

try:
   os.system('cls') 
   for word in ['May', 'the', 'force', 'be', 'with', 'you']:
      stack.push(word)
   print (stack)

   new=input('Agrega otro elemento al arreglo: ')
   stack.push(new)
except Exception as e: 
   print("Error:", str(e))

print('La pila final es:',stack)
      
#print('After pushing', len(stack), 
      #'words on the stack, it contains:\n', stack)

#print('Is stack full?', stack.isFull())
print("\nPresione una tecla para continuar...")
input()

try:
    os.system('cls') 
    print('Sacando elementos de la pila:')
    while not stack.isEmpty():
        print (stack)
        print(stack.pop(), end=' ')
    stack.pop()  
except Exception as e:
    print("\nError:", str(e))

#print()
print(stack)