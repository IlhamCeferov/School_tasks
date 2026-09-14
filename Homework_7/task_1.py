def main():
	seasons = ("winter", "spring", "summer", "autumn")
	month = int(input("Enter the number of a month (1-12): "))

	season = seasons[(month % 12) // 3]
	print(season)

if __name__ == "__main__":
	main()