import os

# from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

#from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

@app.route("/")
def index():
    """Show portfolio of stocks"""
    return("hallo hendrik")