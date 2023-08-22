from Anagram import *
import os
os.system('cls')
print ("\t\t \t A N A G R A M A S  D E  U N A  P A L A B R A")
print ('\nEl método de los anagramas se basa en la reorganización de las letras de una palabra')
print ( 'o frase para formar nuevas palabras o frases que contengan exactamente las mismas letras,')
print ('pero en un orden diferente')
print()
print('Elige que deseas hacer')
print('1.Saber los anagramas de una palabra')
print('2.Saber si dos palabras son anagramas')
op = int(input())

if op == 1: 
    os.system('cls')
    print ("\t\t \t A N A G R A M A S  D E  U N A  P A L A B R A")
    print('\nIngresa una palabra')
    word = input('->')
    result = anagrams(word)
    print (result)

if op ==2:
    os.system('cls')
    print ("\t\t \t S O N  A N A G R A M A S  D O S  P A L A B R A S ?")
    print ('\nIngrese la primera palabra')
    word1 = input('->')
    print ('\nIngrese la segunda palabra\n')
    word2 = input('->')
    
    if is_anagram(word1, word2):
        print(f"{word1} y {word2} son anagramas!")
    else:
        print(f"{word1} y {word2} no son anagrmas :(")