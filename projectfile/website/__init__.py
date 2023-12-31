#from package import Class
from flask import Flask, render_template
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
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Epicureandb.sqlite'
    db.init_app(app)

    #config upload folder
    UPLOAD_FOLDER = 'static\img'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
    
    #add Blueprints
    from . import views
    app.register_blueprint(views.bp)
    from . import events
    app.register_blueprint(events.eventbp)
    from . import auth
    app.register_blueprint(auth.authbp)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(error_404): 
      return render_template("error.html", error=error_404)
    
    @app.errorhandler(500) 
    # inbuilt function which takes error as parameter 
    def internal_error(error_500): 
      return render_template("error.html", error=error_500)
    
    return app