from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")
    
@app.route("/about")
def about_me():
    return render_template("about_me.html")
    
@app.route("/homework")
def homework():
    return render_template("homework.html")
