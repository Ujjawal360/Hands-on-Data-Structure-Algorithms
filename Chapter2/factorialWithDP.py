def factorialWithDP(n):
  # base case
  if n == 1:
    return 1

  # memoization
  if n in lookup:
    return lookup[n]
  
  # recursive case
  lookup[n] = n * factorialWithDP(n-1)
  return lookup[n]

lookup = {}
print(factorialWithDP(5))