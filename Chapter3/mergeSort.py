def mergeSort(arr):
  # base case
  if len(arr) == 1:
    return arr

  # divide the array into two halves
  mid = int(len(arr) / 2)
  half_a = arr[:mid]
  half_b = arr[mid:]

  # recursively divide the array till a single element
  recursive_half_a = mergeSort(half_a)
  recursive_half_b = mergeSort(half_b)
  
  # merge the two halves into sorted fashion
  return merge(recursive_half_a, recursive_half_b)
  
def merge(firstArr, secondArr):
  merged_array = []
  firstArr_pointer = secondArr_pointer = 0
  while firstArr_pointer < len(firstArr) and secondArr_pointer < len(secondArr):
    if firstArr[firstArr_pointer] < secondArr[secondArr_pointer]:
      merged_array.append(firstArr[firstArr_pointer])
      firstArr_pointer += 1
    else:
      merged_array.append(secondArr[secondArr_pointer])
      secondArr_pointer += 1
  
# if there are elements left in the first half, add them to the merged array
  while firstArr_pointer < len(firstArr):
    merged_array.append(firstArr[firstArr_pointer])
    firstArr_pointer += 1

# if there are elements left in the second half, add them to the merged array
  while secondArr_pointer < len(secondArr):
    merged_array.append(secondArr[secondArr_pointer])
    secondArr_pointer += 1
  
  return merged_array

arr = [56, 23, 89, 12, 34, 90, 67, 45, 1, 0, -1, -5]
print(mergeSort(arr))