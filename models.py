from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class user(db.Model):
	__tablename__ = "user"
	id       = db.Column(db.Integer, primary_key=True)
	name     = db.Column(db.String(50),nullable = False)
	password = db.Column(db.String(50),nullable = False)
	email    = db.Column(db.String(50),nullable = False)
	address  = db.Column(db.String(50),nullable = False)
	linkedin = db.Column(db.String(50),nullable = False)
	github   = db.Column(db.String(50),nullable = False)
	phone    = db.Column(db.Integer   ,nullable = False)

	def __init__ (self,name,password,email,phone,address,linkedin,github):
		user.password =  password
		user.phone = phone
		user.name = name
		user.email = email
		user.linkedin = linkedin
		user.github = github
		user.address = address

	def add_user(name,password,email,address,phone,linkedin,github):
		u = user(name=name,address=address,email=email,phone=phone,password=password,github=g,linkedin=l)
		db.session.add(u)
		db.session.commit()


class section(db.Model):
	__tablename__ = "section"
	id      = db.Column(db.Integer ,primary_key=True)
	title   = db.Column(db.String  ,nullable = False)
	role    = db.Column(db.String  ,nullable = False)
	content = db.Column(db.String  ,nullable = False)
	position= db.Column(db.String  ,nullable = False)
	date    = db.Column(db.Time    ,nullable = False)
	user_id = db.Column(db.Integer ,db.ForeignKey("user.id"),nullable= False)
	userR   = db.relationship('user', foreign_keys='section.user_id')

	def __init__ (self,title,content,role,position,date):
		section.title =  title
		section.content = content
		section.date = date
		section.role = role
		section.position = position

	def add_section(title,content,date,position,role):
		u = section(title=title,content=content,date=date,role=role,position=position)
		db.section.add(u)
		db.section.commit()
