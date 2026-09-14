import random

def roll_dice():
	return random.randint(1, 6)

def main():
	result = roll_dice()
	print(result)

	while result != 6:
		result = roll_dice()
		print(result)

if __name__ == "__main__":
	main()
