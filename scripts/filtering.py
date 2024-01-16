"""
Contains all the filters for your dataset
"""

class FilteringClass:
    """
    Class for filtering
    """

    def __init__(self,df):
        self.df = df

    def filter_price(self, price):
        """
        Filter price
        """
        if price.isnumeric() == True:
            return self.df[self.df['Price Starting With ($)'] < price]
        else:
            raise TypeError(f"The entered price: {price} is not a number. Please enter a correct price.")

    def filter_month(self, month):
        """
        Filter by month of publishing
        """
        return self.df[self.df['Publish Date (Month)'] == month]
    
    def filter_year(self, year):
        """
        Filter by year of publishing
        """
        return self.df[self.df['Publish Date (Year)'] == year]
