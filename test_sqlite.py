import pandas as pd
import sqlite3

def load_table(table_name, connecter):
    return pd.read_sql_query("SELECT * FROM {}".format(table_name), con)

con = sqlite3.connect('database/database.sqlite')

# Load data in to DataFrame
player_df = load_table('Player', con)
match_df = load_table('Match', con)
# Close DB pipe
con.close

print(player_df.head())
print(match_df.head())
