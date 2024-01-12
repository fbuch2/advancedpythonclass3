"""
Script to make updates in github
"""

import pandas as pd
import click

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
        return self.df[self.df['Price Starting With ($)'] < price]

@click.command(short_help='Parser to import datset')
@click.option('-f', '--file_name', required=True, help='File to import')
def main(file_name):
    """
    Main function
    """
    df = pd.read_csv(file_name)
    
    
    result = FilteringClass(df).filter_price(12)
    
    print(result.shape)

if __name__ == "__main__":
    main()
