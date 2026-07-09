# -------------------------------
# Command-Line Calculator
# -------------------------------

# Functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


print("=================================")
print("   Welcome to My Calculator")
print("=================================")

while True:

    print("\nAvailable Operations:")
    print("+  Addition")
    print("-  Subtraction")
    print("*  Multiplication")
    print("/  Division")
    print("Type 'quit' anytime to exit.")

    first = input("\nEnter first number: ")

    if first.lower() == "quit":
        print("\nThank you for using the calculator!")
        break

    second = input("Enter second number: ")

    if second.lower() == "quit":
        print("\nThank you for using the calculator!")
        break

    operation = input("Enter operation (+, -, *, /): ")

    if operation.lower() == "quit":
        print("\nThank you for using the calculator!")
        break

    try:
        num1 = float(first)
        num2 = float(second)

        if operation == "+":
            result = add(num1, num2)
            print(f"\n{num1} + {num2} = {result}")

        elif operation == "-":
            result = subtract(num1, num2)
            print(f"\n{num1} - {num2} = {result}")

        elif operation == "*":
            result = multiply(num1, num2)
            print(f"\n{num1} * {num2} = {result}")

        elif operation == "/":
            if num2 == 0:
                print("\nError: Division by zero is not allowed.")
            else:
                result = divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")

        else:
            print("\nError: Invalid operation. Please enter +, -, * or /.")

    except ValueError:
        print("\nError: Please enter valid numbers only.")