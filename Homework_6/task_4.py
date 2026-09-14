def sum_numbers(numbers):
	total = 0

	for number in numbers:
		total += number

	return total

def main():
	numbers = [1, 2, 3, 4, 5]
	result = sum_numbers(numbers)
	print(result)

if __name__ == "__main__":
	main()