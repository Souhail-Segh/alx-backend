#!/usr/bin/env python3
''' Flask render basic hello html
'''
from flask import Flask, render_template


app = Flask(__name__)
# __name__ the name of the module


@app.route("/")
def home():
    ''' render home page
    '''
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
