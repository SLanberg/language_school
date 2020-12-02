from application import app
from flask import render_template


@app.route('/')
@app.route('/index')
def home():
    return render_template("home.html")


@app.route('/prices')
def prices():
    return render_template("prices.html")


@app.route('/teachers')
def teachers():
    return render_template("teachers.html")
