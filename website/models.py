from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class Notes(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  date_time = db.Column(db.DateTime(timezone=True), default=func.now())
  data = db.Column(db.String(10000))
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
class User(db.Model, UserMixin):
  id = db.Column(db.Integer,primary_key=True)
  email = db.Column(db.String(200),unique=True)
  first_name = db.Column(db.String(50))
  password = db.Column(db.String(150))
  note = db.relationship ('Notes')

