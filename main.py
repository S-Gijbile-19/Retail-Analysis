import sqlite3
import pandas as pd

print("Starting Ecommerce Database Setup...")

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Task 2: Create Tables
print("\n Task 2: Creating tables...")
with open('create_tables.sql', 'r') as f:
    sql = f.read()
cursor.executescript(sql)
print("Tables created!")

# Task 3: Load Data
print("\n Task 3: Loading data...")
pd.read_csv('users.csv').to_sql('dim_user', conn, if_exists='replace', index=False)
pd.read_csv('products.csv').to_sql('dim_product', conn, if_exists='replace', index=False)
pd.read_csv('orders.csv').to_sql('dim_order', conn, if_exists='replace', index=False)
pd.read_csv('order_items.csv').to_sql('fact_sales', conn, if_exists='replace', index=False)
pd.read_csv('reviews.csv').to_sql('dim_review', conn, if_exists='replace', index=False)
pd.read_csv('events.csv').to_sql('dim_event', conn, if_exists='replace', index=False)
print("Data loaded!")

# Task 4 & 5: Indexes
print("\n Task 4 & 5: Adding indexes...")
with open('optimize.sql', 'r') as f:
    sql = f.read()
cursor.executescript(sql)
print("Indexes added!")

# Task 6 & 7: Views
print("\n Task 6 & 7: Creating views...")
with open('views.sql', 'r') as f:
    sql = f.read()
cursor.executescript(sql)
print("Views created!")

conn.close()
print("\n All tasks completed successfully!")