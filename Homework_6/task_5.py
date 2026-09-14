def remove_odd_numbers(numbers):
	even_numbers = []

	for number in numbers:
		if number % 2 == 0:
			even_numbers.append(number)

	return even_numbers

def main():
	numbers = [1, 2, 3, 4, 5, 6]
	even_numbers = remove_odd_numbers(numbers)

	print(numbers)
	print(even_numbers)

if __name__ == "__main__":
	main()