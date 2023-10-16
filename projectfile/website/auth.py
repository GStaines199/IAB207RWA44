from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
#new imports:
from flask_login import login_user, login_required, logout_user
from flask_bcrypt import generate_password_hash, check_password_hash
from .models import User
from . import db

#create a blueprint
authbp = Blueprint('auth', __name__)


#not dont yet feel free to change it or delete it 
@authbp.route('/login', methods=['GET', 'POST'])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        print("Logged in!")
        flash("You logged in!")
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=loginForm, heading='Login')

@authbp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print("Registerd!")
        return redirect(url_for('auth.login'))
    return render_template('user.html', form=form)

# this is a hint for a login function
# @bp.route('/login', methods=['GET', 'POST'])
# def authenticate(): #view function
#     print('In Login View function')
#     login_form = LoginForm()
#     error=None
#     if(login_form.validate_on_submit()==True):
#         user_name = login_form.user_name.data
#         password = login_form.password.data
#         user = User.query.filter_by(name=user_name).first()
#         if user is None:
#             error='Incorrect credentials supplied'
#         elif not check_password_hash(user.password_hash, password): # takes the hash and password
#             error='Incorrect credentials supplied'
#         if error is None:
#             login_user(user)
#             nextp = request.args.get('next') #this gives the url from where the login page was accessed
#             print(nextp)
#             if next is None or not nextp.startswith('/'):
#                 return redirect(url_for('index'))
#             return redirect(nextp)
#         else:
#             flash(error)
#     return render_template('user.html', form=login_form, heading='Login')
