'''
Write and test a function that takes an integer as its parameter and returns the factors of that integer (A factor is an integer greater than 1 that cannot be produced by multiplying two other integers)
'''

def factor(n):
    '''
    Function that takes an integer as its parameter and returns the factors of that integer
    '''
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
    return factors

# Test the function
print(factor(12))  # Output: [1, 2, 3, 4, 6, 12]
print(factor(24))  # Output: [1, 2, 3, 4, 6, 8, 12, 24]
print(factor(30))  # Output: [1, 2, 3, 5, 6, 10, 15, 30]

print(factor.__doc__)