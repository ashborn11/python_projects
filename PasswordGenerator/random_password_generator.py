import string
import random

#list of characters that can be included in the password
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like the password to be? "))

    #shuffling the list of characters
    random.shuffle(characters)
    
    password = []

    #randomly selecting characters from the list in prefered length 
    for x in range(password_length):
        password.append(random.choice(characters))

    password = "".join(password)
    
    print("Password : " + password)

choice = input("Do u want to create a password? [Y/N] ")

if choice.lower() == 'y':
    generate_password()
elif choice.lower() == 'n':
    print("Program Ended")
    exit()
else:
    print("Invalid Input, please input [y] or [N]")
    exit()