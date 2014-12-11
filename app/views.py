from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
	
@app.route('/danny')
def danny():
	return render_template('index.html', name='Daniel Fabrizio')
	
	
@app.route('/something')
def somethingHere():
	return "Something here"
	
@app.route('/newhtml')
def myhtml():
# Render template will look inside the template folder for the file that you pass 
# as the first argument of render_template()
	return render_template('newhtml.html')

# define 5 routes
# 3 should return strings
# 2 should return html pages that you have stored in the  templates folder
	
@app.route('/pizza')
def mama_mia():
	return "Mama Mia!"
	
@app.route('/box')
def box():
	return "*" * 35+"\n"+"*"+" Dan Fabrizio" +" "*19 +"*"+"\n"+"*" +" I wrote this...in a box"+" "*8+"*"+"\n"+"*"*35

@app.route('/racecar')
def racecar():
	return "'racecar' spelled backwards is still 'racecar'"

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/account')
def account():
	return render_template('Account.html')

@app.route('/<animal>')
def printAm(animal):
	return animal

@app.route('/novabasketball')
def novabasketball():
	return render_template('novabasketball.html')

@app.route('/physics')
def physics():
	return render_template('physics.html')
	
@app.route('/indexex')
def indexex():
	return render_template('indexex.html')

@app.route('/interview')
def interview():
	return render_template('interviews.html')

