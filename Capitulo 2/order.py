class OrderedRecordArray(object):
    def __init__(self, initialSize, maxSize, key=identity):
        self.__a = [None] * initialSize
        self.__nItems = 0
        self.__key = key
        self.__maxSize = maxSize

    def __resize(self, new_size):
        new_array = [None] * new_size
        for i in range(self.__nItems):
            new_array[i] = self.__a[i]
        self.__a = new_array

    def insert(self, item):
        if self.__nItems >= self.__maxSize:
            # Expandir la lista multiplicando el tamaño actual por un múltiplo fijo
            new_size = self.__maxSize * 2
            self.__resize(new_size)
            self.__maxSize = new_size

        j = self.find(self.__key(item))
        for k in range(self.__nItems, j, -1):
            self.__a[k] = self.__a[k-1]
        self.__a[j] = item
        self.__nItems += 1

# Prueba para comparar estrategias de crecimiento de la lista

# Estrategia de incremento fijo
arr_fixed = OrderedRecordArray(5, 5)
for i in range(10):
    arr_fixed.insert(i)

print("Lista con estrategia de incremento fijo:")
for i in range(len(arr_fixed)):
    print(arr_fixed.get(i))
print()

# Estrategia de multiplicar el tamaño actual
arr_multiple = OrderedRecordArray(5, 5)
for i in range(10):
    arr_multiple.insert(i)
    if len(arr_multiple) >= arr_multiple._OrderedRecordArray__maxSize:
        new_size = arr_multiple._OrderedRecordArray__maxSize * 2
        arr_multiple._OrderedRecordArray__resize(new_size)
        arr_multiple._OrderedRecordArray__maxSize = new_size

print("Lista con estrategia de multiplicar el tamaño actual:")
for i in range(len(arr_multiple)):
    print(arr_multiple.get(i))
