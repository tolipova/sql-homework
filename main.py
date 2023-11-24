import pandas as pd

import sqlite3
import uuid

excel_file_path = 'excel.xlsx'
df = pd.read_excel(excel_file_path)
df['UniqueID'] = [str(uuid.uuid4())for _ in range(len(df))]
conn = sqlite3.connect('Users.sqlite3')
cursor = conn.cursor()

table_name = 'users'
sxema = '''
    CREATE TABLE IF NOT EXISTS users(
        UniqueID TEXT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        email TEXT
    );

'''
conn.execute(sxema)
df.to_sql(table_name,conn, if_exists=r'replace', index=False)
conn.commit()
# Foydalanuvchilarni username bo'yicha izlash so'rovi
first_name = 'altman'
query = f"SELECT * FROM users WHERE first_name = '{first_name}'"
cursor.execute(query)
found_users = cursor.fetchall()
for user in found_users:
    print(user)

cursor = conn.cursor()
query = "DELETE FROM users WHERE email LIKE '%@example%'"

# O'chirish so'rovini bajarish
cursor.execute(query)
conn.commit()
#Yangi foydalanuvchi qushish
def add_user(first_name,last_name,email):
    cursor.execute('''
                INSERT INTO users(first_name, last_name, email)
                VALUES (?,?,?,?)
                   ''',(first_name,last_name,email))
    query = add_user
    print(query)
    conn.commit()

conn.close()
