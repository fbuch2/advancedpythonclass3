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
        self.price = "ABC"
        self.month = "April"
        self.year = "Twenty-two"

    def test_price(self):
        """
        Test the price filter
        """
        with self.assertRaises(TypeError):
            FilteringClass.filter_price(self.price)
    

if __name__ == "__main__":
    unittest.main()