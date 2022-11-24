def quick_sort(array, start, end):
  '''
    Function To Use Quick-Sort Algorithm As Designed By "StackAbuse"

    Args:
      => array(arr) - Array To Be Sorted
      => start(int) - Starting Position In Array
      => end(int) - End Point For Sorting

    Returns:
      => None
  '''
  
  if start >= end:
      return

  p = partition(array, start, end)
  quick_sort(array, start, p-1)
  quick_sort(array, p+1, end)

def partition(array, start, end):

  '''
    Function That Works In Conjunction With QuickSort, In Order To Sort Sections Of Array

    Args:
      => array(arr) - Array To Sort
      => start(int) - Start Position For Partionning
      => end(int) - End Position To Partition

    Returns:
      => None
  '''
  pivot = array[start]
  low = start + 1
  high = end

  while True:
      # If the current value we're looking at is larger than the pivot
      # it's in the right place (right side of pivot) and we can move left,
      # to the next element.
      # We also need to make sure we haven't surpassed the low pointer, since that
      # indicates we have already moved all the elements to their correct side of the pivot
      while low <= high and array[high] >= pivot:
          high = high - 1

      # Opposite process of the one above
      while low <= high and array[low] <= pivot:
          low = low + 1

      # We either found a value for both high and low that is out of order
      # or low is higher than high, in which case we exit the loop
      if low <= high:
          array[low], array[high] = array[high], array[low]
          # The loop continues
      else:
          # We exit out of the loop
          break

  array[start], array[high] = array[high], array[start]

  return high

