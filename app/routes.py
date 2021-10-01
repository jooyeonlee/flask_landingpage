from app import app
from flask import render_template, redirect, url_for
from flask_login import current_user

@app.route('/')
def home():
    if current_user.is_authenticated:
        return render_template('index.html')
    return redirect(url_for('user.signin'))