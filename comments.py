from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# event data
events = [
    {"id": 1, "name": "Event 1"},
]

comments = []

# route definition for home page
@app.route('/')
def home():
    return render_template('comments.html', events=events, comments=comments)

# route definition for posting a comment
@app.route('/post_comment', methods=['POST'])
def post_comment():
    # relevant event id
    event_id = int(request.form.get('event_id'))
    commenter_name = request.form.get('commenter_name')
    comment_text = request.form.get('comment_text')
    # timestamp for comment post
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    comments.append({"event_id": event_id, "commenter_name": commenter_name, "comment_text": comment_text, "timestamp": timestamp})

    return render_template('comments.html', events=events, comments=comments)

if __name__ == '__main__':
    app.run(debug=True)

