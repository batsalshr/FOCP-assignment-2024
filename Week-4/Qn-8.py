'''Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean.'''

def check():
    '''Function processes any number of values. The input
terminates when the user just pressed "Enter"'''
    lst = []
    while True : 
        z = input("Enter a number ")
        if z == '':
            break
        lst.append(z)
    print(lst)
check ()
print(check.__doc__)