import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing

DATABASE = 'C:\tmp\flaskr.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__)
app.config.from_object(__name__)


def connect_db():
	sqlite3.connect(app.config['DATABASE'])

def init_db():
	with closing(connect_db()) as db: #closing is method we imported, create connection to database
		with app.open_resource('schema.sql', mode='r') as f: #open schema.sql in read mode -- shortened as 'f'
			db.cursor().executescript(f.read()) #use database to execute line-by-line what to do
		db.commit() #commit -- i.e. 'save' - can't delete what's been committed without deleting db or dropping table
	
if __name__ == '__main__':
	app.run()
