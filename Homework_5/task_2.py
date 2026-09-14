numbers = []

while True:
	number = input("Enter a number (press Enter to quit): ")

	if number == "":
		break

	numbers.append(int(number))

numbers.sort(reverse=True)
print(numbers[:5])
