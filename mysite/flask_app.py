import traceback

import werkzeug.exceptions
from flask import Flask, render_template, abort, request

from question import get_questions

app = Flask(__name__)
QUESTIONS = get_questions()

def get_answered_questions():
    answered = []
    for cookie in request.cookies:
        if "FQzEhblF99" == request.cookies[cookie]:
            answered.append(cookie)
    return answered

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
    return render_template('list.html', questions=QUESTIONS, answered=answered)

@app.route('/map/<questionhash>')
def map_page(questionhash):
    for i, q in enumerate(QUESTIONS):
        if q['hashed_title'] == questionhash:
            question = q
            questionnumber = i + 1
            break
    else:
        abort(404)

    return render_template('map.html', question=question, number=questionnumber)

@app.errorhandler(werkzeug.exceptions.NotFound)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, werkzeug.exceptions.HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    app.logger.error("\n" + traceback.format_exc())
    return render_template("500_generic.html"), 500

if __name__ == "__main__":
    app.run(debug=True)
