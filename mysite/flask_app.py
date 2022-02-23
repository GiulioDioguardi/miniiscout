import json
import os

from flask import Flask, render_template, abort, request

app = Flask(__name__)

def read_json_file(filename):
    with open(filename) as _file:
        return json.load(_file)

ROOT = os.path.dirname(os.path.abspath(__file__))
QUESTIONS = read_json_file(os.path.join(ROOT, "questions.json"))

def get_answered_questions():
    answered = []
    for q, cookie in enumerate(request.cookies):
        if "Bjxdd03chm" == request.cookies[cookie]:
            answered.append(q + 1)
    return answered

@app.context_processor
def inject_debug():
    return dict(debug=app.debug)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def question_list():
    return render_template('list.html', questions=QUESTIONS, answered=get_answered_questions())

@app.route('/map/<questionnumber>')
def map_page(questionnumber):
    try:
        return render_template('map.html', question=QUESTIONS[int(questionnumber) - 1], number=questionnumber)
    except (IndexError, ValueError):
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
