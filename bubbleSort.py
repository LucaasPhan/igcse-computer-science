import random

#bubble sort function
def bubbleSort(arr):
    arrLen = len(arr) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, arrLen):
            if arr[i] > arr[i+1]:
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

arr = []
#input the data
manOrAuto = input("Manual input or automatic input? A/M\n")
operated = False

if manOrAuto.capitalize() == "A": 
    #User enter the value range and the system will enter the values automatically and randomly
    numberRange = int(input("Your array length:\n"))
    minRange = int(input("Enter the minimum range:\n"))
    maxRange = int(input("Enter the maximum range\n"))

    #check if the number range is valid or not?
    if maxRange <= minRange:
        print("Maximum range of value can't not be smaller or equal to the minimum range of value!")

    #recall the data for the user to check
    print("Confirm data: \nLENGTH:", numberRange, "\nMIN:", minRange, "\nMAX:", maxRange)

    confirm = input("Y/N:\n") #user's confirmation
    if confirm.capitalize() == "Y": #iteration to append the number to the array
        operated = True
        for i in range(0, numberRange):
            number = random.randint(minRange, maxRange)
            arr.append(number)
    elif confirm.capitalize() == "N": 
        print("Operation cancelled.")
        operated = False
    else: #if the user enter value other than Y & N
        print("Invalid input.")
    if operated == True:
        print(str(bubbleSort(arr))[1:-1]) #remove the bracket
elif manOrAuto.capitalize() == "M": #User manually enter their values
    numberRange = int(input("Your array length:\n"))
    print("LENGTH:", numberRange)
    confirm = input("Y/N:\n") #user's confirmation
    if confirm.capitalize() == "Y": #iteration to append the number to the array
        operated = True
        for i in range(0, numberRange):
            number = int(input("Enter your number:\n"))
            arr.append(number)
    elif confirm.capitalize() == "N": 
        print("Operation cancelled.")
        operated = False
    else: #if the user enter value other than A & M
        print("Invalid input.")
    if operated == True:
        print(str(bubbleSort(arr))[1:-1]) #remove the brackets