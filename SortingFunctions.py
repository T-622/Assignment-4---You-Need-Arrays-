def sortFunction(array):
  '''
    Function Designed To Take Argument Of Array And Sort It From Smallest To Largest
  '''
  for i in range(len(array)):  # Counter 1 Use Up To Len Of Array
    
    for j in range(i+1,len(array)):  # Second Counter Counts from Last Counter Position To Last Element Of Array
      
      if array[i]>array[j]:          # If Element In Position I, Greater Than That In Position J
        array[i],array[j]=array[j],array[i] # Flip Order Of Elements In Array
        