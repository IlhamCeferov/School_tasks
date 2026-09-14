import math

def unit_price(diameter, price):
	radius_in_metres = diameter / 200
	area = math.pi * radius_in_metres ** 2
	return price / area

def main():
	diameter_1 = float(input("Enter the diameter of the first pizza in centimetres: "))
	price_1 = float(input("Enter the price of the first pizza in euros: "))
	diameter_2 = float(input("Enter the diameter of the second pizza in centimetres: "))
	price_2 = float(input("Enter the price of the second pizza in euros: "))

	unit_price_1 = unit_price(diameter_1, price_1)
	unit_price_2 = unit_price(diameter_2, price_2)

	if unit_price_1 < unit_price_2:
		print("The first pizza provides better value for money.")
	elif unit_price_2 < unit_price_1:
		print("The second pizza provides better value for money.")
	else:
		print("The pizzas provide equal value for money.")

if __name__ == "__main__":
	main()