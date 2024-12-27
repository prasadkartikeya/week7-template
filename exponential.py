def power_sequence(n, k):
    """
    Calculates the sum of the first k powers of n.
    
    Args:
        n (int): The base number.
        k (int): The number of powers to calculate (must be positive).
    
    Returns:
        int: The sum of the first k powers of n.
    """
    return sum(n ** i for i in range(1, k + 1))

# Example usage
print(power_sequence(2, 4))  # Output: 30 (2^1 + 2^2 + 2^3 + 2^4 = 2 + 4 + 8 + 16 = 30)
print(power_sequence(3, 3))  # Output: 39 (3^1 + 3^2 + 3^3 = 3 + 9 + 27 = 39)
print(power_sequence(5, 2))  # Output: 30 (5^1 + 5^2 = 5 + 25 = 30)