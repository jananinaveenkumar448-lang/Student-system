import unittest
import os

from models.db import init_db, add_student, get_all_students, DB


class TestStudentDB(unittest.TestCase):

    def setUp(self):
        # delete DB before each test
        if os.path.exists(DB):
            os.remove(DB)

        init_db()

    def test_add_student(self):
        add_student("Alice", 20, 85)
        self.assertEqual(len(get_all_students()), 1)

    def test_multiple_students(self):
        add_student("A", 18, 70)
        add_student("B", 19, 80)
        self.assertEqual(len(get_all_students()), 2)

    def test_score_value(self):
        add_student("Charlie", 21, 90)
        students = get_all_students()
        self.assertEqual(students[0][3], 90)

    def test_invalid_age_still_inserts(self):
        add_student("David", 0, 50)
        self.assertEqual(len(get_all_students()), 1)

    def test_db_not_empty(self):
        add_student("Eve", 22, 88)
        self.assertTrue(len(get_all_students()) > 0)


if __name__ == "__main__":
    unittest.main()