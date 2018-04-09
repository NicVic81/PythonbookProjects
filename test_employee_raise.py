import unittest
from chapter_11_testing import Employee


class EmployeeRaiseTest(unittest.TestCase):
    """Class for testing the Employee class"""

    def setUp(self):
        self.new_employee = Employee('nicholas', 'johnson', '80000')

    def test_default_raise(self):
        # self.new_employee = Employee('nicholas', 'johnson', '80000')
        self.new_employee.give_raise()
        self.assertEqual(self.new_employee.salary, 85000)

    def test_custom_raise(self):
        self.new_employee.give_raise(15000)
        self.assertEqual(self.new_employee.salary, 95000)


unittest.main()
