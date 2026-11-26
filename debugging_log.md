Debugging Session 1 – Successful Fixes
Bug 1: Incorrect Dictionary Key
Identified a KeyError in the calculate_average() function.
Root cause: Incorrect dictionary key ("mark" instead of "marks").
Solution: Corrected the dictionary key.
Result: Student marks were retrieved successfully.
Bug 2: Incorrect File Opening Mode
Identified a FileNotFoundError in the save_students() function.
Root cause: The program attempted to read a file that did not exist.
Solution: Changed file mode from "r" to "w" and implemented a with open() statement.
Result: Student records were saved successfully.
Validation

Test input:

Student name: sankari
Marks: 90

Actual output:

Student added successfully!
Average marks: 90.0
Student records saved successfully!

Status: Both bugs successfully resolved.

Bug 4 – ZeroDivisionError Resolution

Issue: The application crashed when no valid student records were available.

Root cause: The calculate_average() function attempted to divide by the number of students when the list was empty.

Fix implemented: Added an empty-list condition before calculating the average.

Testing:

Input marks: 105 – Rejected.
Input marks: -10 – Rejected.
Empty student list – Handled successfully.

Actual result: The application displayed "No student records available to calculate average."

Status: Successfully resolved.

Grade Calculation – Testing Results

Tested the display_grade() function with four different marks.

Input marks	Expected output	Actual output
95	A	A
80	B	B
60	C	C
35	Fail	Fail

Issue: Initially, the final test output was not displayed as expected.

Troubleshooting: Checked the conditional statements, saved the Python file, restarted the Python interpreter and tested again.

Result: All four grade conditions produced the correct output.

Status: Successfully verified.

File Saving – Testing Results

Test performed: Saved student information into students.txt.

Test input:

Student name: Rahul
Marks: 85

Expected result: Student details should be stored in the text file.

Actual result: The file was created and contained:

Rahul,85

Improvement: Used the with open() statement to manage file resources safely.

Status: File saving verified successfully.

File Reading – Code Improvement

Objective: Implemented a function to read and display saved student records.

Changes made:

Created read_students() function.
Used with open() to read the students.txt file.
Added FileNotFoundError exception handling.
Displayed saved student information in the terminal.

Test input:

Student name: Priya
Marks: 95

Expected output: Student details should appear in the terminal.

Actual output: Priya,95 was displayed successfully.

Result: File reading functionality verified successfully.

Code quality improvement: Added modular file-reading functionality and exception handling.

Automated Testing and Final Validation

Testing tool: Python unittest framework.

Total test cases: 7

Tests performed:

Add student successfully.
Reject marks above 100.
Reject negative marks.
Handle non-numeric input.
Calculate average marks.
Handle an empty student list.
Verify grade calculation.

Actual result: All 7 automated tests passed successfully.

Debugger: Python pdb was used to inspect variables and trace program execution.

Final outcome: The corrected Student Marks Management System runs successfully and passes all automated tests.

Conclusion: The debugging process improved application reliability, input validation, file handling, readability and maintainability.