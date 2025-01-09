''' 1 WAP Functions are often used to validate input. Write a function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise. Write a short program to test the function.'''

def accepts(num):
    '''Function that accepts a single
integer as a parameter and returns True if the integer is in the range 0 to 100
(inclusive), or False otherwise.'''

    if num >= 0 and num <= 100:
        print ("True ")
    else:
        print("False")

accepts (100)
accepts (200)
accepts (56)

print(accepts.__doc__)