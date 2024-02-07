import re
from datetime import datetime
from flask import Flask, render_template
app = Flask(__name__)
@app.route("/", methods=["GET"])
def home(name = None):
    return render_template(
        "home.html",
        name=name,
        date=datetime.now()
    )

if __name__ == "__main__":
    app.run()