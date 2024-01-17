"""
Script to make updates in github
"""

import sys
from filtering import FilteringClass as f
import pandas as pd
import click

sys.path.append("scripts")


def load_dataset(filename):
    """
    Function to load dataset.
    """
    extension = filename.rsplit(".", 1)[-1]
    if extension == "csv":
        return pd.read_csv(filename)
    raise TypeError(f"The extension is {extension} and not csv, try again")


@click.command(short_help="Parser to import datset")
@click.option("-f", "--file_name", required=True, help="File to import")
@click.option("-p", "--price", required=True, help="Price to filter by")
@click.option("-m", "--month", help="Month to filter by")
@click.option("-y", "--year", help="Year to filter by")
def main(file_name, price, month, year):
    """
    Main function
    """
    df = load_dataset(file_name)

    print(df.shape)

    if price:
        df = f.FilteringClass(df).filter_price(float(price))
    if month:
        df = f.FilteringClass(df).filter_month(month)
    if year:
        df = f.FilteringClass(df).filter_year(year)

    print(df.shape)


if __name__ == "__main__":
    main()
