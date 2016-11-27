## the following code print cartesian product of two input iterables

from itertools import product

def cartesian_product():
    A = map(int, raw_input().split())
    B = map(int, raw_input().split())
    r = list(product(A, B))
    for elem in r:
        print elem,

cartesian_product()
