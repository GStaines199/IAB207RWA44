from flask import Blueprint, render_template, redirect, url_for, flash, request
from .models import Event, Comment, Favourites
from flask_login import current_user
from . import db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    # Get filter values from the form
    dietary_preference = request.args.get('dietary', type=str)
    theme = request.args.get('theme', type=str)
    skill_level = request.args.get('skill_level', type=str)

    # Check if all three categories are default
    all_default = (
        dietary_preference == 'Dietary Preference' and
        theme == 'Seasonal / Cultural Options' and
        skill_level == 'Skill Level Filter'
    )

    # Query events based on selected filters or display all events
    if all_default:
        events = Event.query.all()
    else:
        events = Event.query.filter(
            (Event.Dietary == dietary_preference) if dietary_preference else True,
            (Event.Theme == theme) if theme else True,
            (Event.SkillLevel == skill_level) if skill_level else True
        ).all()

    return render_template('index.html', events=events)


