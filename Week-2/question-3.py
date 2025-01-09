'''
The Head of Computing at the University of Poppleton is tasked with dividing a group of students into lab groups. A lab group is usually 24 students, but this is sometimes varied to create groups of similar size. Write a program that prompts for the number of students and group size, and then displays how many groups will be needed and how many will be left over in a smaller group.
How many students? 113
Required group size? 22
There will be 5 groups with 3 students left over.
For bonus credit, see if you can fix the grammar in the output. So if there were 101 students in groups of 20 the output would be:
There will be 5 groups with 1 student left over.
'''
num=int(input("How many students? "))
size=int(input("Required group size? "))
count=0
leftover=0
while True:
    if num>=size:
        count+=1
        num-=size
    else:
        leftover=num
        break
if count<2:
    if leftover<2:
        print(f"There will be {count} group and {leftover} student left over.")
    else:
        print(f"There will be {count} group and {leftover} students left over.")
else:
    if leftover<2:
        print(f"There will be {count} groups and {leftover} student left over.")
    else:
        print(f"There will be {count} groups and {leftover} students left over.")
