from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, BooleanField, IntegerField
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
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")], render_kw={"placeholder": "Enter password"})
    confirm = PasswordField("Confirm Password", validators=[InputRequired()], render_kw={"placeholder": "Re-enter password"})

    #submit button
    submit = SubmitField("Register")

#create event
class EventForm(FlaskForm):
    name = StringField('EventName', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Event Image', validators=[
        FileRequired(message='Image cannot be empty'),
        FileAllowed(ALLOWED_FILE, message='Only supports PNG, JPG, png, jpg')])   
    price = IntegerField('Price ($)',  validators=[InputRequired()])
    submit = SubmitField("Create")

    
class CommentForm(FlaskForm):
    text = TextAreaField('Text', validators=[InputRequired()])
    submit = SubmitField("Create")