import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO recipes (title, content, author,ingredients) VALUES (?, ?, ?, ?)",
            ('Nsima', 'put water on fire until lukewarm;;;;add floor to water while stirring until it is milky;;;;wait for water to boil, continue to periodically stir;;;;add more floor until you reach desired thickness;;;serve nsime using chipande','Darlingson','floor, water')
            )

cur.execute("INSERT INTO recipes (title, content, author,ingredients) VALUES (?, ?, ?, ?)",
            ('Futali', 'chop sweet potatoes into desired sizes;;;;boil in water until soft;;;;add salt to taste;;;;add grounded groundnuts to taste;;;;serve','Darlingson','groundnuts, water, salt,sweet potatoes')
            )

connection.commit()
connection.close()