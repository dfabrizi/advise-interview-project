from flask import Flask, render_template, Request, request, redirect, url_for
import sqlite3
import hashlib

app = Flask(__name__)

def passHash(pwd):
	spwd = str(pwd)
	return hashlib.sha256(spwd).hexdigest()
	
	
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# Views
@app.route('/')
@app.route('/index')
def greeting ():
    return render_template('index.html')
 		
@app.route('/login', methods=["GET", "POST"])
def login():
	if request.method == "POST":
		# print request.form['username'], request.form['password']
		user = request.form['username']
		ph = passHash(request.form['password'])
		con = sqlite3.connect('interviewer.db')
		c = con.cursor()
		c.execute("""SELECT passhash FROM users WHERE UserName=?""", [user])
		dbpasshash = c.fetchone()
		con.close()
		if dbpasshash is None:
			return "login denied"

		if dbpasshash[0] == ph:
			message = "login accepted"
			return message
		else:
			message = "login denied"
			return message
	else:
		return render_template('Login.html')

@app.route('/interviews')
def Interviews():
	con = sqlite3.connect('interviewer.db')
	con.row_factory = dict_factory
	c=con.cursor()
	c.execute("""SELECT * FROM jrsqldev_interview""")
	resultsjr = c.fetchall()
	c.execute("""SELECT * FROM midlevel_dev_interview""")
	resultsmid = c.fetchall()
	con.close()
	return render_template("Interviews.html", jr=resultsjr, mid=resultsmid)
		
@app.route('/accounts', methods=["GET", "POST"])
def account():
	if (request.method == 'POST'):
		email = request.form['Email']
		user = request.form['UserName']
		password = passHash(request.form['Password'])
		con = sqlite3.connect('interviewer.db')
		c = con.cursor()
		c.execute("""insert into users(email, username, passhash) values(?, ?, ?)""", [email, user, password])
		c.execute("""select * from users""")
		con.commit()
		con.close();
		return render_template('Login.html')
	else :
		return render_template('Account.html')


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
		#c.execute("""select * from jrsqldev""")
		con.commit()
		con.close()
		return redirect(url_for('Interviews'))
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
		c_sharp_fluency, sql_base, facility_large_datasets, weaknesses, why_advise, questions) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
		[cand, cem, cphone, exp, cflu, sql, large, weak, whyadv, quest])
		#c.execute("""select * from midlevel_dev""")
		con.commit()
		return redirect(url_for('Interviews'))
		con.close()
	else:
		return render_template('midlevel_dev_interview.html')

#pass along an identifier based on previous section picked
@app.route('/interviews/loaded_form/<name><int:job_id>', methods=["GET", "POST"])
def load_form(name, job_id):
	con = sqlite3.connect('interviewer.db')
	con.row_factory = dict_factory
	c=con.cursor()
 
 	#might want to use switch statement..
 	if job_id is 1:
		c.execute("""SELECT * FROM jrsqldev_interview WHERE candidate=?""", [name])
		data = c.fetchall()
		keys = data[0].keys()	
		return render_template('jrsqldev_interview.html', data=data, keys=keys)
	elif job_id is 2:
		c.execute("""SELECT * FROM midlevel_dev_interview WHERE candidate=?""", [name])
		data = c.fetchall()
		keys = data[0].keys()
		return render_template('midlevel_dev_interview.html', data=data, keys=keys)		
	con.close()
	return render_template('loaded_form.html', data=data, keys=keys)

# Start app
if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)

