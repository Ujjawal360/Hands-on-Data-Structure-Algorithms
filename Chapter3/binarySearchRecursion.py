def binarySearchRecursion(arr, target, left, right):
  if left > right:
    return -1 
  mid = int((left + right) / 2)
  if arr[mid] == target:
    return mid
  elif target < arr[mid]:
    return binarySearchRecursion(arr, target, left, mid - 1)
  else:
    return binarySearchRecursion(arr, target, mid + 1, right)

arr = [1, 6, 8, 23, 26, 32, 37, 56, 78, 90, 100]
left = 0
right = len(arr) - 1
print(binarySearchRecursion(arr, 8, left, right))