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