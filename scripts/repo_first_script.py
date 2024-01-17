"""
Script to make updates in github
"""

import pandas as pd
import click
import filtering as f


#When testing the script with pytest, it asks for scripts.filtering as f. But, while using the script scripts. is not asked



def load_dataset(filename):
    """
    Function to load dataset.
    """
    extension = filename.rsplit('.', 1)[-1]
    if extension == "csv":
        return pd.read_csv(filename)
    else:
        raise TypeError(f"The extension is {extension} and not csv, try again")
    return df
@click.command(short_help='Parser to import datset')
@click.option('-f', '--file_name', required=True, help='File to import')
@click.option('-p', '--price', required=True, help='Price to filter by')
@click.option('-m', '--month', help='Month to filter by')
@click.option('-y', '--year', help='Year to filter by')
@click.option('-y', '--year', help='Year to filter by')

def main(file_name, price, month, year):
    """
    Main function
    """
    df = load_dataset(file_name)
    print(df.shape)
    import pdb; pdb.set_trace()
    if price:
        df = f.FilteringClass(df).filter_price(float(price))
    if month:
        df = f.FilteringClass(df).filter_month(month)
    if year:
        df = f.FilteringClass(df).filter_year(year)

    

    print(df.shape)

if __name__ == "__main__":
    main()
