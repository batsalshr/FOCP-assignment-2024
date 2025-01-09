'''
Another way to hide a message is to include the letters that make it up within seemingly random text. The letters of the message might be every fifth character, for example. Write and test a function that does such encryption. It should randomly generate an interval (between 2 and 20), space the message out accordingly, and should fill the gaps with random letters. The function should return the encrypted message and the interval used.
For example, if the message is "send cheese", the random interval is 2, and for clarity the random letters are not random:
Send Cheese
s e n d c h e e s e
sxe e n n n n n n n n n n n n n
'''
import random
import string

def encryption():
    '''
     Encrypts a message by spacing out its characters with random letters, 
    using a randomly generated interval between 2 and 20.
    
    The function randomly selects an interval and then inserts random letters 
    in between the characters of the original message. The function returns 
    the encrypted message and the interval used.
    '''
    # Generate a random interval between 2 and 20
    interval = random.randint(2, 20)
    message = "send cheese"
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


# Test the function
encrypted_message, used_interval = encryption()
print(f"Encrypted Message: {encrypted_message}")
print(f"Interval Used: {used_interval}")

print(encryption.__doc__)


