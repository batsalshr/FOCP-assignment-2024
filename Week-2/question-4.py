'''
A kindly teacher wishes to distribute a tub of sweets between her pupils. She will first count the sweets and then divide them according to how many pupils attend that day. Write a program that will tell the teacher how many sweets to give to each pupil, and how many she will have left over.
'''
pupils=int(input("Enter the number of pupils: "))
chocolate=int(input("Enter the number of chocolate: "))
count=0
leftover=0
while True:
    if chocolate>=pupils:
        count+=1
        chocolate-=pupils
    else:
        leftover=chocolate
        break
print(f"Each pupil will recieve {count} chocolate and {leftover} leftover.")