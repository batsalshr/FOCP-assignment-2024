'''
The Unixgrepcommand searches a file and outputs the lines in the file that contain a certain pattern. Write an implementation of this. It will take two command-line arguments: the first is the string to look for, and the second is the file name. The output should be the lines in the file that contain the string.
'''
# This program searches the line with specific character
filename=input("Enter the name of the file: ")
f1=open(filename,'r')
word=input("Enter the word that you want to search: ")
for x in f1.readlines():
    if word in x:
        print(x)


