print("Student Result System")
name = input("Enter student name: ")
english = float(input("English Marks: "))
math = float(input("Math Marks: "))
science = float(input("Science Marks: "))
computer = float(input("Computer Marks: "))
urdu = float(input("Urdu Marks: "))
total = english + math + science + computer + urdu
percentage = (total / 500) * 100
print("\nTotal Marks =", total)
print("Percentage =", percentage)
if percentage >= 80:
    print("Grade: A")
elif percentage >= 70:
    print("Grade: B")
elif percentage >= 60:
    print("Grade: C")
elif percentage >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")