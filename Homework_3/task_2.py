while True:
    cabin_class = input("Enter the cabin class: ")

    if cabin_class == "LUX":
        print("Upper-deck cabin with a balcony.")
        break
    elif cabin_class == "A":
        print("Above the car deck, equipped with a window.")
        break
    elif cabin_class == "B":
        print("Windowless cabin above the car deck.")
        break
    elif cabin_class == "C":
        print("Windowless cabin below the car deck.")
        break
    else:
        print("Invalid cabin class")
        print("Please try again.")
