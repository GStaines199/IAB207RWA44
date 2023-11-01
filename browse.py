from flask import Flask, render_template

app = Flask(__name__)

# event data
events = [
    # insert name of relevant category
    {"name": "Event 1", "category": "cat 1"},
    {"name": "Event 2", "category": "cat 2"},
    {"name": "Event 3", "category": "cat 3"},
]

@app.route('/')
def landing_page():
    categories = set(event['category'] for event in events)
    return render_template('browse.html', events=events, categories=categories)


