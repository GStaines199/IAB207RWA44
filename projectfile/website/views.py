from flask import Blueprint, render_template, redirect, url_for, flash
from .models import Event, Comment, Favourites
from flask_login import current_user
from . import db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    event = Event.query.all()
    return render_template('index.html', events=event)
