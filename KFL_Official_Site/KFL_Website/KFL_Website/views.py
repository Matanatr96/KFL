"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from KFL_Website import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='KFL Official',
        description='Welcome to the official KFL website!',
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
