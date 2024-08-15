# Assignment 7

Write functions for the following questions in a file named `main.py`.

## Question 1: Function Composition Pipeline

Write a function named `compose_pipeline` that takes a variable number of unary functions (functions that take a single argument) as input and returns a new function that represents the composition of those functions. The composed function should apply the input functions in the order they are passed.

### Requirements:

1. The returned function should take a single argument and apply each function in the pipeline to it in sequence.
2. The order of function application is from left to right (i.e., the first function is applied first, then the second function, and so on).
3. The `compose_pipeline` function should handle an arbitrary number of input functions.

### Illustration

```python
def add1(x):
    return x + 1

def square(x):
    return x * x

def halve(x):
    return x / 2

pipeline = compose_pipeline(add1, square, halve)
print(pipeline(3))  # First: add1(3) -> 4, then: square(4) -> 16, finally: halve(16) -> 8.0

pipeline2 = compose_pipeline(square, add1, halve)
print(pipeline2(3))  # First: square(3) -> 9, then: add1(9) -> 10, finally: halve(10) -> 5.0
```

## Question 2: Calculating Exponential Power Sequence

Write a function named `power_sequence` that takes an integer `n` and a positive integer `k` as input and returns the sum of the first `k` powers of `n` (i.e., \( n^1 + n^2 + ... + n^k \)).

### Illustration

```python
print(power_sequence(2, 4))  # Prints 2^1 + 2^2 + 2^3 + 2^4 = 2 + 4 + 8 + 16 = 30

print(power_sequence(3, 3))  # Prints 3^1 + 3^2 + 3^3 = 3 + 9 + 27 = 39

print(power_sequence(5, 2))  # Prints 5^1 + 5^2 = 5 + 25 = 30
```
