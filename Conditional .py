print("Student Result System")
# student ka name aur marks input liye ja rahe hain
name = input("Enter student name: ")
english = float(input("English Marks: "))
math = float(input("Math Marks: "))
science = float(input("Science Marks: "))
computer = float(input("Computer Marks: "))
urdu = float(input("Urdu Marks: "))
# sab marks ko jamaa kiya ja raha hai
# + operator ka use numbers ko add karne ke liye hota hai
total = english + math + science + computer + urdu
# percentage nikalne ke liye total ko 500 se divide karke 100 se multiply kiya jata hai
percentage = (total / 500) * 100
print("\nTotal Marks =", total)
print("Percentage =", percentage)
# if, elif, aur else ka use conditions check karne ke liye hota hai
# >= comparison operator hai jo barabar ya is se zyada check karta hai
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