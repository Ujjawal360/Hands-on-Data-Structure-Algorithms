'''
Factorial calculation using recursion technique
Base Case:
factorial of 1 -> 1
-------------------------------------------------------------
factorial of rest of numbers: lets say 5 -> 5 * 4 * 3 * 2 * 1
or 5 -> 5 * factorial(4)
or 5 -> 5 * 4 * factorial(3)
or 5 -> 5 * 4 * 3 * factorial(2)
or 5 -> 5 * 4 * 3 * 2 * factorial(1)
or n -> n * factorial(n-1)
'''

def factorialWithRecursion(n):
  if n == 1:
    return 1
  else:
    result = n * factorialWithRecursion(n-1)
    return result

print(factorialWithRecursion(5))