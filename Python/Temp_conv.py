unit = input("Is the tempature Celsius or Fahrenheit (C/F):  ")
temp = float(input("Enter the tempature: "))

if unit == "C":
    temp = round((temp * 9) / 5 + 32, 1)
    print(f"The tempature in Fahrenheit is: {temp}F ")
elif unit == "F":
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"The tempature in Celsius is: {temp}C")
else:
    print(f"{unit} is an invalid unit of measurement")


