#!/usr/bin/env python3
""" webapp for interacting with sign """
import os
from flask import Flask, request
from flask import render_template, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/write', methods=['POST', 'GET'])
def add_message_to_queue():
    if request.method == 'POST':
        requested_message = request.form['message']
        print(requested_message)
    else:
        print('Method is not POST')
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True  # updates the page as the code is saved
    HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
    PORT = int(os.environ.get('PORT', 443))
    app.run(host=HOST, port=PORT)
