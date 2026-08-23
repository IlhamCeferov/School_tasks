grams = int(input('How many grams?: '))
kilograms = grams // 1000
remaining_grams = grams % 1000
print(f'{grams} grams is {kilograms} kilograms and {remaining_grams} grams')
