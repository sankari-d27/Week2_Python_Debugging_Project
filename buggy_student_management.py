
# Student Marks Management System
# Original version - Contains intentional bugs

students = []


def add_student():
    name = input("Enter student name: ")

    try:
        marks = int(input("Enter student marks: "))

        if marks < 0 or marks > 100:
            print("Invalid marks! Enter marks between 0 and 100.")
            return

        students.append({"name": name, "marks": marks})
        print("Student added successfully!")

    except ValueError:
        print("Invalid input! Please enter numbers only.")


def calculate_average():
    if not students:
        print("No student records available to calculate average.")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)
    print("Average marks:", average)


def display_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

def save_students():
    with open("students.txt", "w") as file:
        for student in students:
            file.write(f'{student["name"]},{student["marks"]}\n')

    print("Student records saved successfully!")

def read_students():
    try:
        with open("students.txt", "r") as file:
            print("\nSaved Student Records:")
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("No student records file found.")


def main():
    add_student()
    calculate_average()
    save_students()
    read_students()

if __name__ == "__main__":
    main()
