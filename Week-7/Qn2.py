"""
    Quesntion 2 : 
        Write and test three functions that each take two words (strings) as parameters and return sorted lists (as defined above) representing respectively:
            Letters that appear in at least one of the two words. Letters that appear in both words.
            Letters that appear in either word, but not in both.
"""

# Function 1: Letters that appear in at least one of the two words
def letters_in_either(word1, word2):
    """
    Returns a sorted list of letters that appear in at least one of the two words.
    """
    return sorted(set(word1.lower()) | set(word2.lower()))

# Function 2: Letters that appear in both words
def letters_in_both(word1, word2):
    """
    Returns a sorted list of letters that appear in both words.
    """
    return sorted(set(word1.lower()) & set(word2.lower()))

# Function 3: Letters that appear in either word, but not in both
def letters_in_either_but_not_both(word1, word2):
    """
    Returns a sorted list of letters that appear in either word, but not in both.
    """
    return sorted(set(word1.lower()) ^ set(word2.lower()))

# Testing the functions
word1 = "cheese"
word2 = "bread"

# Displaying the function documentation and results
print("Function Documentation for letters_in_either:")
print(letters_in_either.__doc__)
print("Result:", letters_in_either(word1, word2))

print("\nFunction Documentation for letters_in_both:")
print(letters_in_both.__doc__)
print("Result:", letters_in_both(word1, word2))

print("\nFunction Documentation for letters_in_either_but_not_both:")
print(letters_in_either_but_not_both.__doc__)
print("Result:", letters_in_either_but_not_both(word1, word2))
