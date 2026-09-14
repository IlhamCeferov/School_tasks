def main():
	names = set()

	while True:
		name = input("Enter a name (empty string to stop): ")

		if name == "":
			break

		if name in names:
			print("Existing name")
		else:
			print("New name")
			names.add(name)

	for name in names:
		print(name)

if __name__ == "__main__":
	main()