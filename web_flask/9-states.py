
#!/usr/bin/python3
"""starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """closes
    """
    storage.close()


@app.route('/states')
def states():
    """display a HTML page: (inside the tag BODY)
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route('/states/<id>')
def cities_by_states(id):
    """display a HTML page: (inside the tag BODY)
    """
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
