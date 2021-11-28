"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from src import app, sleeper_api
from flask_table import Table, Col

from src.sleeper_api import Sleeper

s = Sleeper()

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    return render_template(
        'index.html',
        title='KFL Official',
        year=datetime.now().year,
    )

@app.route('/rankings')
def rankings():
    """Renders the contact page."""

    #users = s.getUsers()
    table = s.getTable()


    return render_template(
        'rankings.html',
        title='Rankings',
        table = table,
        year=datetime.now().year,
        message='OFFICIAL RANKINGS OF KFL'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year
    )
