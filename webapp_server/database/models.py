from webapp_server.database import db

class User(db.Model):
	"""Model for users."""
	__tablename__ = 'user'
	id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
	first_name = db.Column('first_name', db.String(25), nullable=False)
	last_name = db.Column('last_name', db.String(25), nullable=False)
	email = db.Column('email', db.String(50), nullable=False)
	password = db.Column('password', db.String(50), nullable=False)
	created_on = db.Column('created_on', db.DateTime, default=db.func.now())
	last_modified = db.Column('last_modified', db.DateTime, default=db.func.now(), onupdate=db.func.now())

	def __init__(self, first_name: str, last_name: str, email:str, password: str):
		# TODO think about constraints
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
