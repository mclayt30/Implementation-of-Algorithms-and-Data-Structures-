import numpy as np
from ClassFiles import SortingAlgorithms 
    

def findSecondMinimum(self): # NEED TO IMPLEMENT
    secondMin = -1
    print(self.nums)
    
    return secondMin

        
        
      
size = 10
startArray = np.random.randint(10, size = (size))
startArray = list(startArray)
print(str(startArray) + "\n")
sort = SortingAlgorithms.Sorting()
sortedArray = sort.mergeSort(startArray)
print(sortedArray)
