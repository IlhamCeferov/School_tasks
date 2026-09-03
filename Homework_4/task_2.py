inches = float(input("Enter inches (negative value to stop): "))

while inches >= 0:
	centimeters = inches * 2.54
	print(f"{inches} inches = {centimeters} centimeters")
	inches = float(input("Enter inches (negative value to stop): "))