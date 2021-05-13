from flask import Blueprint, render_template, request,jsonify,json,flash
from flask_login import login_required, current_user
from .models import Notes
from . import db

views = Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
@login_required
def home():
  if request.method == 'POST':
    data = request.form.get('note')
    if len(data)<1:
      flash('Note cannot be less than 1 Character','error')
    else:
      note = Notes(data=data,user_id=current_user.id)
      db.session.add(note)
      db.session.commit()
      flash('Note Added','success')
  return render_template('home.html',user = current_user)
  
@views.route('/deleteNote',methods=['POST'])
def deleteNote():
  note = json.loads(request.data)
  noteId = note['noteId']
  note = Notes.query.get(noteId)
  if note:
    db.session.delete(note)
    db.session.commit()
    flash('Note deleted!','error')
  return jsonify({})