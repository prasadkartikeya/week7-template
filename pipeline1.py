def compose_pipeline(*functions):
    """
    Takes a variable number of unary functions and returns a new function
    that represents the composition of those functions.
    """
    def composed_function(x):
        for func in functions:
            x = func(x)  # Apply each function in order
        return x
    
    return composed_function

# Example usage
def add1(x):
    return x + 1

def square(x):
    return x * x

def halve(x):
    return x / 2

# Define pipelines
pipeline = compose_pipeline(add1, square, halve)
print(pipeline(3))  # Output: 8.0

pipeline2 = compose_pipeline(square, add1, halve)
print(pipeline2(3))  # Output: 5.0