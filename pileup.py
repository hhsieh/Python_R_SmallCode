## test if a set of cubes can be piled up given the rule that the length of lower cube must be larger than that of upper cube.

def pileup():
    #print "enter the number of test cases: "
    N = input()
    for i in range(N):
        #print "enter the number of cubes in case no. " + str(i + 1) + " :"
        cubes = input()
        #print "enter the side lengths of cubes from the leftmost to the rightmost: "
        lengths = map(int, raw_input().split())
        pile = []
        for j in range(len(lengths)):
            if lengths[0] >= lengths[-1]:
                pile.append(lengths[0])
                lengths.pop(0)
            else:
                pile.append(lengths[-1])
                lengths.pop()
        u = []
        for k in range(len(pile)-1):
            if pile[k] >= pile[k+1]:
                u.append("Yes")
            else:
                u.append("No")
        if "No" in u:
            #print "Unable to stack the cubes."
            print "No"
        elif "No" not in u:
            #print "Able to stack the cubes."
            print "Yes"

pileup()
