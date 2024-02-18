import re
import sqlite3
from datetime import datetime
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)

app.secret_key = 'secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config["SECRET_KEY"] = "secret-key"
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.init_app(app)

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
 
 
db.init_app(app) 
with app.app_context():
    db.create_all()
 
@login_manager.user_loader
def loader_user(user_id):
    return Users.query.get(user_id)

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = Users(username=request.form.get("username"),
                     password=request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("sign_up.html")
 
 
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Users.query.filter_by(
            username=request.form.get("username")).first()
        if user.password == request.form.get("password"):
            login_user(user)
            return redirect(url_for("home"))
    return render_template("login.html")
 
 
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

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
@app.route("/recipes", methods=["GET"])
def recipes():
    conn = get_db_connection()
    recipes = conn.execute('SELECT * FROM recipes').fetchall()
    conn.close()
    return render_template("recipes.html", recipes=recipes)

@app.route("/recipe/<int:recipe_id>", methods=["GET"])
def recipe(recipe_id):
    conn = get_db_connection()
    recipe = conn.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,)).fetchone()
    print(recipe)
    conn.close()
    return render_template("recipe.html", recipe=recipe)
app.route("/recipe/<int:recipe_id>/edit", methods=["GET"])
@login_required
def edit_recipe(recipe_id):
    return render_template("edit_recipe.html", recipe_id=recipe_id)
@app.route("/add-recipe", methods=["POST", "GET"])
@login_required
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
@app.route("/about",methods=["GET"])
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run()