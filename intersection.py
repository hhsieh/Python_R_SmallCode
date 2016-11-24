## Use intersection to find out whether two strings share the same substring(s)

##############################
## First, some basic things ##
##############################
# map two strings
a = map(str, input())
b = map(str, input())

# intersect a and b
d = set(a).intersection(b)

# if the length of c is greater than 0, print "Yes" - a and b share the same substring(s). Otherwise, print "No".
if len(d) > 0:
    print "Yes"
else:
    print "No"

######################################################    
## We can write a function to accommodate the above ##
######################################################

def intersect():
    a = map(str, raw_input())
    b = map(str, raw_input())
    d = set(a).intersection(b)
    if len(d) > 0:
        print "YES"
    else:
        print "NO"

## call the function intersct for multiple times

c = int(input())

for _ in range(c):
    intersect()
    
