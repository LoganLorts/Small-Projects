from sys import stdin

def compute_prefix_function(pattern):
    m = len(pattern)
    pi = [0] * m
    k = 0
    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = pi[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        pi[q] = k
    return pi

def kmp_search(pattern, string):
    m = len(pattern)
    n = len(string)
    pi = compute_prefix_function(pattern)
    q = 0
    indices = []

    for i in range(n):
        while q > 0 and pattern[q] != string[i]:
            q = pi[q - 1]
        if pattern[q] == string[i]:
            q += 1
        if q == m:
            indices.append(i - m + 1)
            q = pi[q - 1]

    return indices

if __name__ == '__main__':
    on_string = False
    for line in stdin:
        if not on_string:
            pattern = line.rstrip()
            on_string = True
        else:
            string = line.rstrip()
            on_string = False

            indices = kmp_search(pattern, string)
            print(*indices, end=" ")
            print('\n')