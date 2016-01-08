'''
Main entrypoint for my 'build a bear' web application
'''

import json

from flask import (Flask, render_template, url_for, redirect,
                   request, make_response)

from options import DEFAULTS

app = Flask(__name__)


# This should work, but beware if this returns xyz...I get a 404, should
# fix later...
def get_saved_data():
    ''' Get saved data from browser cookies,
    or initialize data as empty dict '''
    try:
        data = json.loads(request.cookies.get('character'))
    except TypeError:
        data = {}
    return data


@app.route('/')
def index():
    ''' Instantiates home/index root route,
    context variable saves is assigned to dict data '''
    data = get_saved_data()
    return render_template('index.html', saves=data)


@app.route('/builder')
def builder():
    ''' Set builder route, gets cookie data, options variable
    is set from options.py '''
    return render_template('builder.html',
                           saves=get_saved_data(),
                           options=DEFAULTS)


@app.route('/save', methods=['POST'])
def save():
    ''' Handles save method (to cookies), and redirect post-save to
    builder route '''
    response = make_response(redirect(url_for('builder')))
    data = get_saved_data()
    data.update(dict(request.form.items()))
    response.set_cookie('character', json.dumps(data))
    return response

app.run(debug=True, host='0.0.0.0', port=8000)
