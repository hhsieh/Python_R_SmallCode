## an exercise of using Counter and removing values from a list

from collections import Counter

def buyshoes():
    N = int(input())
    sizes = map(int, raw_input().split())
    baskets = []
    C = int(input())
    for c in range(C):
        s, P = map(int, raw_input().split())
        if s in Counter(sizes).keys():
            baskets.append(P)
            sizes.remove(s)
    print sum(baskets)
 
buyshoes()
