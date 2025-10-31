student_marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Dhananjay": 90,
    "Eva": 88
}

name = input("Enter the student's name: ")

#Retrieve and display marks or show message if not found
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found in the record.")
