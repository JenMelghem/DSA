import Array

maxSize = 10 # Max size of the array

arr = Array.Array(maxSize) # Create an array object

arr.insert(77) # Insert 10 items
arr.insert(99)
arr.insert("foo")
arr.insert("bar")
arr.insert(44)
arr.insert(55)
arr.insert(12.34)
arr.insert(0)
arr.insert("baz")
arr.insert(-17)

print("Array containing", len(arr), "items")
arr.traverse()

print("Search for 12 returns", arr.search(12))

print("Search for 12.34 returns", arr.search(12.34))

print("Deleting 0 returns", arr.delete(0))
print("Deleting 17 returns", arr.delete(17))

print("Setting item at index 3 to 33")
arr.set(3, 33)

print("Array after deletions has", len(arr), "items")
arr.traverse()


# inciso 2.3 Clasificar el arreglo utilizando "sorted()"

print("\nMatriz desordenada:")
arr.traverse()

arreglo_clasificado = []
arr.traverse(lambda item: arreglo_clasificado.append(item))

arreglo_clasificado_numerico = [item for item in arreglo_clasificado if isinstance(item, (int, float))]
arreglo_clasificado_letras = [item for item in arreglo_clasificado if isinstance(item, str)]

arreglo_clasificado_numerico = sorted(arreglo_clasificado_numerico)
arreglo_clasificado_letras = sorted(arreglo_clasificado_letras)

arreglo_clasificado_ordenado = arreglo_clasificado_numerico + arreglo_clasificado_letras

print("\nMatriz ordenada:")
for item in arreglo_clasificado_ordenado:
    print(item)



#INCISO 2.1
print("\n*Buscar número mayor*")
max=arr.getMaxNum()
print("\nEl mayor es: %s " % (max))

#INCISO 2.2 (Borra el número mayor de la lista)
# arr.delete(max) 
arr.deleteMaxNum()
arr.traverse()
