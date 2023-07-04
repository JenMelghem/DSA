from SortArray import *
import random
import timeit
import statistics

def initArray(size=10, maxValue=5000, seed=3.1415916):
    """Create an Array of the specified size with a fixed sequence of
       'random' elements"""
    arr = Array(size)                   # Create the Array object
    random.seed(seed)                   # Set random number generator
    for i in range(size):               # to known state, then loop
        arr.insert(random.randrange(maxValue)) # Insert random numbers
    return arr                          # Return the filled Array

arr = initArray()
print("La matriz contiene", len(arr), "elementos:\n", arr)

for test in ['\ninitArray().bubbleSort()',
             'initArray().selectionSort()',
             'initArray().insertionSort()']:
    elapsed = timeit.timeit(test, number=100, globals=globals())
    print(test, "Su tiempo fue:", elapsed, "seconds", flush=True)

arr.insertionSort()
print('\nSorted array contains:\n', arr)

mediana = arr.mediana()
print("\nLa mediana del arreglo es:", mediana)
#print("El procedimiento para culcular la mediana fue:", indice1)

media = arr.media()
print("\nLa media del arreglo es:", media)