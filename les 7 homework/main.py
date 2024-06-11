import json
import sqlite3

import requests

users = requests.get('https://jsonplaceholder.typicode.com/users').json()

for user in users:
    name = user['name']
    username = user['username']
    email = user['email']

    database = sqlite3.connect('users.db')
    cursor = database.cursor()

    cursor.execute('''
    INSERT INTO users(name, username, email)
    VALUES (?,?,?)
    ''', (name, username, email))

    database.commit()
    database.close()
