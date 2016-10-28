## The growth of a rabbit popualtion following a Fibonacci series. How many rabbits are there after 100 years? 
fibonacci <- function(n) {
	a <- 1
	b <- 0
	for (n in seq(1:n))
	    {swap <- a
	     a <- a+b
             b <- swap
	     n <- n-1}
	     b
}
rabbits <- c(sapply(1:100,fibonacci))
print("the number of rabbits after 100 years is:")
print(rabbits[100])
