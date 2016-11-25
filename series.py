## You have a series of numbers: 3, 4, 5, 7, 9, 12, 15... What will be the Nth number (N >= 1)?

## It is easy to find out the rule of addition in the sequence of numbers is 1, 1, 2, 2, 3, 3, ...
## We can write a function to reflect the above rule.

def series(N):
    if N % 2 == 0:
        print 3 + (1 + N / 2) * (N / 2) - (N /2)
    else:
        print 3 + (1 + N / 2) * (N / 2)
        
## We can call the function for many times to get a series of numbers if we desire:
## Let's produce the first 100 numbers

for N in range(1, 100):
    series(N)
    
    
    
        
        

