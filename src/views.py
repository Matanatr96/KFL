"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from src import app
from src import sleeper_api as sp

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""

    names = sp.test()

    return render_template(
        'index.html',
        title='KFL Official',
        description=names,
        year=datetime.now().year,
    )

@app.route('/rankings')
def rankings():
    """Renders the contact page."""
    return render_template(
        'rankings.html',
        title='Rankings',
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
