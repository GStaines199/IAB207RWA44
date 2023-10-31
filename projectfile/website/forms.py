from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, BooleanField, IntegerField, SelectField, DateTimeField
from wtforms import widgets
from dateutil.relativedelta import *
from dateutil.easter import *
from dateutil.rrule import *
from dateutil.parser import *
from datetime import *
from wtforms.validators import InputRequired, Email, EqualTo, Length
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'JPEG', 'png', 'jpg', 'jpeg'}

#creates the login information
class LoginForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired('Enter user name')], render_kw={"placeholder": "Enter user name"})
    password=PasswordField("Password", validators=[InputRequired('Enter user password')], render_kw={"placeholder": "Enter user password"}, id="password")
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()], render_kw={"placeholder": "Enter user name"})
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")], render_kw={"placeholder": "Enter email address"})
    #linking two fields - password should be equal to data entered in confirm
    Phone_Number = StringField("Phone Number", validators=[InputRequired()], render_kw={"placeholder": "Enter phone number"})
    Address = StringField("Address", validators=[InputRequired()], render_kw={"placeholder": "Enter address"})
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")], render_kw={"placeholder": "Enter password"})
    confirm = PasswordField("Confirm Password", validators=[InputRequired()], render_kw={"placeholder": "Re-enter password"})

    #submit button
    submit = SubmitField("Register")

#create event
class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Event Image', validators=[
        FileRequired(message='Image cannot be empty'),
        FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, png, jpg')])   
    price = IntegerField('Price ($)',  validators=[InputRequired()])
    theme = StringField('Event Theme', validators=[InputRequired()])
    Dietry = StringField('Dietry', validators=[InputRequired()])
    SkillLevel = SelectField('Skill Level', validators=[InputRequired()], choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert'), ('Foody', 'Foody'), ('Chef', 'Chef'), ('Family Friendly', 'Family Friendly')])
    startdate = StringField('Start Date & Time', validators=[InputRequired()], widget=widgets.Input(input_type='datetime-local'))
    enddate = StringField('End Date & Time', validators=[InputRequired()],widget=widgets.Input(input_type='datetime-local'))
    location = StringField('Location', validators=[InputRequired()])
    status = SelectField('Status', validators=[InputRequired()], choices=[('Active', 'Active'), ('Limited', 'Limited'), ('Sold Out', 'Sold Out'), ('Canceled', 'Canceled')])
    submit = SubmitField("Post Event")

class EventUpdateForm(FlaskForm):
    name = StringField('Event Name', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Event Image', validators=[
        FileRequired(message='Image cannot be empty'),
        FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, png, jpg')])   
    price = IntegerField('Price ($)',  validators=[InputRequired()])
    startdate = StringField('Start Date & Time', validators=[InputRequired()], widget=widgets.Input(input_type='datetime-local'))
    enddate = StringField('End Date & Time', validators=[InputRequired()],widget=widgets.Input(input_type='datetime-local'))
    location = StringField('Location', validators=[InputRequired()])
    status = SelectField('Status', validators=[InputRequired()], choices=[('Active', 'Active'), ('Limited', 'Limited'), ('Sold Out', 'Sold Out'), ('Canceled', 'Canceled')])
    submit = SubmitField("Update Event")
    
class CommentForm(FlaskForm):
    text = TextAreaField('Text', validators=[InputRequired()])
    submit = SubmitField("Create")