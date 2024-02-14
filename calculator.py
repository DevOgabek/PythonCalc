import math

while True:
    print("\nCalculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '7':
        print("Exiting the calculator. Goodbye! Stay healthy!")
        break

    if choice not in ['1', '2', '3', '4', '5', '6']:
        print("Invalid choice. Please enter a number between 1 and 7.")
        continue

    if choice in ['1', '2', '3', '4', '5']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    if choice == '1':
        result = num1 + num2
        operation = "Addition"
    elif choice == '2':
        result = num1 - num2
        operation = "Subtraction"
    elif choice == '3':
        result = num1 * num2
        operation = "Multiplication"
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            operation = "Division"
        else:
            print("Error: Division by zero.")
            continue
    elif choice == '5':
        result = num1 ** num2
        operation = "Power"
    elif choice == '6':
        if num1 >= 0:
            result = math.sqrt(num1)
            operation = "Square Root"
        else:
            print("Error: Cannot calculate square root of a negative number.")
            continue

    print(f"{operation} Result: {result}\n")