#!/usr/bin/env python
# coding=utf8

"""
A demo to show the unexpected `super()` escape when use `pyjade` together with `jinja2`
"""

from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/')
def index():
    return render_template('example.jade')


if '__main__' == __name__:
    app.run(debug=True)
