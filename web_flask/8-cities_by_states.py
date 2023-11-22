#!/usr/bin/python3
"""
Module Docs
"""
from flask import Flask
from models import *
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display the states and cities listed in alphabetical order"""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Function Docs
    """
    storage.close()


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
