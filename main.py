import numpy as np
from ClassFiles import SortingAlgorithms 
from ClassFiles import DataStructures 
          
size = 10
startArray = np.random.randint(10, size = (size))
startArray = list(startArray)
sort = SortingAlgorithms.Sorting()

print(str(startArray) + "\n")
sortedArray = sort.mergeSort(startArray)
print(sortedArray)
