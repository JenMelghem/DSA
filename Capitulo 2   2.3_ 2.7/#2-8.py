#2-8
def identity(x):  # The identity function
    return x

class OrderedRecordArray(object):
    def __init__(self, initialSize, key=identity):  # Constructor
        self.__a = [None] * initialSize  # The array stored as a list
        self.__nItems = 0  # No items in array initially
        self.__key = key  # Key function gets record key

    def __len__(self):  # Special def for len() func
        return self.__nItems  # Return the number of items

    def get(self, n):  # Return the value at index n
        if n >= 0 and n < self.__nItems:  # Check if n is in bounds
            return self.__a[n]  # Only return item if in bounds
        raise IndexError("Index " + str(n) + " is out of range")

    def traverse(self, function=print):  # Traverse all items and apply a function
        for j in range(self.__nItems):  # Loop through items
            function(self.__a[j])

    def __str__(self):  # Special def for str() func
        ans = "["  # Surround with square brackets
        for i in range(self.__nItems):  # Loop through items
            if len(ans) > 1:  # Except next to left bracket
                ans += ", "  # Separate items with a comma
            ans += str(self.__a[i])  # Add the string form of the item
        ans += "]"  # Close with the right bracket
        return ans
    
     # 2_7
class OrderedRecordArray(object):
    def __init__(self, initial_size, max_size):
        self.__a = [None] * initial_size
        self.__nItems = 0
        self.__maxSize = max_size
        self.__key = identity

def __resize(self, new_size):
        new_array = [None] * new_size
        for i in range(self.__nItems):
            new_array[i] = self.__a[i]
        self.__a = new_array

def insert(self, item):
        if self.__nItems >= self.__maxSize:
            new_size = self.__maxSize * 2
            self.__resize(new_size)
            self.__maxSize = new_size

        self.__a[self.__nItems] = item
        self.__nItems += 1


# Prueba de crecimiento 

# incremento fijo
arr_nuevo = OrderedRecordArray(5, 5)
for i in range(10):
    arr_nuevo.insert(i)

print("Lista con estrategia de incremento fijo:")
for i in range(len(arr_nuevo)):
    print(arr_nuevo.get(i))
print()

# multiplicar el tamaño actual
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

