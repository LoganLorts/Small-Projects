first_input = input().split()
size = int(first_input[0])
num_found = int(first_input[1])
#print(size, num_found)
arr = []
count = 0
for i in range(num_found):
    loop_var = int(input())
    if (loop_var not in arr):
        arr.append(loop_var)
        count += 1
        #print(i)
for j in range(size):
    if j not in arr:
        print(j)
print('Mario got ', count, ' of the dangerous obstacles.')