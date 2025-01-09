'''
 Modify your previous program so that the password must be between 8 and 12 characters (inclusive) long.
'''
while True:
    password=input("Enter a Password: ")
    password1=input("Enter Password again: ")
    if len(password)<=12 and len(password)>=8:
        break;
if password==password1:
    print("Password Set")
else:
    print("Error!The passwords doesnt match")