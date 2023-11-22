#!/usr/bin/python3
"""
Module Docs
"""
from flask import Flask
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
    Fucntion Docs
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Function Docs
    """
    storage.close()


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
