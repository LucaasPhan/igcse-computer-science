initPassword = input("Enter your password: ")
confirmPassword = input("Confirm your password: ")

if initPassword == confirmPassword:
    print("Your password is correct")
else:
    print("Your password is not the same")