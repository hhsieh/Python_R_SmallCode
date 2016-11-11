# Write a program in which the computer rolls three dice, and the user has to guess the sum result of that roll. 
# Be sure to write a message on screen informing the player of the actual number the computer has generated, 
# and whether s/he has won or lost.

print("guess the sum of rolling a dice for three times and then press ENTER twice")
x <- scan()
results <- sample(1:6,3)
result <- sum(results)
if (x == result) {
	print("Your answer is correct. Congratulations!!")
}
if (x != result) {
	print("Oops, better luck next time. The correct answer is:")
	print(result)
}
