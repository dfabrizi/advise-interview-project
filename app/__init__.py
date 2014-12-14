from flask import Flask
from flask.ext import login

app = Flask(__name__)
from app import views