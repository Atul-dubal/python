import flask
from flask import Flask, request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
@app.route('/')
def home():
   return "hii"
 

app.run(debug = True)
	