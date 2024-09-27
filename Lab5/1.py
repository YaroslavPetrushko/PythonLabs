
n = int(input("n = "))

print(f"Enter {n} array elements:")

arr = [int(input()) for _ in range(n)]

newArr=[]

for i in range(n-1):
    if arr[n-1-i] < 0:
        newArr.append(arr[n-1-i])

print("New array: ", newArr)
