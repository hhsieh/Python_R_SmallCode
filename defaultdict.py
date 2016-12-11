# an exercise of defaultdict

from collections import defaultdict

def match_():
    d = defaultdict(list)
    n, m = map(int, raw_input().split())
    for i in range(n):
        d['n'].append(map(str, raw_input()))
    for j in range(m):
        d['m'].append(map(str, raw_input()))
    for elem in d['m']:
        if elem in d['n']:
            print "Yes"
        else:
            print "No"


match_()
