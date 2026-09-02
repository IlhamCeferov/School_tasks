gender = input("Enter biological gender(female/male): ").lower()
hemoglobin = float(input("Enter hemoglobin value in g/l: "))

if gender == "female":
    if 117 <= hemoglobin <= 155:
        print("Hemoglobin value is normal.")
    elif hemoglobin < 117:
        print("Hemoglobin value is low.")
    else:
        print("Hemoglobin value is high.")
elif gender == "male":
    if 134 <= hemoglobin <= 167:
        print("Hemoglobin value is normal.")
    elif hemoglobin < 134:
        print("Hemoglobin value is low.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender input.Please enter female or male.")