## You have a series of numbers: 3, 4, 5, 7, 9, 12, 15... What will be the Nth number (N >= 1)?

## enter the 
N = int(input())

def series(N):
    if N % 2 == 0:
        print 3 + (1 + N / 2) * (N / 2) - (N /2)
    else:
        print 3 + (1 + N / 2) * (N / 2)
        
        

