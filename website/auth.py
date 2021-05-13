from flask import Blueprint, render_template,flash, request, redirect, url_for
from .models import User
from . import db
from flask_login import login_required,current_user, login_user, logout_user

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    if user:
      if password==user.password:
        login_user(user)
        return redirect(url_for('views.home'))
      else:
        flash("Wrong Password!",'error')
    else:
      flash("Email doesn't Exists", 'error')
  return render_template('login.html',user = current_user)

@auth.route('/signup',methods=['GET','POST'])
def signup():
  if request.method == "POST":
    email = request.form.get('email')
    first_name = request.form.get('first_name')
    password1 = request.form.get('password1')
    password2= request.form.get('password2')
    user = User.query.filter_by(email=email).first()
    if len(email) < 3:
      flash("Email address cannot be less than 3", 'error')
    elif user:
      flash('Email already exists!','error')
    elif len(first_name) < 1:
      flash('First Name cannot be less than 1','error')
    elif password1 != password2:
      flash('Passwords do not Match','error')
    elif len(password1) < 8:
      flash('Password length cannot be less than 8','error')
    else:
      newUser = User(email=email,first_name=first_name,password=password1)
      db.session.add(newUser)
      db.session.commit()
      login_user(newUser)
      flash('Signed Up successfully','success')
      return redirect(url_for('views.home'))
  return render_template('signup.html',user = current_user)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('auth.login'))