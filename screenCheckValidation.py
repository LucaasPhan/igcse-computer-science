initPassword = input("Enter your password: ")
print("Confirm your password:", initPassword)
confirmation = input("Y/N:\n")

if confirmation.capitalize() == "Y":
    print("Password confirmed")
elif confirmation.capitalize() == "N":
    print("Password not confirmed")
else:
    print("Unvalid input")

