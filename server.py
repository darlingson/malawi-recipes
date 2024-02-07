import re
import sqlite3
from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/", methods=["GET"])
def home(name = None):
    conn = get_db_connection()
    recipes = conn.execute('SELECT * FROM recipes').fetchall()
    conn.close()
    return render_template(
        "home.html",
        name=name,
        date=datetime.now(),
        recipes=recipes
    )

if __name__ == "__main__":
    app.run()