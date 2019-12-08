import os
from flask import Flask, render_template,url_for,session,request, redirect
from models import * 
from flask_session import Session
from tempfile import mkdtemp

app = Flask(__name__)

app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

with app.app_context():
	db.create_all()

@app.route("/")
def home():
	return redirect(url_for('login'))

@app.route("/profile")
def profile():

	return render_template("profile.html")

@app.route("/edit")
def edit():

	render_template("edit.html")

@app.route("/logout")
def logout():
	key_list = list(session.keys())
	for key in key_list:
		session.pop(key)
	return redirect(url_for('login'))


@app.route("/login",methods=["GET", "POST"])
def login():
	if request.method == "POST":
		user_name = request.form.get('name')
		password = request.form.get('password') 

		loged = user.query.filter_by(name=user_name, password=password).first()
		if loged is not None:
			session["user_name"] = user_name
			session["password" ] = password
			return render_template('profile',var=loged )
		 else:
			return render_template('error.html')
	else: ## request.method == "GET"
		if "user_name" not in session and "password" not in session :
			return render_template("login.html")
		else:
			user_name = session["user_name"]
			password = session["password"]
			loged = user.query.filter_by(name=user_name, password=password).first()
			return render_template('student',var=loged )


@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "POST":
		user_name = request.form.get('name')
		password = request.form.get('password') 
		email = request.form.get('email')
		add_user(user_name,password,email)
		session["user_name"] = user_name
		session["password" ] = password
		return redirect(url_for('login'))
	else:
		return render_template("register.html")