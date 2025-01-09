'''
The Unixwccommand counts the number of lines, words,and characters in a file. Write an implementation of this that takes a file name as a command-line argument, and then prints the number of lines and characters.
Note: Linux (and Mac) users can use the "wc" commandto check the results of their implementation.
'''
# This program prints the number of line, words and character in a file
filename=input("Enter the name of the file: ")
f1=open(filename,'r')
linecount=0
wordcount=0
charactercount=0
for x in f1.readlines():
    linecount+=1
    for y in x.split(' '):
        wordcount+=1
        for z in y:
            charactercount+=1

print("The number of lines in this files is",linecount)
print("The number of word in this files is",wordcount)
print("The number of character in this files is",charactercount)
