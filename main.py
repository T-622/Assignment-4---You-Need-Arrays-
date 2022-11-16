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
import numpy

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

def playAgain():
  '''
    Simple Play Again Loop Returning True Or False To Continue Running Of Program
  '''
  while True:
    try:
      againChoice = input(YELLOW+"\nWould You Like To Play Again? 'y' or 'n': "+RESET)
    except ValueError:
      print(RED+"\nYou Didn't Enter A Valid Input! 'y' or 'n'!"+RESET)
    else: 
      if(againChoice == ""):
        print(RED+"\nYou Didn't Enter A Valid Input! 'y' or 'n'!"+RESET)
      elif(againChoice in 'yY'):
        return True
      elif(againChoice in 'nN'):
        print(YELLOW+"\nThanks For Using This Program!"+RESET)
        return False    

def getArraySize():
  '''
    Text-Based Function Gaining User Input To Get Desired Array Size
  '''
  global randArray
  print(GREEN+"------------------------------------------------------------"+RESET)
  while True:
    try:
      arrSize = int(input(BLUE+"\nHow Many Elements Would You Like In Your Array?: "))
    except ValueError:
      print(RED+"\nYou Didn't Enter A Valid Value!"+RESET)
    else:
      if(arrSize <= 0):
        print(RED+"\nYou Entered A Value Smaller Than Or Equal To Zero!"+RESET)
      if(arrSize >=5001):
        print(RED+"\nYou Have Entered More Than 5000! Too Many Elements"+RESET)
      else:
        randArray = [0]*arrSize # Fill Array With 0s, Adding arrSize Elements
        print(YELLOW+"The Array Is Now Of Size",len(randArray),"Elements"+RESET)
        break
  print(GREEN+"\n------------------------------------------------------------"+RESET)
  
def fillArray(ll, ul, arrlen):
  '''
    Function That Takes In 3 Positional Args, (3 INTs), For Upper Limit, Lower Limit, And Length Of Array It Is About To Fill, To Fill Each Position Of An Index With A Random Number
  '''
  for index in range (0, arrlen):
    randArray[index] = random.randint(ll, ul)

def binSearch(key, array):
  '''
    Function To Effectively Binary Search An Array Of Elements For All Iterations Of A Key. Returns First Term Or No Term
  '''
  low = 0
  high = len(array)-1
  while (low <= high):
    middleTerm = low + (high-low) // 2
    if(array[middleTerm] == key):
      print(GREEN+"\nKey Of",key,"Found At Position",middleTerm+1,"In Array!"+RESET)
      return None
    elif (array[middleTerm] > key):
      high = middleTerm - 1
    else:
      low = middleTerm + 1
  print(RED+"\nKey Of",key,"Was Not Found In Array!"+RESET)
  return None

def linSearch(searchTerm,arrays):
  global val
  '''
    Function To Linearly Search For All Iterations Of Search Term In Array
  '''
  for x in range (0, len(arrays)):
    if (arrays[x] == searchTerm):
      val += 1
  print(GREEN+"\n",val,"Valid Iterations Of Key:",searchTerm,"Found In",len(arrays),"Items"+RESET)

def selectSearch():
  '''
    Selection Of Which Search Is To Be Conducted On Array For Term
  '''
  while True:
    try:
      mode = int(input(YELLOW+"\nWhich Search Mode Do You Desire? 1 For Linear, 2 For Binary: "+RESET))
    except ValueError:
      print(RED+"\nYou Didn't Enter A Number!"+RESET)
    else:
      if (mode > 2 or mode < 1):
        print(RED+"\nI Expected A Valid Search Mode!"+RESET)
      else:
        break

  while True:
    try:
      selection = int(input(GREEN+"\nWhat Is Your Desired Search Term (Integer)?: "))
    except ValueError:
      print(RED+"\nYou Didn't Enter A Number!"+RESET)
    else:
      if (mode == 1):
        time_start = time.time()
        linSearch(selection, randArray)
        time_elapsed = (time.time() - time_start)
        print(GREEN+"\nSearch Took:",time_elapsed,"seconds"+RESET)
        break
      else:
        randArray.sort()
        time_start = time.time()
        binSearch(selection, randArray)
        time_elapsed = (time.time() - time_start)
        print(GREEN+"\nSearch Took:",time_elapsed,"seconds"+RESET)
        print(randArray)
        break
        

  return None
while True:
  
  getArraySize()
  
  while True:
    try:
      lowerLimit = int(input(BLUE+"\nPlease Enter A Lower Limit For Random Number Generation: "+RESET))
    except ValueError:
      print(RED+"\nYou Didn't Enter A Valid Integer Value!"+RESET)
    else:
      break
      
  while True:
    try:
      upperLimit = int(input(BLUE+"\nPlease Enter An Upper Limit For Random Number Generation: "+RESET))
    except ValueError:
      print(RED+"\nYou Didn't Enter A Valid Integer Value!"+RESET)
    else:
      if (upperLimit < lowerLimit):
        print(RED+"\nThe Entered Upper Limit Is Smaller Than Lower Limits!"+RESET)
      elif (upperLimit == lowerLimit):
        print(RED+"\nThe Entered Upper Limit Is Smaller Than Lower Limits!"+RESET)
      else:
        break
        
  fillArray(lowerLimit, upperLimit, len(randArray))
  selectSearch()
  if (playAgain() == False):
    break
  else:
    print(GREEN+"\nContinuing!"+RESET)

  
    