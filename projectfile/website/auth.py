from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import LoginForm, RegisterForm, EditProfileForm
#new imports:
from flask_login import login_user, login_required, logout_user, current_user
from flask_bcrypt import generate_password_hash, check_password_hash
from .models import User, Event, Favourites, Tickets
from . import db
from sqlalchemy import update

#create a blueprint
authbp = Blueprint('auth', __name__ )

@authbp.route('/register', methods=['GET', 'POST'])
def register():
    register = RegisterForm()
    #the validation of form is fine, HTTP request is POST
    if (register.validate_on_submit()==True):
            #get username, password and email from the form
            uname = register.user_name.data
            pwd = register.password.data
            email = register.email.data
            address = register.Address.data
            phone = register.Phone_Number.data
            #check if a user exists
            user = db.session.scalar(db.select(User).where(User.name==uname))
            if user:#this returns true when user is not None
                flash('Username already exists, please try another')
                return redirect(url_for('auth.register'))
            # don't store the password in plaintext!
            pwd_hash = generate_password_hash(pwd)
            #create a new User model object
            new_user = User(name=uname, password_hash=pwd_hash, email=email, phone=phone, address=address)
            db.session.add(new_user)
            db.session.commit()
            #commit to the database and redirect to HTML page
            return redirect(url_for('auth.login'))
    #the else is called when the HTTP request calling this page is a GET
    else:
        return render_template('user.html', form=register, heading='Register')

@authbp.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    error = None
    if(login_form.validate_on_submit()==True):
        #get the username and password from the database
        user_name = login_form.user_name.data
        password = login_form.password.data
        user = db.session.scalar(db.select(User).where(User.name==user_name))
        #if there is no user with that name
        if user is None:
            error = 'Incorrect username or password'#could be a security risk to give this much info away
        #check the password - notice password hash function
        elif not check_password_hash(user.password_hash, password): # takes the hash and password
            error = 'Incorrect username or password'
        if error is None:
            #all good, set the login_user of flask_login to manage the user
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash(error, 'error')
    return render_template('user.html', form=login_form, heading='Login')

@authbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@authbp.route('/account/profile', methods=['GET', 'POST'])
@login_required
def account():
    form = EditProfileForm()

    if (form.validate_on_submit()==True):
        # Update user details in the database
        name = form.name.data if form.name.data is not None else current_user.name
        email = form.email.data if form.email.data is not None else current_user.email
        address = form.address.data if form.address.data is not None else current_user.address
        phone = form.phone.data if form.phone.data is not None else current_user.phone
        # Assuming you have a database session and commit changes
        updateUser = update(User).where(User.id==current_user.id).values(name=name, email=email, address=address, phone=phone)
        db.session.execute(updateUser)
        db.session.commit()

        # Redirect to the profile page after saving changes
        return redirect(url_for('auth.account'))

    return render_template('account/profile.html', form=form, current_user=current_user)

@authbp.route('/account/myevents')
@login_required
def myevents():
    user = current_user.name
    userevents = Event.query.filter_by(user=user).all()
    return render_template('account/myevents.html', UserEvent=userevents, heading='MyEvents')

@authbp.route('/account/tickets')
@login_required
def tickets():

    return render_template('account/tickets.html', heading='Tickets')

@authbp.route('/account/favourites')
@login_required
def favourites():
    user_id = current_user.id

    user_favorites = Favourites.query.filter_by(user_id=user_id).all()

    event_ids = [fav.event_id for fav in user_favorites]

    favorite_events = Event.query.filter(Event.eventid.in_(event_ids)).all()

    return render_template('account/favourites.html',favorite_events=favorite_events, heading='Favourites')

@authbp.route('/toggle_favorite/<int:id>', methods=['GET', 'POST'])
@login_required
def toggle_favorite(id):
    # Check if the event is already in favorites
    event = db.session.scalar(db.select(Event).where(Event.eventid==id))
    favorite = Favourites.query.filter_by(user_id=current_user.id, event_id=id).first()
    fragment = request.referrer.split('#', 1)[-1]
    if favorite:
        # Event is already in favorites, remove it
        db.session.delete(favorite)
    else:
        # Event is not in favorites, add it
        new_favorite = Favourites(user_id=current_user.id, event_id=id)
        db.session.add(new_favorite)

    db.session.commit()
    return redirect(f"{request.referrer}#{fragment}")

@authbp.route('/accounts/delete/<int:id>')
def delete_event(id):
    event = Event.query.get_or_404(id)
    db.session.delete(event)
    db.session.commit()
    user = current_user.name
    userevents = Event.query.filter_by(user=user).all()
    return render_template('account/myevents.html', UserEvent=userevents, heading='MyEvents')