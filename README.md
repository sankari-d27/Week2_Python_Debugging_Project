Student Marks Management System – Python Debugging Project
1. Project Overview

The Student Marks Management System is a beginner-friendly Python console application developed as part of Week 2: Debugging and Troubleshooting Python Applications.

The project demonstrates how to identify, reproduce, debug, and fix common Python programming errors while improving code quality and reliability.

2. Project Objectives
Identify common Python programming bugs.
Understand the root causes of errors.
Apply debugging techniques using Python's pdb module.
Validate user inputs.
Handle file operations and exceptions.
Test the corrected application using automated test cases.
Improve code readability and maintainability.
3. Technologies Used
Python 3
Visual Studio Code
Python pdb Debugger
unittest Framework
Git and GitHub
4. Project Features
Add student names and marks.
Validate marks between 0 and 100.
Calculate average marks.
Assign grades based on marks.
Save student records in a text file.
Read and display saved student records.
Handle invalid inputs and file errors.
5. Bugs Identified and Resolved

The debugging process covered the following issues:

Incorrect dictionary key reference (KeyError).
Incorrect file opening mode (FileNotFoundError).
Missing marks validation.
Division by zero (ZeroDivisionError).
Invalid input handling (ValueError).
Grade calculation verification.
File reading and writing improvements.
6. Project Structure
text
Week2_Python_Debugging_Project/
│
├── buggy_student_management.py
├── student_management.py
├── test_student_management.py
├── students.txt
├── bug_report.md
├── debugging_log.md
├── README.md
│
└── screenshots/
    ├── 01_original_code.png
    ├── 02_errors_found.png
    ├── 03_second_error.png
    ├── 04_file_saved.png
    ├── 05_marks_validation.png
    ├── 06_zero_division_fixed.png
    ├── 07_invalid_input_test.png
    ├── 08_grade_testing.png
    ├── 09_file_content.png
    ├── 10_read_student_records.png
    ├── 11_automated_tests.png
    └── 12_pdb_debugging.png

7. How to Run the Application
Install Python 3.
Download or clone this repository.
Open the project folder in Visual Studio Code.
Open the terminal.
Run the following command:
bash
python student_management.py

8. How to Run Automated Tests

Execute:

bash
python -m unittest -v test_student_management.py


The project includes seven automated test cases covering student registration, input validation, average calculation, empty-list handling, and grade calculation.

9. Debugging Techniques

The Python pdb debugger was used to inspect variables and trace program execution.

Example commands:

text
p students
n
p total
c


These commands help inspect variable values, execute the next line, and continue program execution.

10. Testing and Results

The application was tested using valid marks, invalid marks, negative values, non-numeric inputs, and empty student records.

All seven automated test cases passed successfully.

11. Conclusion

This project provided practical experience in Python debugging and troubleshooting. By identifying and resolving programming errors, implementing input validation, improving file handling, and performing automated testing, the application became more reliable and maintainable.

The project strengthened my understanding of debugging techniques and basic Python application development.

