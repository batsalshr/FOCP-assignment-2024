'''
The Unixdiff command compares two files and reports the differences, if any. Write a simple implementation of this that takes two file names as command-line arguments and reports whether or not the two files are the same. (Define "same" as having the same contents.)
'''
# This program checks if the two file are same or not.
f01=input("Enter the name of first file: ")
f02=input("Enter the name of second file: ")
f1=open(f01,'r')
f2=open(f02,'r')

if f1.read()==f2.read():
    print("They are same!!!")
else:
    print("They are different")
