'''
The Unixspellcommand is a simple spell-checker.It prints out all the words in a text file that are not found in a dictionary. Write and test an implementation of this, that takes a file name as a command-line argument.
Note: You may want to simplify the program at first by testing with a text file that does not contain any punctuation. A complete version should obviously be able to handle normal files, with punctuation.
Another Note: You will need a list of valid words. Linux users will already have one (probably in /usr/share/dict/words). It is more complicated,as usual, for Windows users. Happily, there are several available on GitHub.
'''
#This program prints the words that are not found in the dictionary.
filename=input("Enter the filename: ")
f1=open(filename,'r')
dict={'key':['the','and','python','of','to','be']}
for x in f1.readlines():
    for y in x.split(' '):
        if y in dict['key']:
            pass
        else:
            print(y)