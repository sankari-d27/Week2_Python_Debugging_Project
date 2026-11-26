Bug Report – Student Marks Management System
Bug 1: Incorrect Dictionary Key

Error message: KeyError: 'mark'

Location: calculate_average() function, line 18.

Problem: The program uses student["mark"], but the dictionary stores the value using the key "marks".

Root cause: Incorrect dictionary key reference.

Expected behavior: The program should retrieve student marks correctly and calculate the average.

Proposed solution: Replace student["mark"] with student["marks"].

Evidence: screenshots/02_errors_found.png

Bug 2: FileNotFoundError

Error message: FileNotFoundError: [Errno 2] No such file or directory: 'students.txt'

Location: save_students() function, line 34.

Problem: The program attempts to open students.txt in read mode ("r"), but the file does not exist.

Root cause: Incorrect file opening mode.

Expected behavior: The program should create the file if it does not exist and save student records.

Proposed solution: Change the file opening mode from "r" to "w" and use a with open() statement.

Evidence: screenshots/03_second_error.png

Bug 3: Missing Marks Validation

Unexpected behavior: The program accepts marks outside the valid range of 0–100.

Test cases:

Student	Marks	Actual result
ABC	105	Accepted incorrectly
XYZ	-10	Accepted incorrectly
JK	75	Accepted

Root cause: No conditional validation was implemented before storing student marks.

Expected behavior: The application should accept only marks between 0 and 100.

Proposed solution: Add an if condition to validate marks before adding a student.

Evidence: Terminal screenshots showing the three test cases.

Bug 4: Division by Zero Error

Error message: ZeroDivisionError: division by zero

Location: calculate_average() function.

Problem: When invalid marks are entered, the student is not added to the list. However, the program still attempts to calculate the average.

Root cause: Missing empty-list validation before performing division.

Expected behavior: The program should display a message when no student records are available instead of crashing.

Solution: Add a condition to check whether the students list is empty before calculating the average.

Evidence: Terminal screenshot showing ZeroDivisionError after invalid marks were entered.

Bug 5: Invalid Input Handling

Problem: The original program crashed when the user entered text instead of numeric marks.

Root cause: The program attempted to convert invalid text into an integer without exception handling.

Solution: Implemented try-except using ValueError.

Test input: abc

Expected output: Invalid input! Please enter numbers only.

Actual result: The program handled the invalid input without crashing.

Status: Successfully resolved.