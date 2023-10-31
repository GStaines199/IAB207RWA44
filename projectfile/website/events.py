from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import EventForm, CommentForm, EventUpdateForm
from .models import Event, Comment
from datetime import datetime
from . import db
from werkzeug.utils import secure_filename
from flask_login import current_user, login_required
import os

eventbp = Blueprint('event', __name__, url_prefix='/events')

@eventbp.route('/<id>')
def show(id):
    event = db.session.scalar(db.select(Event).where(Event.eventid==id))
    valid = Event.status
    # create the comment form
    form = CommentForm()    
    return render_template('events/show.html', Event=event, form=form, valid=valid)

@eventbp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
  print('Method type: ', request.method)
  form = EventForm()
  if form.validate_on_submit():

    current_dateTime = datetime.now()
    startdate = datetime.strptime(form.startdate.data, '%Y-%m-%dT%H:%M')
    enddate = datetime.strptime(form.enddate.data, '%Y-%m-%dT%H:%M')

    #call the function that checks and returns image
    db_file_path = check_upload_file(form)
    
    event = Event(name=form.name.data,description=form.description.data, 
    image=db_file_path,ticketPrice=form.price.data, startdate=startdate, enddate=enddate, status=form.status.data, location=form.location.data , 
    user=current_user.name, Dietary=form.Dietry.data, Theme=form.theme.data, SkillLevel=form.SkillLevel.data)
    # add the object to the db session
    db.session.add(event)
    # commit to the database
    db.session.commit()
    #Always end with redirect when form is valid
    return redirect(url_for('main.index'))
  return render_template('events/create.html', form=form)

@login_required
@eventbp.route('/update/<id>', methods=['GET', 'POST'])
def update_event(id):
  # Get the event
  event = db.session.query(Event).get(id)
  form = EventUpdateForm(obj=event)

  if form.validate_on_submit():
    startdate = datetime.strptime(form.startdate.data, '%Y-%m-%dT%H:%M')
    enddate = datetime.strptime(form.enddate.data, '%Y-%m-%dT%H:%M')

    db_file_path = check_upload_file(form)
    
    event.name = form.name.data
    event.description = form.description.data
    event.image = db_file_path
    event.ticketPrice = form.price.data
    event.startdate = startdate
    event.enddate = enddate
    event.status = form.status.data
    event.location = form.location.data
    event.user = current_user.name

    # Commit the changes to the database
    event.session.commit()

  return render_template('events/update.html', form=form)
def check_upload_file(form):
  #get file data from form  
  fp = form.image.data
  filename = fp.filename
  #get the current path of the module file… store image file relative to this path  
  BASE_PATH = os.path.dirname(__file__)
  #upload file location – directory of this file/static/image
  upload_path = os.path.join(BASE_PATH, 'static/img/', secure_filename(filename))
  #store relative path in DB as image location in HTML is relative
  db_upload_path = 'static/img/' + secure_filename(filename)
  #save the file and return the db upload path
  fp.save(upload_path)
  return db_upload_path

@eventbp.route('/<id>/comment', methods = ['GET','POST'])
def comment():
    print('method type: ', request.method) 
    form = CommentForm()
    if form.validate_on_submit():
        print(f"The following comment has been posted: {form.text.data}")
    return redirect(url_for('event.show', id=1))
