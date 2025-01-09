'''Write a function that has a single string as its parameter, and returns the number of
uppercase letters, and the number of lowercase letters in the string. Test the
function with a short program.'''

def case(word):
    '''
    This function takes a string as an arguement and returns the count of Upper Case and Lower Case in the string.
    '''
    countU=0
    countL=0
    for x in word:
        if x.upper() == x:
            countU=countU+1
        elif x.lower() == x:
            countL=countL+1
    print(f"There are {countU} Upper Case Letters and {countL} Lower Case Letters")


case('BaTsAl')
print(case.__doc__)