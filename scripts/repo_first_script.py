"""
Script to make updates in github
"""

import pandas as pd
import click
import filtering as f

def load_dataset(filename):
    """
    Function to load dataset.
    """
    extension = filename.rsplit('.', 1)[-1]
    if extension == "csv":
        return pd.read_csv(filename)
    else:
        raise TypeError(f"The extension is  {extension} and not csv, try again")
    return df
@click.command(short_help='Parser to import datset')
@click.option('-f', '--file_name', required=True, help='File to import')
def main(file_name):
    """
    Main function
    """
    df = load_dataset(file_name)
    
    
    result = f.FilteringClass(df).filter_price(12)
    
    print(result.shape)

if __name__ == "__main__":
    main()
