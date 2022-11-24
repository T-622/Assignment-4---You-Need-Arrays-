# UTF-8 CRLF
# Done in REPL.IT & Python 3.8.4 32-bit interpreter
# Reproduction without citation is exclusively NOT permitted
# Licensed under GNU GPLv3.0

# Copyright (c) 2022 Tyler Peppy @ OCDSB

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import random
import time
import cpuinfo
import platform, subprocess
from SearchFunctions import *   # Import Custom Lib Defined In Files
from SortingFunctions import *  # Import Custom Lib Defined In Files

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

# Variable declarations
randArray = []
againChoice = 0
arrSize = 0
upperLimit = 0
lowerLimit = 0
index = 0
val = 0
foundTerms = 0
firstPosition = 0
 

def intro():
  '''
    Basic, Text Based Function Taking No Positional Args To Print Intro Data
  '''
  print(BLUE+"______                _                    ")                                            
  print("| ___ \              | |                    ")                                            
  print("| |_/ /__ _ _ __   __| | ___  _ __ ___       ")                                           
  print("|    // _` | '_ \ / _` |/ _ \| '_ ` _ \        ")                                         
  print("| |\ | (_| | | | | (_| | (_) | | | | | |          ")                                      
  print("\_| \_\__,_|_| |_|\__,_|\___/|_| |_| |_|            ")                                    
  print("")                                                                                                                                                               
  print(" _   _                 _                 _____                           _              ")
  print("| \ | |               | |               |  __ \                         | |             ")
  print("|  \| |_   _ _ __ ___ | |__   ___ _ __  | |  \/ ___ _ __   ___ _ __ __ _| |_ ___  _ __  ")
  print("| . ` | | | | '_ ` _ \| '_ \ / _ | '__| | | __ / _ | '_ \ / _ | '__/ _` | __/ _ \| '__| ")
  print("| |\  | |_| | | | | | | |_) |  __| |    | |_\ |  __| | | |  __| | | (_| | || (_) | |    ")
  print("\_| \_/\__,_|_| |_| |_|_.__/ \___|_|     \____/\___|_| |_|\___|_|  \__,_|\__\___/|_|    "+RESET)
  print(MAGENTA+"\nProcessor Info:",cpuinfo.get_cpu_info()['brand_raw'],""+RESET)  # Get Processor Info For User
  print(GREEN+"\nHello User! Welcome to this random number generation program!\nIn Here, You Will Be Asked For:\n\n=> An Upper And Lower Limit For Random Number\n=> A Range To Fill With These Random Numbers\n=> A Search Method\n=> A Search Integer\n\n"+MAGENTA+"In Order, To Generate An Array With Random Numbers, That You \nCan Either Binary, Or Linearly Search For!\nHave Fun!\n"+RESET)
                                                                                      
def playAgain():
  '''
    Simple Play Again Loop Returning True Or False To Continue Running Of Program
    
    Args:
      None
      
    Returns:
      => True
      => False
      Based On User Selection
  '''
  while True:    # Trap User Input In A Loop In Order To Avoid Allowing False Input
    try:
      againChoice = input(YELLOW+"\nWould You Like To Generate A New Array? 'y' or 'n': "+RESET)  # Attempt To Gain User Input
    except ValueError:
      print(RED+"\nYou Didn't Enter A Valid Input! 'y' or 'n'!"+RESET)                  # Throw Out Message On Exception 
    else: 
      if(againChoice == ""):                    # If ENTER Key Is Detected In Text Field
        print(RED+"\nYou Didn't Enter A Valid Input! 'y' or 'n'!"+RESET)
      elif(againChoice in 'yY'):                # If Any Form of Y Is Recieved Return True And Exit
        return True
      elif(againChoice in 'nN'):                # If Any Form Of N Is REcieved Return False And Exit
        print(YELLOW+"\nThanks For Using This Program!"+RESET)  # Thank USer
        return False    
      else:
        print(RED+"\nYou Didn't Enter A Valid Input! 'y' or 'n'!"+RESET)
        
def getArraySize():
  '''
    Text-Based Function Gaining User Input To Get Desired Array Size, Returns None, And Takes None
  '''
  global randArray  # Declare randArray As Usable Elsewhere For Additional Functions
  
  print(GREEN+"------------------------------------------------------------"+RESET)  # Formatting
  
  while True:  # Trap User Input To Avoid Letting False Input By
    try:
      arrSize = int(input(BLUE+"\nHow Many Elements Would You Like In Your Array?: "))  # Prompt For Integer Size To Create Array With
    except ValueError:
      print(RED+"\nYou Didn't Enter A Valid Value!"+RESET)                              # Throw Text On Exception Error To Handle Program Unexpected
    else:
      if(arrSize <= 0):                                                                 # Do Not Allow <= 0 Elements To Be Available
        print(RED+"\nYou Entered A Value Smaller Than Or Equal To Zero!"+RESET)
      if(arrSize >=50000):                                                              # Do Not Allow 50 000 Or More Elements To Conserve Resources
        print(RED+"\nYou Have Entered More Than 20 000! Too Many Elements"+RESET)
      else:
        randArray = [0]*arrSize                                                         # Fill Array With 'arrSize' 0s, Adding arrSize Elements
        print(YELLOW+"\nThe Array Is Now Of Size",len(randArray),"Elements"+RESET)      # Print Current Array Size For User To See Using 'len()'
        break
  print(GREEN+"\n------------------------------------------------------------"+RESET)   # Formatting
  
def fillArray(ll, ul, arrlen):
  '''
    Function That Takes In 3 Positional Args, (3 INTs), For Upper Limit, Lower Limit, And Length Of Array It Is About To Fill

    Args:
      => ll(int) - Lower Limit For Random Number Generation
      => ul(int) - Upper Limit For Random Number Generation
      => arrlen(int) - Length Of Fed Array
      
    Returns:
      => None
  '''
  
  for index in range (0, arrlen):              # Repeat Function For Each Element In The Array (For Length Of Data Struct)
    randArray[index] = random.randint(ll, ul)  # Generate Randint At Position Generated By Incremeing Counter, Between Specified Upper And Lower Limits

def selectSearch():
  '''
    Selection Of Which Search Is To Be Conducted On Array For Search Term
    
    Args:
      None
      
    Returns:
      None
  '''
  while True:
    while True:     # Error-Trap User Input For Selection To Avoid Crashing
      try:
        mode = int(input(YELLOW+"\nWhich Search Mode Do You Desire? 1 For Linear, 2 For Binary: "+RESET))  # Gain An Integer Input For Mode Selection
      except ValueError:
        print(RED+"\nYou Didn't Enter A Number!"+RESET)    # Throw Error On Value Error Exception 
      else:    
        if (mode > 2 or mode < 1):  # If Number Isn't One Or Two, Handle Exception
          print(RED+"\nI Expected A Valid Search Mode!"+RESET)
        else:
          break                     # Valid Input Detected, User May Continue (Input Is One Or Two )
  
    while True:    # Error-Trapping Similar To The Last Where, Integers Are Gathred As Search Terms
      try:
        selection = int(input(GREEN+"\nWhat Is Your Desired Search Term (Integer)?: "))
        print()    # Formatting
        
      except ValueError:
        print(RED+"\nYou Didn't Enter A Number!"+RESET)
      else:
        if (selection > upperLimit or selection < lowerLimit):
          print(RED+"This Value Isn't Within The Valid Range Of Random Numbers!"+RESET)
        elif (mode == 1):  # If A Linear Search Has Been Selected
          print(GREEN+"\n------------------------RESULTS----------------------------"+RESET) # Use sortFunction (SortFunction Library File) To Order The Elements In The Array, Smallest to Largest
          time_start = time.time()         # Begin A Timer For Counting Compute Duration
          linSearch(selection, randArray)  # Use Linear Search Function, And Pass In Our Random Int Array With The Desired Search Term Gathered Before
          time_elapsed = (time.time() - time_start)  # Calculate Compute Time
          if (time_elapsed < 1):
            print(MAGENTA+"Search Took:"+YELLOW,round(time_elapsed,5)*1000,"mSecs"+RESET)  # Print Compute Time In mS
          else:
            print(MAGENTA+"Search Took:"+YELLOW,round(time_elapsed,5),"Secs"+RESET)  # Print Compute Time In mS
          print(GREEN+"-----------------------------------------------------------"+RESET)
          break
        elif (mode == 2):                      # A Binary Search Has Been Specified
          print(GREEN+"\n------------------------RESULTS----------------------------"+RESET)  
          quick_sort(randArray, 0, len(randArray)-1)  # Use SortFunction To Sort Array From Smallest To Largest 
          time_start = time.time() # Start Compute Time Timer
          binSearch(selection, randArray, len(randArray)-1, 0)  # Use BinSearch Function To Binary Search, With Key Term, Array, and Start / End Points
          time_elapsed = (time.time() - time_start)             # Compute Time Calculation
          if (time_elapsed < 1):
            print(MAGENTA+"Search Took:"+YELLOW,round(time_elapsed,5)*1000,"mSecs"+RESET)  # Print Compute Time In mS
          else:
            print(MAGENTA+"Search Took:"+YELLOW,round(time_elapsed,5),"Secs"+RESET)  # Print Compute Time In mS
          print()
          print(GREEN+"------------------------------------------------------------"+RESET)
          break
          
    while True:
      try:
        selection = input(YELLOW+"\nWould You Like To Search Again 'y' or 'n'?: "+RESET)
      except ValueError:
        print(RED+"\nInvalid Value Entered!"+RESET)
      else:
        if (selection == ""):
          print(RED+"\nInvalid Value Entered!"+RESET)
        elif (selection in 'yY'):
          print(GREEN+"\nRunning Again..."+RESET)
          break
        elif (selection in 'nN'):
          return None
        else:
          print(RED+"\nInvalid Value Entered!"+RESET)
          
def getNum(mode):
  '''
    Function That Gains User Upper Or Lower Limit Based On Selected Mode

    Args:
      => mode(int), 1 or 2, for Lower Limit Or Upper Limit

    Returns:
      => Upper Limit - Mode 2
      => Lower Limit - Mode 1
  '''
  strings = ""
  if (mode == 1):
    strings = "Lower"
  elif(mode == 2):
    strings = "Upper"

  while True:     # Use Error-Trapped Loop To Gain Lower Limit For Random Int Generation
    try:
      limit = int(input(BLUE+"\nPlease Enter A "+strings+" Limit For Random Number Generation: "+RESET))  # Gather Expected Integers
    except ValueError:
      print(RED+"\nYou Didn't Enter A Valid Integer Value!"+RESET)                                       # Handle Exceptions
    else:
      if (mode == 1):
        if (limit < 0):
          print(RED+"\nValue Is Too Small!"+RESET)
        else:
          return limit
      elif (mode == 2):
        if (limit < lowerLimit):     # Disallow Upper Limits Smaller Than The Lower Ones
          print(RED+"\nThe Entered Upper Limit Is Smaller Than Lower Limit!"+RESET)
        elif (limit == lowerLimit):  # Disallow Equal Limits (Avoid Complexity)
          print(RED+"\nThe Entered Upper Limit Is Equal To The Lower Limit!"+RESET)
        else:
          return limit
  
intro()
while True: 
  getArraySize()  # Get The Desired Array Size
  
  lowerLimit = getNum(1)  # Get Lower Limit
  upperLimit = getNum(2)  # Get Upper Limit
        
  fillArray(lowerLimit, upperLimit, len(randArray))  # Fill Array With Recently Gathered Random Numbers
  selectSearch()  # Select Search Method
  
  if (playAgain() == False):  # Run Play Again Loop To Prompt User To Continue Or Not
    break                     # Break Out Of Main Loop On Exit Command And Break
  else:
    print(GREEN+"\nContinuing!"+RESET)  # Continue On Correct Command

  
    