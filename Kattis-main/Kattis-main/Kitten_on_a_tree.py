def find_next(start, arr):
    if (start == arr[0][0] or start == -1):
        #print(arr[0][0])
        return 0
    else:
        for i in arr:
            found = False
            for j in i:
                if (j == start and i.index(j) != 0):
                    start = (i[0])
                    answer_arr.append(start)
                    find_next(start, arr)
                    found = True
                    break
            if found:
                break

answer_arr = []
start = int(input())
arr = []
end = 0
while(end != -1):
    line = input()
    line_arr = [int(n) for n in line.split()]
    arr.append((line_arr))
    end = int(line_arr[0])

print(start, end=' ')
#print(arr[0][0], 'this')
(find_next(start, arr))
#print(answer_arr)
for i in (answer_arr):
    print(i, end=' ')