import sqlite3
import pandas as pd


excel_file_path = 'Excel.xlsx'
df = pd.read_excel(excel_file_path)

conn = sqlite3.connect('Users.sqlite3')
c = conn.cursor()

table_name = 'users'
sxema = '''
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT,
        last_name TEXT,
        email TEXT
    );

'''
conn.execute(sxema)
conn.commit()

#Get user input for adding new users
while True:
    print("1)Add new user")
    print("2)You can find  the need first_name")
    print("3)Delete email: ")
    print("4)Break")
    
    choice = int(input("Enter the need number: "))
    if choice == 1:
        first_name1 = input("Enter the first name of the new user: ")
        last_name1 = input("Enter the last name of the new user: ")
        email1 = input("Enter the email of the new user: ")

        c.execute('''
                        INSERT INTO users(first_name, last_name, email)
                        VALUES (?,?,?)
                        ''',(first_name1,last_name1,email1))
        conn.commit()
    elif choice == 2:
    #if first_name = 'altman'find first _name
        first_name = input("Enter the you need first_name from database which 'altman': ")
        if first_name == 'altman':
            c.execute(f"SELECT * FROM users WHERE first_name = '{first_name}'")
            query = c.fetchall()
            print(query,"ismi bor")
        else:
            print('bunday ism mavjud emas')
    elif choice == 3:        
    #delete user if user email = 'example.com'
        email = input("you will delete email only'exapmle.com' and enter this email if don't need : ")
        if email == 'example.com':
            c.execute("DELETE FROM users WHERE email LIKE 'example.com'")
            print("Delete this email")
        else:
            print("Bu email uchirish mumkin emas")
    elif choice == 4:
        print("okay bye!")
        break
    conn.commit()
    conn.close()
