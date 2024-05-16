from math import sqrt
from itertools import permutations
def is_prime(n):
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return (True)
        else:
            return (False)
    else:
        return (False)


#main
length = int(input())
for i in range(length):
    count = 0
    prime = input()
    split = list(map(int, str(prime)))
    set_prime = set()
    #print(split)
    #print(prime)
    for z in range(len(split)):
        perm = permutations(split, z+1)
        for j in list(perm):
            if(j[0] == 0):
                continue
            num = int(''.join(map(str, j)))
            if(is_prime(num)):
                set_prime.add(num)
            else:
                continue

    print(len(set_prime))

