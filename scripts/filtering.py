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
        if isinstance(price, float):
            return self.df[self.df['Price Starting With ($)'] < price]
        else:
            raise TypeError(f"The entered price: {price} is not a number. Please enter a correct price.")

    def filter_month(self, month):
    
        """
        Filter by month of publishing
        """
        if month in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
            return self.df[self.df['Publish Date (Month)'] == month]
        else:
            raise TypeError(f"The entered month: {month} is not a month. Please enter a correct month.")
    
    def filter_year_length(self,year):
        if len(year) == 4:
            return True
        else:
            raise TypeError(f"The entered month: {year} is not a year. Please enter a correct year.")
    
    
    def filter_year(self, year):
        """
        Filter by year of publishing
        """
        if isinstance(year, int):
            return self.df[self.df['Publish Date (Year)'] == year]
        else:
            raise TypeError(f"The entered month: {year} is not a year. Please enter a correct year.")
        
