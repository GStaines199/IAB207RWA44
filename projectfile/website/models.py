from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False)
    phone = db.Column(db.String(100), index=True, nullable=False)
    address = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)

    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')


class Event(db.Model):
    __tablename__ = 'events'
    eventid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(200))
    image = db.Column(db.String(400))
    ticketPrice = db.Column(db.Integer)
    status = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.now())
    startdate = db.Column(db.DateTime)
    enddate = db.Column(db.DateTime)
    Dietary = db.Column(db.String(80))
    Theme = db.Column(db.String(80))
    SkillLevel = db.Column(db.String(80))
    location = db.Column(db.String(100))
    userid = db.Column(db.String(80))
    # ... Create the Comments db.relationship
	# relation to call destination.comments and comment.destination
    comments = db.relationship('Comment', backref='event')



class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.eventid'), nullable=False)


class Tickets(db.Model):
    __tablename__ = 'tickets'
    ticketid = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    event_id = db.Column(db.Integer, db.ForeignKey('events.eventid'), nullable=False)
    FirstName = db.Column(db.String(80))
    LastName = db.Column(db.String(80))
    NumTickets = db.Column(db.Integer)
    TotalPrice = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now())
    date = db.Column(db.DateTime)


class Favourites(db.Model):
    __tablename__ = 'favourites'
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.eventid'), nullable=False, primary_key=True)

    