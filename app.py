# Imports
from flask import Flask
from flask.templating import render_template
import  main

# Declaration

app = Flask(__name__)

# Settings


# Routes
@app.route("/")
def hello():
    return "Hello, World "

@app.route('/web/')
def web():
    return render_template('home.html')

@app.route('/click/')
def click():

    return main.Trans()

@app.route('/form/')
def form():
    return render_template('form.html')

# Start here
if __name__ == "__main__":
    app.run(debug=True)