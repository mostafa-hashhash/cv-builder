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
	loged = user.query.filter_by(name=session["user_name"], password=session["password"]).first()
	data = section.query.filter_by(user_id = loged.id).all()
	return render_template("edit.html",person=loged, info=data)


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
		data = section.query.filter_by(user_id = loged.id).all()

		if loged is not None:
			session["user_name"] = user_name
			session["password" ] = password
			return render_template('profile.html',person=loged, info=data )
		else:
			return render_template("error.html", message="No such Credentials.")

	else: ## request.method == "GET"
		if "user_name" not in session and "password" not in session :
			return render_template("login.html")
		else:
			user_name = session["user_name"]
			password = session["password"]
			loged = user.query.filter_by(name=user_name, password=password).first()
			##data  = db.session.query(user,section).filter(user.id == section.user_id ).all()
			##data = section.query.get(loged.id).user
			data = section.query.filter_by(user_id = loged.id).all()
			return render_template('profile.html',person=loged ,info = data )


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

@app.route("/diplay/<int:user_id>" )
def users_api(x):

	loged = user.query.get(user_id)
	if loged is None:
		return jsonify ( {"error":"Invalid Profile ID"} ), 422
		data = section.query.filter_by(user_id = x).all()
	else:
		return jsonify({
				"name" : loged.name,
				"email": loged.email,
				"phone": loged.phone
			})