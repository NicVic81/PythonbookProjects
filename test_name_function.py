import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names with no middle name work such as Trent Reznor"""
        formatted_name = get_formatted_name('trent', 'reznor')
        self.assertEqual(formatted_name, 'Trent Reznor')


unittest.main()
