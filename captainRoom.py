if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int, input().split()))
    roomSet = set(rooms)
    print(roomSet)
    roomSum = sum(rooms)
    print(roomSum)
    roomSetSum = sum(roomSet) * k
    print(roomSetSum)
    captainsRoom = (roomSetSum - roomSum) // (k - 1)
    print(captainsRoom)
