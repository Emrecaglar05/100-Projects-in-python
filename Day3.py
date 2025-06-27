print("------------Welcome To My Calculator------------")

choice = input("Please select a calculation type (a/s/m/d/mo/ex): ")

if choice in ["a", "s", "m", "d", "mo", "ex"]:
    number1 = int(input("Enter a number: "))
    number2 = int(input("Enter a second number: "))

    if choice == "a":
        print(f"Addition: {number1} + {number2} = {number1 + number2}")
    elif choice == "s":
        print(f"Subtraction: {number1} - {number2} = {number1 - number2}")
    elif choice == "m":
        print(f"Multiplication: {number1} * {number2} = {number1 * number2}")
    elif choice == "d":
        if number2 != 0:
            print(f"Division: {number1} / {number2} = {number1 / number2}")
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == "mo":
        print(f"Modulus: {number1} % {number2} = {number1 % number2}")
    elif choice == "ex":
        print(f"Exponentiation: {number1} ** {number2} = {number1 ** number2}")
else:
    print("Invalid choice. Please try again.")
