#from package import Class
from flask import Flask 
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db=SQLAlchemy()

#create a function that creates a web application
# a web server will run this web application
def create_app():
  
    app = Flask(__name__)

    #we use this utility module to display forms quickly
    bootstrap = Bootstrap5(app)

    #A secret key for the session object
    app.secret_key = 'somerandomvalue'

    #Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traveldb.sqlite'
    db.init_app(app)

    #config upload folder
    UPLOAD_FOLDER = '/static/image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
    
    #add Blueprints
    from . import views
    app.register_blueprint(views.bp)
    # from . import auth
    # app.register_blueprint(auth.authbp)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    return app
