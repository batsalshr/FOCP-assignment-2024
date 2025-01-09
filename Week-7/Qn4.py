"""
    Question 4 : 
        One approach to analysing some encrypted data where a substitution is suspected is frequency analysis. A count of the different symbols in the message can be used to identify the language used, and sometimes some of the letters. In English, the most common letter is "e", and so the symbol representing "e" should appear most in the encrypted text.
            Write a program that processes a string representing a message and reports the six most common letters, along with the number of times they appear. Case should not matter, so "E" and "e" are considered the same.
"""
def frequency_analysis(message):
    """
    Analyzes a string to identify the six most common letters and their frequencies.
    Ignores case and counts letters only (ignoring non-alphabetic characters).
    Reports the letters and their counts in descending order of frequency.
    """
    # Initialize a dictionary for letter frequencies
    letter_counts = {chr(letter): 0 for letter in range(ord('a'), ord('z') + 1)}

    # Normalize the message to lowercase and count only letters
    for char in message.lower():
        if char.isalpha():
            letter_counts[char] += 1

    # Sort the dictionary by frequency in descending order and extract the top six
    sorted_letter_counts = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)
    top_six = sorted_letter_counts[:6]

    return top_six

# Example usage
print("Function Documentation:")
print(frequency_analysis.__doc__)

# Input message for analysis
message = input("Enter a sentence ")
result = frequency_analysis(message)

# Display the results
print("\nSix most common letters and their frequencies:")
for letter, count in result:
    print(f"{letter}: {count}")
