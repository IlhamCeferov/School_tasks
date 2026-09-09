import random

dice_count = int(input("How many dice should be rolled? "))
total = 0

for _ in range(dice_count):
	total = total + random.randint(1, 6)

print(f"The sum is {total}.")


