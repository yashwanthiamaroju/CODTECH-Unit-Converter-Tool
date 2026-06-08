print("UNIT CONVERTER TOOL")

while True:
    print("\n1. Kilometers to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. Kilograms to Pounds")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        miles = km * 0.621371
        print("Miles =", miles)

    elif choice == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print("Fahrenheit =", fahrenheit)

    elif choice == "3":
        kg = float(input("Enter kilograms: "))
        pounds = kg * 2.20462
        print("Pounds =", pounds)

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")