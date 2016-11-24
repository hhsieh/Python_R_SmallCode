## Use intersection to find out whether two strings share the same substring(s)

# map two strings
a = map(str, input())
b = map(str, input())

# intersect a and b
c = set(a).intersection(b)

# if the length of c is greater than 0, print "Yes" - a and b share the same substring(s). Otherwise, print "No".
if len(c) > 0:
    print "Yes"
else:
    print "No"
