'''
Modify your program a final time so that it executes until the user successfully chooses a password. That is, if the password chosen fails any of the checks, the program should return to asking for the password the first time.
'''

BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
while True:
    password=input("Enter a Password: ")
    password1=input("Enter Password again: ")
    if len(password)<=12 and len(password)>=8:
        if password not in BAD_PASSWORDS:
            break;

if password==password1:
    print("Password Set")
else:
    print("Error!The passwords doesnt match")