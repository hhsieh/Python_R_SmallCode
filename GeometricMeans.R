# Write a function that will calculate the geometric mean of any given vector of numbers. 
# Test your function by feeding it various vectors and checking if it works properly.

print("enter a vector of numbers and then press ENTER twice")
x <- scan()
l <- length(x)
geometric.mean <- prod(x)^(1 / l)
