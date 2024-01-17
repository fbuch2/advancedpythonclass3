"""
Test the filtering of the dataset
"""

import unittest
from scripts.filtering import FilteringClass


class TestFiltering(unittest.TestCase):
    """
    Class to test the different filters.
    """

    def setUp(self):
        """
        Wrong variables to enter
        """
        self.price = "AAAA"
        self.price_high= 2000
        self.month = "04"
        self.year = "ASD"
        self.year_length = 230

    def test_price(self):
        """
        Test the price filter
        """
        with self.assertRaises(TypeError):
            FilteringClass.filter_price(self, self.price)
    
    def test_price_high(self):
        """
        Test the price high filter
        """
        with self.assertRaises(TypeError):
            FilteringClass.filter_price_high(self, self.price_high)

    def test_month(self):
        """
        Test the month filter
        """
        with self.assertRaises(TypeError):
            FilteringClass.filter_month(self, self.month)

    def test_year_type(self):
        """
        Test if the year filter is a number
        """
        with self.assertRaises(TypeError):
            FilteringClass.filter_year(self, self.year)

    def test_year_length(self):
        """
        Test if the input year has 4 numbers.
        """
        with self.assertRaises(TypeError):
            FilteringClass.filter_year_length(self, self.year_length)
    

if __name__ == "__main__":
    unittest.main()