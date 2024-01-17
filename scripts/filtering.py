"""
Contains all the filters for your dataset
"""


class FilteringClass:
    """
    Class for filtering
    """

    def __init__(self, df):
        self.df = df

    def filter_price(self, price):
        """
        Filter price
        """
        if isinstance(price, float):
            return self.df[self.df["Price Starting With ($)"] < price]
        raise TypeError(f"The entered price: {price} is not a number.")

    def filter_price_high(self, price):
        """
        Check if the entered price is too high
        """
        if price <= 1095:
            return True
        raise TypeError(f"The entered price: {price} is too high.")

    def filter_month(self, month):
        """
        Filter by month of publishing
        """
        if month in [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ]:
            return self.df[self.df["Publish Date (Month)"] == month]
        raise TypeError("The month you entered is not valid.")

    def filter_year_length(self, year):
        """
        Ensures that the lenght of the entered number is 4, soo it is a year
        """
        if len(year) == 4:
            return True
        raise TypeError

    def filter_year(self, year):
        """
        Filter by year of publishing
        """
        if isinstance(year, int):
            return self.df[self.df["Publish Date (Year)"] == year]
        raise TypeError
