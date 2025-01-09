'''
Write and test a function that determines if a given integer is a prime number. A prime number is an integer greater than 1 that cannot be produced by multiplying two other integers
'''

def is_prime(n):
    '''
    Function that determines if a given integer is a prime number
    '''
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
print(is_prime(2))  # Output: True
print(is_prime(4))  # Output: False
print(is_prime(13))  # Output: True
print(is_prime(15))  # Output: False

print(is_prime.__doc__)