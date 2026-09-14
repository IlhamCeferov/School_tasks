def gallons_to_litres(gallons):
	return gallons * 3.78541

def main():
	while True:
		gallons = float(input("Enter a volume in gallons (negative to quit): "))

		if gallons < 0:
			break

		print(gallons_to_litres(gallons))

if __name__ == "__main__":
	main()