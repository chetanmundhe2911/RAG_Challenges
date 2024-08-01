import pandas as pd
from sqlalchemy import create_engine

# Create a sample DataFrame
data = {'user_id': [1, 2, 3], 'username': ['Alice', 'Bob', 'Charlie']}
df = pd.DataFrame(data)

# Connect to an SQLite database (you can replace this with other databases)
engine = create_engine('sqlite:///mydatabase.db')

# Write the DataFrame to an 'users' table in the database
df.to_sql(name='users', con=engine, if_exists='replace', index=False)

# Now you can query the 'users' table using SQL
query_result = pd.read_sql_query("SELECT * FROM users", con=engine)
print(query_result)


## Use below snapshot for ln2sql

# Suppose you have a database 'city.sql' and a language file 'english.csv'
# You want to convert the query "Count how many cities there are with the name 'blob'?"
# into an SQL query
from ln2sql import ln2sql

query = "Count how many cities there are with the name 'blob'?"
result = ln2sql(query, db_path='database/city.sql', lang_path='lang/english.csv')
print(result)

