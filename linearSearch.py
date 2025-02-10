items = ["hamburger", "fried chicken", "french fries", "pho", "com tam"]
itemToFind = input("What food?\n").lower()

def linearSearch(items, itemToFind):
    i = 0
    found = False
    while not found and i < len(items):
        if itemToFind == items[i]:
            found = True
        else:
            i += 1
    if found:
        return print("Item found in the menu at the position", i+1)
    else:
        return print("Item not found")

linearSearch(items, itemToFind)~