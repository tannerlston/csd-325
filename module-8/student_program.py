# Tanner Elston, 11/22/25, JSON practice Assignment 8.2

import json

class Student:
    def __init__(self, F_Name, L_Name, Student_ID, Email):
        self.F_Name = F_Name
        self.L_Name = L_Name
        self.Student_ID = Student_ID
        self.Email = Email

def print_students(students):
    for s in students:
        print(f"{s.L_Name}, {s.F_Name} : ID = {s.Student_ID} , Email = {s.Email}")

def main():
    filename = "student.json"

    # Load JSON file into list of Student objects
    with open(filename, "r") as f:
        data = json.load(f)

    students = [Student(**entry) for entry in data]

    # Original list
    print("=== Original Student List ===")
    print_students(students)
    print()

    # Get new student info from user
    print("=== Add New Student ===")
    f_name = input("First Name: ")
    l_name = input("Last Name: ")

    while True:
        try:
            student_id = int(input("Student ID (numbers only): "))
            break
        except ValueError:
            print("Student ID must be a number. Please try again.")

    email = input("Email: ")

    # Append to class list and JSON data list
    new_student = Student(f_name, l_name, student_id, email)
    students.append(new_student)

    data.append({
        "F_Name": new_student.F_Name,
        "L_Name": new_student.L_Name,
        "Student_ID": new_student.Student_ID,
        "Email": new_student.Email
    })

    # Updated list
    print("\n=== Updated Student List ===")
    print_students(students)
    print()

    # Save updated data back to JSON
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"The {filename} file has been updated with the new student record.")

if __name__ == "__main__":
    main()
