import random

secret_number = random.randint(1, 10)
guess = int(input("Guess the number from 1 to 10: "))

while guess != secret_number:
	if guess > secret_number:
		print("Too high")
	else:
		print("Too low")

	guess = int(input("Guess again: "))

print("Correct")
