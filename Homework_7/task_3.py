def main():
	airports = {}

	while True:
		print("1 - Enter a new airport")
		print("2 - Fetch airport information")
		print("3 - Quit")
		choice = input("Choose an option: ")

		if choice == "1":
			icao_code = input("Enter the ICAO code: ").upper()
			airport_name = input("Enter the name of the airport: ")
			airports[icao_code] = airport_name
		elif choice == "2":
			icao_code = input("Enter the ICAO code: ").upper()
			airport_name = airports.get(icao_code)

			if airport_name is None:
				print("Airport not found")
			else:
				print(airport_name)
		elif choice == "3":
			break
		else:
			print("Invalid option")


if __name__ == "__main__":
	main()