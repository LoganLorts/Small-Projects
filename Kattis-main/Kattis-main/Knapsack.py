def knapSack(W, wt, val, n): 
    K = [[0] * (W + 1) for x in range(n + 1)]
 
    for i in range(1, n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                K[i][w] = max(val[i-1] 
                            + K[i-1][w-wt[i-1]], 
                            K[i-1][w]) 
            else: 
                K[i][w] = K[i-1][w] 
    ans = []
    for i in range(n, 0, -1):
        if K[i][W] != K[i-1][W]:
            ans.append(i-1)
            W -= wt[i-1]
    return ans

from sys import stdin
#main
while True:
    try:
        index_array = []
        unmodified_input = stdin.readline().split()
        weight = int(unmodified_input[0])
        weight2 = weight
        length = int(unmodified_input[1])
        values = []
        weights = []
        for i in range(length):
            unmodified_input = stdin.readline().split()
            values.append(int(unmodified_input[0]))
            weights.append(int(unmodified_input[1]))

        ans_arr = knapSack(weight, weights, values, length)
        ans_arr.sort()
        print(len(ans_arr))
        for i in (ans_arr):
            print(i, end = ' ')
        print()
    except:
        break