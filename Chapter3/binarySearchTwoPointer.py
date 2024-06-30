def binarySearchTwoPointer(arr, target): 
  # should return the index of the element in the array if founded, otherwise -1
  left = 0
  right = len(arr) - 1
  
  while left <= right:
    mid = int((left + right) / 2)
    if arr[mid] == target:
      return mid
    elif target > arr[mid]:
      left = mid + 1
    else:
      right = mid - 1
  return -1


arr = [1, 6, 8, 23, 26, 32, 37, 56, 78, 90, 100]
print(binarySearchTwoPointer(arr, 26))