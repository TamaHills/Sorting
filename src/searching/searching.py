# STRETCH: implement Linear Search				
def linear_search(arr, target):
  for index in range(len(arr)):
    if arr[index] == target:
      return index

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):

  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr)-1

  while high > low:
    mid = high // 2
    if target == arr[mid]:
      return mid
    elif target > arr[mid]:
      low = mid
    elif target < arr[mid]:
      high = mid

  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2
  print(arr)
  if len(arr) == 0:
    return -1 # array empty
  elif target == arr[middle]:
    return middle
  elif target > arr[middle]:
    return binary_search_recursive(arr[middle:], target, middle, high)
  elif target < arr[middle]:
    return binary_search_recursive(arr[:middle], target, low, middle)