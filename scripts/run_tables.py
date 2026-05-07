import sqlite3

conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

with open('create_tables.sql', 'r') as f:
    sql = f.read()

cursor.executescript(sql)
conn.commit()
conn.close()

print("All tables created successfully!")