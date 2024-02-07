import re
import sqlite3
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for
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

@app.route("/add-recipe", methods=["POST", "GET"])
def add_recipe():
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        ingredients = request.form['ingredients']
        conn = get_db_connection()
        conn.execute('INSERT INTO recipes (title, content, author, ingredients) VALUES (?, ?, ?, ?)',(title, content, author, ingredients))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    # return render_template('add_recipe.html', title=title, content=content, author=author, ingredients=ingredients)
    else:
        return render_template('add_recipe.html')

if __name__ == "__main__":
    app.run()