'''Write a program that reads 6 temperatures (in the same format as before), and
displays the maximum, minimum, and mean of the values.
Hint: You should know there are built-in functions for max and min. If you hunt, you
might also find one for the mean.'''

def check(a):
    '''This function reads 6 temperatures (in the same format as before), and displays that maximum, and mean of the values'''
    print(min(a))
    print(max(a))
    print(sum(a)/len(a))

a=[]
for x in range(6):
    a.append(float(input("Enter temperature: ")))
check(a) 
print(check.__doc__)
