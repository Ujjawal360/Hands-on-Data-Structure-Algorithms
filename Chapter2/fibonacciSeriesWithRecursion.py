'''
fibonacci series using recursion technique
fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
The current number is sum of the previous two numbers

Base Case:
if n == 0 return 0
if n == 1 return 1
As it always starts with 0 & 1, we can return 0 & 1
-------------------------------------------------------------
So to calculate the fibo series, we need to calculate the fibo series of n-1 and n-2
'''

def fibonacciSeriesWithRecursion(n):
  # base case
  if n == 0: 
    return 0
  if n == 1:
    return 1
  
  # recursive case
  result = fibonacciSeriesWithRecursion(n-1) + fibonacciSeriesWithRecursion(n-2)
  return result

print(fibonacciSeriesWithRecursion(6))
