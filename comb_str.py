# Given a string S, print all possible combinations, up to size N, of the string in lexicographic sorted order.

from itertools import combinations

def comb_str():
    A = map(str, raw_input().split())
    S = "".join(sorted(A[0]))
    N = int(A[1])
    L = [combinations(S,n) for n in range(1, N+1)]
    for l in L:
        for i in l:
            print "".join(i)

comb_str()
