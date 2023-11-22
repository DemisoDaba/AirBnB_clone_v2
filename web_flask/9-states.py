#!/usr/bin/python3
"""
Module Docs
"""
from flask import Flask
from models import *
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    Function Docs
    """
    states = storage.all("State")
    if state_id is not None:
        state_id = 'State.{}'.format(state_id)
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Function Docs
    """
    storage.close()


if __name__ == '__main__':
    app.run(port='5000', host='0.0.0.0')
