import random

total_points = int(input("How many random points should be generated? "))
inside_circle = 0

for _ in range(total_points):
	x = random.uniform(-1, 1)
	y = random.uniform(-1, 1)

	if x ** 2 + y ** 2 < 1:
		inside_circle += 1

pi_approximation = 4 * inside_circle / total_points
print(f"Approximation of pi: {pi_approximation}")
