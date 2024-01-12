"""
Script to make updates in github
"""

import pandas as pd
import click

click.command(short_help='Parser to import datset')
click.option('-f', '--file_name', required=True, help='File to import')
def main(file_name):
    """
    Main function
    """
    df = pd.read_csv(file_name)
    print(df.shape)

if __name__ == "__main__":
    main()
