import numpy as np

# Arrays
class Sorting ():
    # def __init__(self array):
    #     
    
    def mergeSort(self, array):
        if(len(array) > 1):
            
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]
            
            self.mergeSort(left)
            self.mergeSort(right)
            
            i = j = k = 0
            while(i < len(left) and j < len(right)):
                if(left[i] <= right[j]):
                    array[k] = left[i]
                    i += 1
                    
                else:
                    array[k] = right[j]
                    j += 1
                k += 1
                
            while(i < len(left)):
                array[k] = left[i]
                i += 1
                k += 1
                
            while(j < len(right)):
                array[k] = right[j]
                j += 1
                k += 1
        return array         
    
        
        
    
      
    

    def findSecondMinimum(self): # NEED TO IMPLEMENT
        secondMin = -1
        print(self.nums)
        
        return secondMin
    
        
        
      
size = 10
startArray = np.random.randint(10, size = (size))
startArray = list(startArray)
print(str(startArray) + "\n")
sort = Sorting()
sortedArray = sort.mergeSort(startArray)
print(sortedArray)
