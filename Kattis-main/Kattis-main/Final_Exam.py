length = int(input())
arr = []
count = 0
for i in range(length):
    arr.append(input())
for i in range(1, length):
    if arr[i] == arr[i-1]:
        count += 1
print(count)