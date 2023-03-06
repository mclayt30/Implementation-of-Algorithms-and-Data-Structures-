
class Sorting:
    # def __init__(self, array):
    #     self.array = array
    #     return
    
    def __init__(self):
        return
             
    
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
    
        
        
    