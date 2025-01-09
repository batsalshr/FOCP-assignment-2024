'''
Decrypt question number 5
'''
import random
import string

def encryption():
    '''
    Functionm decrypts question number 5
    '''
    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    message = input("Enter a sentence ")
    encrypted = ""
    position = 0  # Track the position for placing message characters

    # Iterate until the length of the message and add random letters
    while position < len(message):
        encrypted += message[position] 
        print(encrypted)# Add the next character of the message
        position += 1
        for _ in range(interval - 1):
            encrypted += random.choice(string.ascii_lowercase)
    return encrypted, interval

def decryption(encrypted_message, interval):
    decrypted_message = encrypted_message[::interval]
    return decrypted_message

encrypted_message, used_interval = encryption()

# Decrypt the message
decrypted_message = decryption(encrypted_message, used_interval)

# Test the function
encrypted_message, used_interval = encryption()
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval Used: {used_interval}")
print(f"Decrypted Message: {decrypted_message}")

print(encryption.__doc__)