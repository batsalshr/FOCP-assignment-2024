'''
Computers are commonly used in encryption. A very simple for of encryption(more accuratley "obfuscation") would beremove the spaces from a message and revers the resulting string. Write and test a function that takes strings containing a message and "encrypt" it in this way
'''

def check(word):
    '''
    Function that takes strings containing a message and "encrypt" it in this way
    '''
    word = word.replace(' ', '' )
    word = word[::-1]
    print(word)

# Test the function
check("H  e l      l o Wo r l  d ")  # Output: dlroW olleH
check("P y t h on i s fun")  # Output: nuf si nohtyP

print(check.__doc__)
