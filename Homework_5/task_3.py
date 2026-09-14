check_number = int(input("Enter a number: "))
is_prime = check_number >= 2

for divisor in range(2, check_number):
    if check_number % divisor == 0:
        is_prime = False
        break

if is_prime:
    print(f"{check_number} is a prime number.")
else:
    print(f"{check_number} is not a prime number.")