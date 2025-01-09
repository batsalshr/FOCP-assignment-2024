"""
    Question 1: 
        Write and test a function that takes a string as a parameter and returns a sorted list of all the unique letters used in the string. 
        So, if the string is cheese, the list returnedshouldbe['c', 'e', 'h', 's'].
"""

def unique_sorted_letters(input_string):
    """
    Takes a string as input and returns a sorted list of unique letters.
    Non-alphabetic characters are ignored, and the function is case-insensitive.
    """
    
    letters = [char.lower() for char in input_string if char.isalpha()]
    return sorted(set(letters))

# Display the function's documentation using __doc__
print("Function Documentation:")
print(unique_sorted_letters.__doc__)

# Example usage
test_input = input("Enter a word ")
result = unique_sorted_letters(test_input)
print("Sorted unique letters:", result)
