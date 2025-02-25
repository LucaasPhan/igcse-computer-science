arr = []
for _ in range(3):
    n = int(input())
    arr.append(n)

sorted = False
answer = 0
i = 0
while not sorted:
    sorted = True
    if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]
        sorted = False
    i+=1

answer = arr[1]*arr[2] 
print(answer)