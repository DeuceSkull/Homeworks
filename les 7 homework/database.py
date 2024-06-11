import sqlite3
database = sqlite3.connect('users.db')
cursor = database.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
    users_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name CHAR(10),
    username CHAR(10),
    email CHAR(10)
)
''')

database.commit()
database.close()
