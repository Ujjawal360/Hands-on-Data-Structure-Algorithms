def partition(elements, start, end):
  pivot_index = start 
  pivot = elements[pivot_index]

  while start < end:
      while start < len(elements) and elements[start] <= pivot:
          start+=1

      while elements[end] > pivot:
          end-=1

      if start < end:
          elements[start], elements[end] = elements[end], elements[start]

  elements[pivot_index], elements[end] = elements[end], elements[pivot_index]
  return end

def quickSort(elements, start, end):
  if start < end:
    pi = partition(elements, start, end) # gives partition index
    quickSort(elements, start, pi-1)
    quickSort(elements, pi+1, end)

elements = [11,9,29,7,2,15,28]
quickSort(elements, 0, len(elements) - 1)
print(elements)


"""
# <----> First Steps Quick Sort <---->
def partition(elements):
  pivot_index = 0
  pivot = elements[pivot_index]

  start = 0
  end = len(elements) - 1

  while start < end:
      while start < len(elements) and elements[start] <= pivot:
          start+=1

      while elements[end] > pivot:
          end-=1

      if start < end:
          elements[start], elements[end] = elements[end], elements[start]

  elements[pivot_index], elements[end] = elements[end], elements[pivot_index]

def quickSort(elements):
  partition(elements)

elements = [11,9,29,7,2,15,28]
quickSort(elements)
print(elements)
"""