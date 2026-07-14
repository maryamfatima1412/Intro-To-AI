# user se name aur age liya ja raha hai
# input() hamesha string return karta hai, is liye age ko int() se integer mein convert kiya gaya hai
name = input("Enter student name: ")
age = int(input("Enter student age: "))
# f-string ka use is liye hota hai kyun ke yeh text ke sath variable ka value asaan tareeqay se dikhata hai
print(f"Hello {name}, you are {age} years old.")
# variable ka naam number se start nahi ho sakta, is liye age, name jaise naam use kiye gaye hain
# > comparison operator hai jo check karta hai ke age 18 se bari hai ya nahi
is_student = age > 18
print(is_student)