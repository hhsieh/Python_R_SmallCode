## Given a string S, print all possible size N replacement combinations of the string in lexicographic sorted order.

from itertools import combinations_with_replacement

def comb_replace():
    A = map(str, raw_input().split())
    S = "".join(sorted(A[0]))
    N = int(A[1])
    L = list(combinations_with_replacement(S, N))
    for elem in L:
        print "".join(elem)

## call the function        
comb_replace()  

## to implement the function for multiple times
c = int(input())

for i in range(c):
    comb_replace()
