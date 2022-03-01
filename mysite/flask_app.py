import hashlib

from flask import Flask, render_template, abort, request

from question import get_questions

app = Flask(__name__)
QUESTIONS = get_questions()

def get_answered_questions():
    answered = []
    for cookie in request.cookies:
        if "FQzEhblF99" == request.cookies[cookie]:
            answered.append(cookie)
    print(answered)
    return answered

def md5(s):
    return hashlib.md5(s).hexdigest()

@app.context_processor
def inject_debug():
    return dict(debug=app.debug)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def question_list():
    answered = get_answered_questions()
    app.logger.info(answered)
    return render_template('list.html', md5=md5, questions=QUESTIONS, answered=answered)

@app.route('/map/<questionnumber>')
def map_page(questionnumber):
    try:
        return render_template('map.html', question=QUESTIONS[int(questionnumber) - 1], number=questionnumber)
    except (IndexError, ValueError):
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
