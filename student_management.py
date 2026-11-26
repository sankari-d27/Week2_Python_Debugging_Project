
# Student Marks Management System
# Final Corrected Version

students = []


def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty!")
        return

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
        print("No student records available.")
        return

    total = sum(student["marks"] for student in students)
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
    try:
        with open("students.txt", "w") as file:
            for student in students:
                grade = display_grade(student["marks"])
                file.write(
                    f'{student["name"]},{student["marks"]},{grade}\n'
                )

        print("Student records saved successfully!")

    except OSError as error:
        print("Error saving student records:", error)


def read_students():
    try:
        with open("students.txt", "r") as file:
            print("\nSaved Student Records:")

            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("No student records file found.")

    except OSError as error:
        print("Error reading student records:", error)


def main():
    print("=== Student Marks Management System ===")

    add_student()
    calculate_average()
    save_students()
    read_students()


if __name__ == "__main__":
    main()
