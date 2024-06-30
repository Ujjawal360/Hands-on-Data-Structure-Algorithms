def fibonacciSeriesWithDP(n):
  # base case
  if n == 0:
    return 0
  if n == 1:
    return 1

  # memoization
  if n in lookup:
    return lookup[n]

  # recursive case
  lookup[n] = fibonacciSeriesWithDP(n-1) + fibonacciSeriesWithDP(n-2)
  return lookup[n]


lookup = {}
print(fibonacciSeriesWithDP(8))