from flask import Flask, render_template, Request, request
from flask.ext import login
import sqlite3
import hashlib

app = Flask(__name__)

def passHash(pwd):
	spwd = str(pwd)
	return hashlib.sha256(spwd).hexdigest()

# Views
@app.route('/')
@app.route('/index')
def greeting ():
    #return 'normal string'
    return render_template('index.html')
 		
@app.route('/login', methods=["GET", "POST"])
def login():
	if request.method == "POST":
		print request.form['username'], request.form['password']
		user = request.form['username']
		ph = passHash(request.form['password'])
		con = sqlite3.connect('interviewer.db')
		c=con.cursor()
		c.execute("""SELECT passhash FROM users WHERE UserName=?""", [user])
		dbpasshash=c.fetchone()
		con.close()
		if dbpasshash[0] == ph:
			return "login accepted"
		else:
			return "login refused"
	else:
		return render_template('login.html')

@app.route('/interviews')
def Interviews():
	return render_template("Interviews.html")
		
@app.route('/accounts', methods=["GET", "POST"])
def account():
    if request.method == 'POST':
		email = request.form['Email']
		user = request.form['UserName']
		password = passHash(request.form['Password'])
		con = sqlite3.connect('interviewer.db')
		c = con.cursor()
		c.execute("""insert into users(email, username, passhash) values(?, ?, ?)""", [email, user, password])
		c.execute("""select * from users""")

@app.route('/new-account')
def new_account():
			return render_template("Account.html")
			
@app.route('/forgot')
def forgot():
	return render_template('Forgot.html')

# Views
@app.route('/interviews/jrsqldev', methods=["GET", "POST"])
def jrsqldev():
	if request.method == 'POST':
		cand = request.form['candidate']
		cem = request.form['candidate_email']
		cphone = request.form['candidate_phone']
		dbfund = request.form['database_fundamentals']
		entexp = request.form['enterprise_years_experience']
		qopt = request.form['query_optimization']
		largdat = request.form['facility_large_datasets']
		ntier = request.form['notions_n_tier_architecture']
		ETL = request.form['ETL_processes']
		whyadv = request.form['why_advise']
		weak = request.form['weaknesses']
		quest = request.form['questions']
		con = sqlite3.connect('interviewer.db')
		c = con.cursor()
		c.execute("""insert into jrsqldev_interview (candidate, candidate_email, candidate_phone, database_fundamentals, enterprise__years_experience, query_optimization, facility_large_datasets, notions_n_tier_architecture,
		ETL_processes, why_advise, weaknesses, questions) values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", 
		[cand, cem, cphone, dbfund, entexp, qopt, largdat, ntier, ETL, whyadv, weak, quest])
		c.execute("""select * from jrsqldev""")
		con.commit()
		return render_template('interviews.html')
		con.close()
	else:
		return render_template('jrsqldev_interview.html')
	
@app.route('/interviews/midlevel_dev', methods=["GET", "POST"])
def midlevel_dev():
	if request.method == 'POST':
		cand = request.form['candidate']
		cem = request.form['candidate_email']
		cphone = request.form['candidate_phone']
		exp = request.form['years_experience']
		cflu = request.form['c_sharp_fluency']
		sql = request.form['sql_base']
		large = request.form['facility_large_datasets']
		weak = request.form['weaknesses']
		whyadv = request.form['why_advise']
		quest = request.form['questions']
		con = sqlite3.connect('interviewer.db')
		c = con.cursor()
		c.execute("""insert into midlevel_dev_interview (candidate, candidate_email, candidate_phone, years_experience,
		c_sharp_fluency, sql_base, facility_large_datasets, weaknesses, why_advise, questions) valyes (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
		[cand, cem, cphone, exp, cflu, sql, large, weak, whyadv, quest])
		c.execute("""select * from midlevel_dev""")
		con.commit()
		return render_template("interviews.html.")
		con.close()
	else:
		return render_template('midlevel_dev_interview.html')

# Start app
if __name__ == '__main__':
    app.run(debug=True)

