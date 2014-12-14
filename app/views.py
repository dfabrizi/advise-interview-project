from flask import render_template
from app import app
import sqlite3

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')
	
@app.route('/Login')
def Login():
	return render_template('Login.html')
"""	
login_manager = login.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.get(id)
	
@app.route("/log_me_in", methods=["GET", "POST"])
def log_me_in():
    form = LoginForm()
    if form.validate_on_submit():
        login_user(UserName)
        flash("Logged in successfully.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("Login.html", form=form)
"""
		
@app.route('/account')
def account():
	if request.method == "POST":
		pass
	else:
		return render_template("Account.html")

@app.route('/interviews')
def interviews():
	return render_template('interviews.html')
	
@app.route('/New_Interview')
def New_Interview():
	return render_template('New_Interview.html')

@app.route('/Forgot')
def Forgot():
	return render_template('Forgot.html')

