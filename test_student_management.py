
import unittest
from unittest.mock import patch
from io import StringIO
import student_management as app


class TestStudentManagement(unittest.TestCase):

    def setUp(self):
        app.students.clear()

    def test_add_student(self):
        with patch("builtins.input", side_effect=["Rahul", "85"]):
            app.add_student()

        self.assertEqual(len(app.students), 1)
        self.assertEqual(app.students[0]["marks"], 85)

    def test_invalid_marks(self):
        with patch("builtins.input", side_effect=["ABC", "105"]):
            with patch("sys.stdout", new=StringIO()) as output:
                app.add_student()

        self.assertEqual(len(app.students), 0)
        self.assertIn("Invalid marks", output.getvalue())

    def test_negative_marks(self):
        with patch("builtins.input", side_effect=["ABC", "-10"]):
            with patch("sys.stdout", new=StringIO()) as output:
                app.add_student()

        self.assertEqual(len(app.students), 0)
        self.assertIn("Invalid marks", output.getvalue())

    def test_invalid_text_input(self):
        with patch("builtins.input", side_effect=["ABC", "hello"]):
            with patch("sys.stdout", new=StringIO()) as output:
                app.add_student()

        self.assertEqual(len(app.students), 0)
        self.assertIn("Invalid input", output.getvalue())

    def test_average(self):
        app.students.extend([
            {"name": "Rahul", "marks": 80},
            {"name": "Priya", "marks": 100}
        ])

        with patch("sys.stdout", new=StringIO()) as output:
            app.calculate_average()

        self.assertIn("90.0", output.getvalue())

    def test_empty_student_list(self):
        with patch("sys.stdout", new=StringIO()) as output:
            app.calculate_average()

        self.assertIn("No student records", output.getvalue())

    def test_grade_calculation(self):
        self.assertEqual(app.display_grade(95), "A")
        self.assertEqual(app.display_grade(80), "B")
        self.assertEqual(app.display_grade(60), "C")
        self.assertEqual(app.display_grade(35), "Fail")


if __name__ == "__main__":
    unittest.main()
