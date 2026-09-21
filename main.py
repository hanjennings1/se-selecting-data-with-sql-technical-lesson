import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

orders = pd.read_sql("""
        SELECT orderDate,
        strftime('%m', orderDate) AS month,
        strftime('%Y', orderDate) AS year,
        strftime('%d', orderDate) AS day
        FROM orders;
""", conn)

print(orders)

conn.close()