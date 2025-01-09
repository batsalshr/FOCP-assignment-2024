'''Write a function that accepts a postive integer  as a parameter and then returns a representation that number in binary(base 2)'''

rem = 0
lst=[]
def binary(num):
    while num!=0:
        rem = num%2
        num = num//2
        lst.append(rem)
    print(lst[::-1])
num = int(input("enter a postive integer "))

binary(num)
        

