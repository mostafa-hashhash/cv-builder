from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class user(db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50),nullable = False)
	email = db.Column(db.String(50),nullable = False)
	password = db.Column(db.String(50),nullable = False)

	def __init__ (self,name,password,email,phone,age,status,tid):
		user.password =  password
		user.phone = phone
		user.age = age
		user.name = name
		user.email = email
		user.status = status
		user.teacher_id = tid

	def add_user(name,password,email,age,phone,tid,status):
		u = user(name=name,age=age,email=email,phone=phone,password=password,status=status,tid=tid)
		db.session.add(u)
		db.session.commit()



class section(db.Model):
	__tablename__ = "lecture"
	id = db.Column(db.Integer,primary_key=True)
	title = db.Column(db.String(40), nullable = False)
	content = db.Column(db.String(200),nullable = False)
	date = db.Column(db.Time(60),nullable = False)
	hw = db.Column(db.String(500),nullable = False)
	teacher_id = db.Column(db.Integer, nullable = False)

	def __init__ (self,title,content,date,tid,hw):
		lecture.title =  title
		lecture.content = content
		lecture.date = date
		lecture.teacher_id = tid
		lecture.hw = hw
	
	def add_lecture(title,content,date,tid,hw):
		u = lecture(title=title,content=content,date=date,tid=tid,hw=hw)
		db.lecture.add(u)
		db.lecture.commit()

