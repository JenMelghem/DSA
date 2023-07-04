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
            
            # El nuevo tamaño puede ser un incremento fijo o un múltiplo del tamaño actual.
            new_size = self.__maxSize * 2
            self.__resize(new_size)
            self.__maxSize = new_size
