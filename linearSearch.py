items = ["hamburger", "fried chicken", "french fries", "pho", "com tam"]
itemToFind = input("What food?\n").lower()

def linearSearch(items, itemToFind):
    i = 0
    found = False
    while found == False and i < len(items):
        if items[i] == itemToFind:
            found = True
        else:
            i = i + 1
    if found == True:
        return print("Item found in the menu at the position", i+1)
    else:
        return print("Item not found")

linearSearch(items, itemToFind)