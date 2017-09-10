"""Database Script."""
import sqlite3

import pandas as pd

# pylint: disable=invalid-name


def load_table(table_name, connecter):
    """Load table from database to pandas Dataframe"""
    return pd.read_sql_query("SELECT * FROM {}".format(table_name), connecter)


if __name__ == "__main__":
    con = sqlite3.connect('database/database.sqlite')

    # Load data in to DataFrame
    match_df = load_table('Match', con)

    # Close DB pipe
    con.close()

    match_2016 = match_df[(match_df['season'] == '2015/2016') & (match_df['league_id'] == 1729)]
    sliced_match_df = match_2016[['goal']]

    sliced_match_df.to_csv(path_or_buf='output.csv')