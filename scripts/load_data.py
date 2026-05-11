import sqlite3
import pandas as pd

conn = sqlite3.connect('ecommerce.db')

pd.read_csv('users.csv').to_sql('dim_user', conn, if_exists='replace', index=False)
print("dim_user loaded!")

pd.read_csv('products.csv').to_sql('dim_product', conn, if_exists='replace', index=False)
print("dim_product loaded!")

pd.read_csv('orders.csv').to_sql('dim_order', conn, if_exists='replace', index=False)
print("dim_order loaded!")

pd.read_csv('order_items.csv').to_sql('fact_sales', conn, if_exists='replace', index=False)
print("fact_sales loaded!")

pd.read_csv('reviews.csv').to_sql('dim_review', conn, if_exists='replace', index=False)
print("dim_review loaded!")

pd.read_csv('events.csv').to_sql('dim_event', conn, if_exists='replace', index=False)
print("dim_event loaded!")

conn.close()
print("All data loaded successfully!")