from hello_world import app, db
from hello_world.formater import get_formatted
from hello_world.formater import SUPPORTED, PLAIN
from flask import request


@app.route('/')
def index():
    moje_imie = 'Natalia'
    msg = 'Hello World!'
    output = request.args.get('output')
    if not output:
        output = PLAIN

    if db:
        user = db.Users.find_one({'imie': 'Sebastian'})
        if user:
            moje_imie = user['imie']
            msg = user['mgs']

    return get_formatted(msg, moje_imie,
                         output.lower())


@app.route('/outputs')
def supported_output():
    return ", ".join(SUPPORTED)
