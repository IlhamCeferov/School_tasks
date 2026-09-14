import random

def roll_dice(number_of_sides):
	return random.randint(1, number_of_sides)

def main():
	number_of_sides = int(input("How many sides does the dice have? "))
	result = roll_dice(number_of_sides)
	print(result)

	while result != number_of_sides:
		result = roll_dice(number_of_sides)
		print(result)

if __name__ == "__main__":
	main()
