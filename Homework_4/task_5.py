correct_username = "python"
correct_password = "rules"

for attempt in range(5):
	username = input("Enter username: ")
	password = input("Enter password: ")

	if username == correct_username and password == correct_password:
		print("Welcome")
		break
else:
	print("Access denied")
