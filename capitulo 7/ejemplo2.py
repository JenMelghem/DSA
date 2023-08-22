class Quicksort:
    def quicksort_sketch(self, arr, lo=0, hi=None, key=lambda x: x):
        if hi is None:
            hi = len(arr) - 1
        if lo >= hi:
            return

        pivot = self.choosePivot(arr, lo, hi)
       

        hipart = self.partition(arr, pivot, lo, hi, key)

        self.quicksort_sketch(arr, lo, hipart - 1, key)
        self.quicksort_sketch(arr, hipart, hi, key)

    def choosePivot(self, arr, lo, hi):
        return arr[hi]  #  último elemento del arreglo como pivote

    def partition(self, arr, pivot, lo, hi, key):
        while lo <= hi:
            while lo <= hi and key(arr[lo]) < key(pivot):
                lo += 1
            while lo < hi and pivot < key(arr[hi]):
                hi -= 1
            if lo >= hi:
                return lo
            arr[lo], arr[hi] = arr[hi], arr[lo]
            lo, hi = lo + 1, hi - 1
        return lo


print ("Q U I C K S O R T\n")
arr = [8, 3, 1, 5, 2, 4, 7, 6]
print (arr)
quicksort = Quicksort()
quicksort.quicksort_sketch(arr)

print("\nArreglo ordenado:", arr)
