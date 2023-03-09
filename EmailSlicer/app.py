
def slicer():
    print("")
    print("Welcome to the email slicer")
    print("---------------------------")

    email_input = input("Enter your email address : ")
    print("")
    
    (username,domain) = email_input.split("@")
    (domain,extension) = domain.split(".")

    print("Username : ",username)
    print("Domain : ",domain)
    print("Extension : ",extension)
    print("")

while True:
    slicer()
    choice = input("End the program?[Y/N]  ")
    if choice.lower() == "y":
        exit()



