from flask import Flask, render_template, Request, request
from flask.ext import login
import sqlite3
import hashlib

app = Flask(__name__)

def passHash(pwd):
	spwd = str(spwd)
	return hashlib.sha256(pwd).hexdigest()

# Views

@app.route('/')
def greeting ():
    #return 'normal string'
    return render_template('index.html')
    
@app.route('/Login')
@app.route('/accounts', methods=["GET", "POST"])
def account():
    if request.method == 'POST':
		user = request.form['UserName']
		password = passHash(request.form['Password'])
		conn = sqlite3.connect('example.db')
		c = conn.cursor()
		c.execute("""insert into accounts values(?, ?)""", [user, password])
		c.execute("""select * from accounts""")
		conn.commit()
		return render_template('index.html')
		conn.close()
    else:
        return render_template('account.html')

# Start app
if __name__ == '__main__':
    app.run(debug=True)