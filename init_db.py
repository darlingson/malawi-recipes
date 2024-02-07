import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO recipes (title, content, author,ingredients) VALUES (?, ?, ?, ?)",
            ('Nsima', 'Nsima cooking instructions','Darlingson','Nsima ingredients')
            )

cur.execute("INSERT INTO recipes (title, content, author,ingredients) VALUES (?, ?, ?, ?)",
            ('Futali', 'Futali cooking instructions','Darlingson','Futali ingredients')
            )

connection.commit()
connection.close()