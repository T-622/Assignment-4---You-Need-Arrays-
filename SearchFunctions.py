MAGENTA = "\u001b[35m"
BLACK = "\033[0;30m"
YELLOW = "\u001b[33m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
RESET = "\u001b[0m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"



def binSearch(key, array, high, low):
  '''
    Function To Effectively Binary Search An Array Of Elements For All Iterations Of A Key. Returns First Term Or No Term
  '''
  positions = []
  currIndex = 0
  iterations = 0
  
  if low <= high:
 
    mid = (high + low) // 2
  
    if array[mid] < key:   # If Current Positional Returns Value Smaller Than Key
      return binSearch(key, array, high, mid+1) # Lowpoint Moved To Start Of Right-Hand Sector Of Array, Eliminating Values On Left Side
      print("Searching Right Side")
  
    elif array[mid] > key: # If Current Positional Return Value Larger Than Key
      return binSearch(key, array, mid-1, low) # High Mark Moved To End Of Left-Hand Sector Of Array, Eliminating Values On Right Side
      print("Searching Left Side")
  
    else:                        # If An Iteration Of Number Is Detected
      if ((mid - 1) < 0):            # If Current Index-1 Is Smaller Than Zero, And Before Statements Indicate Our Midpoint Isn't Smaller Or Bigger Than Key, This Must Be Our First Iteration
        currentIndex = mid
        print(MAGENTA+"\nFirst Match Token Found In Index:",mid,""+RESET)
        for x in range(mid, len(array)):
          if (array[currentIndex] == key):
            iterations += 1
            positions.append(currentIndex)
          elif (array[currentIndex+1] != key):
            break
          currentIndex += 1
          
        print(GREEN+"Iterations Found!",iterations,"Total, For Match Of Key",key,""+RESET)
        return mid
      if (array[mid - 1] != key):  # If The Current Value-1 Is Not The Key, We Know We Have The Required Value
        currentIndex = mid
        print(MAGENTA+"\nFirst Match Token Found In Index:",mid,""+RESET)
        for x in range(mid, len(array)):
          if (array[currentIndex] == key):
            iterations += 1
            positions.append(currentIndex)
          elif (array[currentIndex+1] != key):
            break
          currentIndex += 1
          
        print(GREEN+"Iterations Found!",iterations,"Total, For Match Of Key",key,""+RESET)
        print(GREEN+"Positions Found:",positions,""+RESET)
        return mid
      return binSearch(key, array, mid-1, low) # If We Are Able To Have Iterations Of Our Key Before The Current Value, We Know The High Mark Needs To Move Back  
  print(RED+"\nValue Not Found In Range!"+RESET)
  return -1

def linSearch(searchTerm,arrays):
  global val
  '''
    Function To Linearly Search For All Iterations Of Search Term In Array
  '''
  positions = []
  firstIndex = 0
  val = 0
  for x in range (0, len(arrays)):
    if (firstIndex == 0 and arrays[x] == searchTerm):
      firstIndex = x
      
    if (arrays[x] == searchTerm):
      val += 1
      positions.append(x)
  if(val != 0):  # If A Possible Result Has Been Found    
    print(MAGENTA+"\nFirst Match Token Found In Index:",firstIndex,""+RESET)
    print(GREEN+"Iterations Found!",val,"Total, For Match Of Key",searchTerm,""+RESET)
    print(GREEN+"Positions Found:",positions,""+RESET)
  else:
    print(RED+"\nValue Not Found In Range!"+RESET)
