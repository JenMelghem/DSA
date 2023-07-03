class OrderedRecordArray(object):
    # ...
    
    def find(self, key): # Find index at or just below key
        lo = 0 # in ordered list
        hi = self.__nItems-1 # Look between lo and hi
        while lo <= hi:
            mid = (lo + hi) // 2 # Select the midpoint
            if self.__key(self.__a[mid]) == key: # Did we find it?
                return mid # Return location of item
            elif self.__key(self.__a[mid]) < key: # Is key in upper half?
                lo = mid + 1 # Yes, raise the lo boundary
            else:
                hi = mid - 1 # No, but could be in lower half
        return lo # Item not found, return insertion point instead
    
    def search(self, key):
        idx = self.find(key) # Search for a record by its key
        if idx < self.__nItems and self.__key(self.__a[idx]) == key:
            return self.__a[idx] # and return item if found
    
    def insert(self, item):
        if self.__nItems >= self.__maxSize:
            new_size = self.__maxSize * 2
            self.__resize(new_size)
            self.__maxSize = new_size

        j = self.find(self.__key(item))
        for k in range(self.__nItems, j, -1):
            self.__a[k] = self.__a[k - 1]
        self.__a[j] = item
        self.__nItems += 1
    
    def delete(self, item): # Delete any occurrence
        j = self.find(self.__key(item)) # Try to find the item
        if j < self.__nItems and self.__a[j] == item: # If found,
            self.__nItems -= 1 # One fewer at end
            for k in range(j, self.__nItems): # Move bigger items left
                self.__a[k] = self.__a[k+1]
            return True # Return success flag
        return False # Made it here; item not found

def identity(x):  # The identity function
    return x


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
