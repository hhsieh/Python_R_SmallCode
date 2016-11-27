## use itertools.permutations to permutate a string 

from itertools import permutations

def permutate_str():
    A = map(str, raw_input().split()) # input includes a string and the length of the iterable
    S = A[0]
    N = int(A[1])
    S = "".join(sorted(S)) # sort the string in alphabetical order
    L = list(permutations(S,N))
    for elem in L:
        print "".join(elem)

permutate_str()   
