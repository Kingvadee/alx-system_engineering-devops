#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /airbnb-onepage/: Displays 'Hello HBNB!'
    /number_odd_or_even/<int:n>: Displays whether the number is odd or even.
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/airbnb-onepage/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    return render_template('number_odd_or_even.html', number=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

