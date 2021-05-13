from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db_name = 'data.db'
db = SQLAlchemy()

def create_app():
  
  app = Flask(__name__)
  
  app.config['SECRET_KEY'] = "secretxkeyxroit"
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_name}'
  app.config['SEND_FILE_MAX_AGE_DEFAULT'] 

  db.init_app(app)
  
  from .models import User, Notes
  create_database(app)
  
  from .views import views
  app.register_blueprint(views, url_prefix='/')
  
  from .auth import auth
  app.register_blueprint(auth,url_prefix='/')
  
  loginManager = LoginManager()
  loginManager.login_view = 'auth.login'
  loginManager.init_app(app)
  
  @loginManager.user_loader
  def load_user(id):
    print(User.query.get(int(id)))
    return User.query.get(int(id))
  
  return app

def create_database(app):
  if not path.exists('website/'+db_name):
    db.create_all(app=app)