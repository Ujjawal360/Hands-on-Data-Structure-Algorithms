def quickSort(arr):
  if len(arr) <= 1:
    return arr

  pivot = arr[-1]
  left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to the pivot
  right = [x for x in arr[:-1] if x > pivot]  # Elements greater than the pivot
  return quickSort(left) + [pivot] + quickSort(right)


arr = [56, 12, 9, 23, 90, 86, 67, 73, 89, 7, 1, 3]
print(quickSort(arr))
