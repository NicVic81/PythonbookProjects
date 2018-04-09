import unittest
from chapter_11_testing import format_city_country


class TestCities(unittest.TestCase):
    """Class form testing the cities functions"""

    def test_city_country(self):
        """Test to see if the function works with just a city and state """
        returned_address = format_city_country('parkersburg', 'west virginia')
        self.assertEqual(returned_address, 'Parkersburg, West Virginia')

    def test_city_country_population(self):
        """Test to see if it works with a population as well"""
        returned_address = format_city_country('arnoldsburg', 'west virginia', '7')
        self.assertEqual(returned_address, 'Arnoldsburg, West Virginia - population one hottie.')


unittest.main()
