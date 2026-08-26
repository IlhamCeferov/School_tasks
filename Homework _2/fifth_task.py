import math

talents = float(input("Enter the number of talents: "))
pounds = float(input("Enter the number of pounds: "))
lots = float(input("Enter the number of lots: "))

total_lots = talents * 20 * 32 + pounds * 32 + lots
total_grams = total_lots * 13.3

kilograms = total_grams / 1000
grams = total_grams % 1000

print(f"The weight is {int(kilograms)} kilograms and {grams:.2f} grams.")
