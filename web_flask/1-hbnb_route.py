#!/usr/bin/python3
"""
Module Docs
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def task0():
    """
    Function Docs
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def task1():
    """
    Function Docs
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
