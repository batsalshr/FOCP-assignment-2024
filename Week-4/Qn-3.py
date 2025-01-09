'''Modify your "greetings" program so that the first letter of the name entered is
always in uppercase with the rest in lowercase. This should happen even if the user
entered their name differently. So if the user entered arthur, ARTHUR, or even
arTHur the name should be displayed as Arthur.'''

def hello(val):
    '''
    This function takes a string as an argument and prints it in Title Case.
    '''
    values=''
    for x in range(len(val)):
        if x == 0:
            values=values+val[x].upper()
        else:
            values=values+val[x].lower()
    print(values)

    # print(val.title())
hello('batsal')
hello('BATSAL')
hello('BaTsaL')

print(hello.__doc__)
