The main algorithmic patterns in computer Science are:
* Recursion

* Dynamic Programming
  
* Divide and Conquer Strategy

* Greedy Approach

---------------------------------
**Recursion**

A recursive algorithm calls itself repeatedly in order to solve the problem until a certain condition is fulfilled. A recursive function can be in an infinite loop; therefore, it is required that each recursive function adheres to certain properties. At the core of a recursive function are two types of cases:

1. Base cases: These tell the recursion when to terminate, meaning the recursion will be stopped once the base condition is met
2. Recursive cases: The function calls itself recursively, and we progress toward achieving the base criteria.

**In the dynamic approach, we divide a given problem into smaller sub-problems. In recursion also, we divide the problem into sub-problems. However, the difference between recursion and dynamic programming is that similar sub-problems can be solved any number of times, but in dynamic programming, we keep track of previously solved sub-problems**

Two Examples of Recursion:
* Factorial with recursion technique: [factorial calculation using pure recursion](factorialWithRecursion.py)
* Fibonacci Series with recursion technique: [fibonacci series calculation using pure recursion](fibonacciSeriesWithRecursion.py)

If these same problems were to solve using **dynamic programming** then, we would have to make sure that intermediate results are store in some data structure so that we don't end up calculating computations multiple times after it is done the first time.

* Factorial with dynamic programming: [factorial calculation using pure recursion](factorialWithDP.py)
* Fibonacci Series with dynamic programming: [fibonacci series calculation using pure recursion](fibonacciSeriesWithDP.py)

