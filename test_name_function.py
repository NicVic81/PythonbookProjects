import unittest
from name_function import get_formatted_name


class TestNameCase(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names with no middle name work such as Trent Reznor"""
        formatted_name = get_formatted_name('trent', 'reznor')
        self.assertEqual(formatted_name, 'Trent Reznor')

    def test_first_last_middle_name(self):
        """Do name with a middle name work"""
        formatted_name = get_formatted_name('emry', 'johnson', 'victoria')
        self.assertEqual(formatted_name, 'Emry Victoria Johnson')


unittest.main()
