'''Write a program that takes a centigrade temperature and displays the equivalent in
fahrenheit. The input should be a number followed by a letter C. The output should
be in the same format.'''

def con_Fahrenheit(temp):
    '''
    This function takes celcius temprature as an arguement as a string and converts it into fahrenheit and prints it with a 'C' at the end.s
    '''
    tempr=temp[0:-1]
    tempr=int(tempr)
    fahrenheit=round((tempr * 9/5) + 32,2)
    print(fahrenheit,'C')


con_Fahrenheit('20C')
print(con_Fahrenheit.__doc__)

