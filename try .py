# ye code try-except use karta hai error handle karne ke liye
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result =", result)
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
except ValueError:
    print("Error: Please enter a valid number.")